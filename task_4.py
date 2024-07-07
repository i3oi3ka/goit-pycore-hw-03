"""task 4"""

from datetime import datetime, timedelta


def convert_str_to_date(date: str) -> datetime.date:
    """
    Convert date string to date object.

    Args:
        date (str): The date string in the format "%Y.%m.%d".

    Returns:
        datetime.date: The corresponding date object.

    Throws:
        ValueError: When the date format is not "%Y.%m.%d".
    """
    return datetime.strptime(date, "%Y.%m.%d").date()


def get_upcoming_birthdays(users_birthday: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Get a list of users with upcoming birthdays within the next 7 days.

    Args:
        users (list[dict[str, str]]): List of users with 'name' and 'birthday'.

    Returns:
        list[dict[str, str]]: List of users with upcoming birthdays, including the congratulation date.
    """
    users_upcoming_birthday = []
    today = datetime.today().date()

    for user in users_birthday:
        try:
            birthday_date = convert_str_to_date(user["birthday"])
        except ValueError:
            continue  # Skip users with invalid date format

        # Set the birthday to the current year
        birthday_this_year = birthday_date.replace(year=today.year)

        # If the birthday this year has already passed, set it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days
        if (birthday_this_year - today).days <= 7:
            # Adjust the birthday to avoid weekends
            while birthday_this_year.weekday() in [5, 6]:
                birthday_this_year += timedelta(days=1)

            users_upcoming_birthday.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return users_upcoming_birthday


# Sample data
users = [
    {"name": "John Doe", "birthday": "1985.07.12"},
    {"name": "Jane Smith", "birthday": "1990.07.07"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
