"""task 2"""
from random import sample


def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list[int]:
    """
    Generate a set of unique random numbers for lottery.

    Parameters:
    min (int) - the minimum possible number in the set (not less than 1).
    max (int) - the maximum possible number in the set (not more than 1000).
    quantity (int) - the number of numbers to be selected (a value between min and max).

    Return:
    list: sorted random set of numbers within the specified parameters, and all random numbers in the set are unique.
    """
    try:
        min_number = int(min_number)
        max_number = int(max_number)
        quantity = int(quantity)
    except (TypeError, ValueError) as e:
        print(e)
        return []

    possible_numbers = range(min_number, max_number + 1)
    if (
        min_number < 1
        or max_number > 1000
        or max_number < min_number
        or quantity not in possible_numbers
        or max_number - min_number < quantity - 1
    ):
        return []
    return sorted(sample(possible_numbers, quantity))


lottery_numbers = get_numbers_ticket("1", 100, 10)
print("Ваші лотерейні числа:", lottery_numbers)
