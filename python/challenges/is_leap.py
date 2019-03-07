def is_leap(year: int) -> bool:
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if divisible_by_4 and not divisible_by_100 or divisible_by_400:
        return True
    return False
