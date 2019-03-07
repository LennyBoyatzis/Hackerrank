from challenges.if_else import py_printer


def test_weird_cases():
    odd_result = py_printer(3)
    even_and_in_range = py_printer(20)

    expected = "Weird"
    assert odd_result == expected
    assert even_and_in_range == expected


def test_not_weird_cases():
    even_and_in_range = py_printer(4)
    even_and_greater_than = py_printer(30)

    expected = "Not Weird"
    assert even_and_in_range == expected
    assert even_and_greater_than == expected
