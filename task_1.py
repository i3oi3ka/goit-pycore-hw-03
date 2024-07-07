from datetime import datetime


def convert_str_to_date(date: str) -> datetime.date:
    """
    convert date string to data object

    Throws:
        ValueError - when date format is not %Y-%m-%d

    """
    return datetime.strptime(date, "%Y-%m-%d").date()


def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days from today to a given date.

    Parameters:
    date (str): The date in string format to calculate the difference from today.
                The expected format should be compatible with the convert_str_to_date function (%Y-%m-%d).
                Example - '2020-10-09'

    Returns:
    int: The number of days between today and the provided date. If the provided date is in the future,
         the returned number will be negative.
    """
    try:
        date = convert_str_to_date(date)
    except ValueError as e:
        return e
    today = datetime.today().date()
    return (today - date).days


print(get_days_from_today("2024-07-10"))
print(get_days_from_today("20-07-06"))
