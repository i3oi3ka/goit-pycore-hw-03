"""task 3"""

import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to the format +380XXXXXXXXX.

    This function removes all non-digit characters from the input phone number
    and then normalizes it to start with the country code +380.
    If the number of digits is less than 9 returns "".
    Parameters:
    phone_number (str): The input phone number as a string.

    Returns:
    str: The normalized phone number in the format +380XXXXXXXXX.
    """
    phone_number = re.sub(r"\D", "", str(phone_number))
    if len(phone_number) < 9:
        return ""

    normalize_phone_number = re.sub(
        r"^(380|80|0)?(\d{9})(\d*)$", "+380" + r"\2", phone_number
    )
    return normalize_phone_number


raw_numbers = [
    "067\\t123 45678",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "50 111 22 11   ",
    6795551742511,
    "////////////////////////",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
