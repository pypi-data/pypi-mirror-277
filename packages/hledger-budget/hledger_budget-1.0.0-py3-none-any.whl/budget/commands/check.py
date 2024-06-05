import itertools
import sys
from dataclasses import replace

import click
from rich import box
from rich.table import Table

from budget.hledger import bal_csv, bal_budget, prepare_db
from budget.structures import Args, Database, Summary
from budget.utils import eprint, rprint

from ._options import common_options


def sum_summaries(db: Database, commodity: str) -> Summary:
    summed = Summary("total", "", commodity, 0, 0)
    for summary in db.iter(commodity=commodity):
        summed.balance += summary.balance
        if summary.budget:
            if summed.budget is None:
                summed.budget = summary.budget
            else:
                summed.budget += summary.budget
    return summed


def sum_missing_spendings(db: Database, commodity: str) -> Summary:
    fore = Summary("forecast", "", commodity, 0, 0)

    for summary in db.iter(commodity=commodity):
        if summary.budget is None:
            continue

        if summary.budget < summary.balance:
            continue

        fore.balance += summary.budget - summary.balance

    return fore


@click.command()
@common_options
@click.argument("assets", nargs=-1)
@click.option(
    "-t",
    "--title",
    default="Budget Validity Report: {commodity}",
    help="report title",
)
@click.option(
    "--no-auto-excludes",
    is_flag=True,
    default=False,
    help="disable automatic exclusions of unbudgeted and assets accounts from the budget",
)
@click.pass_obj
def check(args: Args, title, assets, no_auto_excludes, **kwargs):
    """Check correctness of budget against available assets."""
    if not assets:
        return

    args = replace(args, **kwargs)

    # This is what users actually want even if they don't know it :)
    #
    # Suppose that we have 2 accounts for our cash:
    #   - assets:bank:checking
    #   - assets:bank:savings
    # Each month we save some cash by transfering it from checking to savings.
    # Hledger includes savings account in budget report, but it also
    # includes its parent: assets:bank. Now, assets:bank:checking quietly
    # contributes to assets:bank (see `hledger bal -E` for proof) and to
    # the sum of expenses. The problem is that checking accounts balance is a
    # result of many transactions which don't contribute to the "budget" or
    # "spending" report, like income.
    if not no_auto_excludes:
        args.excludes.extend(assets)
        args.excludes.append("unbudgeted")

    db = prepare_db(bal_budget(args))

    ass_args = replace(
        args,
        includes=assets,
        excludes=[],
        flags={"cumulative": True, "historical": True, "monthly": True},
    )

    assets_db = prepare_db(bal_csv(ass_args))

    result = True

    def v(cond: bool, msg: str):
        nonlocal result
        result &= cond

        if cond:
            prefix = "PASS"
            color = "green"
        else:
            prefix = "FAIL"
            color = "red"

        return f"[bold {color}][{prefix}][/] {msg}"

    for commodity in db.commodities:
        spendings = sum_summaries(db, commodity)
        if spendings.budget is None:
            eprint(f"[red]No budgeted spendings for {commodity}")
            eprint("[red]Do you have any periodic transactions for this commodity?")
            result = False
            continue

        missing_spendings = sum_missing_spendings(db, commodity)
        forecast = spendings.balance + missing_spendings.balance

        # NOTE: in case there's no assets in a given currency, assets_db.iter()
        # will produce empty iterator, and sum() will return integer (not Decimal) 0.
        # This is the case when you budget in a currency, but rely on auto
        # currency conversion done by bank.
        cash = sum(
            summary.balance
            for summary in assets_db.iter(commodity=commodity)
        )

        remaining_spendings = spendings.budget - spendings.balance
        unbudgeted = cash - remaining_spendings
        forecasted_debit = cash + spendings.balance - forecast

        t = Table(
            title=title.format(commodity=commodity),
            show_header=True,
            header_style="bold",
            box=box.MINIMAL_HEAVY_HEAD,
        )
        t.add_column("Report")
        t.add_column(f"Amount {commodity}", justify="right")
        t.add_column("Check Verdict")

        t.add_row("Money available", f"{cash:.2f}")
        t.add_row(
            "Remaining budgeted spendings",
            str(missing_spendings.balance),
            v(remaining_spendings <= cash, "Enough money for remaining spendings"),
        )
        t.add_row("Spendings this month", str(spendings.balance))
        t.add_row(
            "Total forecasted spendings",
            str(forecast),
            v(
                forecast <= cash + spendings.balance,
                "Sufficient funds for forecasted budgeted and unbudgeted spendings",
            ),
        )
        t.add_row("Total budget this month", str(spendings.budget))
        t.add_row(
            "Unbudgeted funds",
            str(unbudgeted),
            v(unbudgeted >= 0, "Not over-budgeting"),
        )
        t.add_row("Forecasted fall over", str(forecasted_debit))
        rprint(t)

    sys.exit(not result)
