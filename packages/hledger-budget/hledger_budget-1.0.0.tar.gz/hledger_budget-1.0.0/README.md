# hledger-budget

hledger-budget is a wrapper for for `hledger balance --budget` report which
helps maintaining envelope-style budgeting while using goal-based
capabilities for budgeting in hledger.

## Introduction

With envelope-style budgeting one divides available spending money into
"envelopes" which represent spending categories. For example, there may be a
separate envelope for groceries, bills, entertainment and so on. With
[ledger](https://ledger-cli.org/) and [hledger](https://hledger.org) accounts
and subaccounts serve a role of envelopes.

There are 2 typical approaches for ledger and hledger for envelope-style
budgeting:

- by using subaccounts for your main checking account (for example
  `assets:bank:checking:groceries`, `assets:bank:checking:bills` and so on;
- by using virtual accounts (and possibly automated transactions).

hledger-budget proposes a different approach: using goal-based budgeting from
hledger. With hledger you use periodic transactions to set budgeting goals
against "expenses" accounts and track these expenses. One thing which many
hledger tutorials often omit, but which enables periodic transaction for
fluid envelope-stype budgeting, is that "periodic" transactions don't have to
be periodic at all. This gives flexibility necessary for effective
envelope-style budgeting and simplicity of budgeting recurring expenses.

Example budget may look like this (it uses non-balancing virtual accounts
which are only used for hledger's budget reports; alternatively you could
also project your income and balance expenses against it):

```ledger
~ monthly from 2024-01
    (expenses:groceries)        200.00 EUR
    (expenses:bills)            300.00 EUR
    (expenses:car:fuel)         100.00 EUR

~ 2024-03-01
    (expenses:car:repairs)      150.00 EUR
    (expenses:trips)            400.00 EUR
```

To efficiently use goal-based budgeting as envelope-style budgeting, bare
hledger misses necessary tools, which hledger-budget provides:

- ability to verify how much of available money is not yet budgeted and if
  we're not over-budgeting;
- a way to forecast whether there's still enough money to cover all budgeted
  expenses
- how much money each expenses category has budgeted (hledger aggregates
  budgets of subaccounts in parent accounts).

## Current Budget

`hledger-budget balance` provides a similar table for a current budget as
`hledger --budget`, but with deaggregated budgets for all accounts. It means
that you'll only see money which you explicitly assigned to each "envelope".

hledger-budget makes no assumptions here and shows all accounts for which
budget is defined. You may want to exclude your "spending" account from the
report though, because it affects the total spendings which report presents.
For example, if you track transactions like this:

```ledger
2024-02-01 Groceries
    expenses:groceries          10.00 EUR
    assets:bank:checking       -10.00 EUR
```

you may want to use `hledger-budget balance -e assets:bank:checking`.

## Budget Verification

`hledger-budget check` compares your budgets for each month against the money
available on one or more "spending" accounts. For example, to see the report
for current month, you may use `hledger-budget check -p 'this month' assets:bank:checking`.

The report automatically verifies the validity of your budget:

- whether there's enough of money for all remaining (budgeted) spendings;
- whether you're not over-budgeting.
