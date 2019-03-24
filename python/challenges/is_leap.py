def is_leap(year: int) -> bool:
    is_leap = True

    if year % 4 != 0:
        is_leap = False
        return is_leap

    if year % 100 == 0:
        is_leap = False

    if year % 400 == 0:
        is_leap = True

    return is_leap


if __name__ == "__main__":
    is_leap(1)
