from challenges.is_leap import is_leap


def test_is_leap_if_evenly_divided_by_4():
    result = is_leap(2004)
    expected = True
    assert result == expected


def test_is_leap_if_divisible_by_100_and_not_400():
    result = is_leap(2300)
    expected = False
    assert result == expected


def test_is_leap_if_divisible_by_400():
    result = is_leap(2400)
    expected = True
    assert result == expected
