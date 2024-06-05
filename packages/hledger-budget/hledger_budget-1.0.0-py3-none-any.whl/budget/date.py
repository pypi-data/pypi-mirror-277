from datetime import date


def first_of_this_month() -> str:
    return date.today().replace(day=1).isoformat()
