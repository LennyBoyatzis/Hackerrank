from challenges.setshappiness import calc_happiness


def test_sethappiness():
    arr = [1, 2, 3]
    set_a = {1, 7, 9}
    set_b = {2, 3}
    result = calc_happiness(arr, set_a, set_b)
    expected = -1
    assert result == expected


def test_sethappiness_complex():
    arr = list(range(100))
    set_a = set(range(0, 50, 2))
    set_b = set(range(0, 25, 3))
    # result = calc_happiness(arr, set_a, set_b)
    # expected = 16
    pass
