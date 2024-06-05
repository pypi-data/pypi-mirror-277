#!/usr/bin/env python3

import click

from budget.commands.check import check
from budget.commands.balance import balance
from budget.structures import Args


@click.group()
@click.option("-f", "--file", help="input file")
def cli(**kwargs):
    """Budget helper for hledger"""
    args = Args(**kwargs)
    ctx = click.get_current_context()
    ctx.obj = args


cli.add_command(balance)
cli.add_command(check)
