import sys
import itertools
from typing import Iterable
from dataclasses import dataclass
from decimal import Decimal

from budget.console import console, econsole
from budget.structures import Summary

rprint = console.print


@dataclass
class Amount:
    balance: Decimal = Decimal(0)
    budget: Decimal = Decimal(0)


def eprint(*a, **kw):
    kw.setdefault("style", "error")
    econsole.print(*a, **kw)
    

def sum_amounts(summaries: Iterable[Summary], start=None):
    if start is None:
        start = {}

    for summary in summaries:
        amount = start.setdefault(summary.commodity, Amount())
        amount.balance += summary.balance
        amount.budget += summary.budget

    return start


def flatten(val):
    return list(itertools.chain.from_iterable(val))
