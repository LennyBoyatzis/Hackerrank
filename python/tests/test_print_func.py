from challenges.print_func import print_string


def test_simple_case():
    result = print_string(3)
    expected = "123"
    assert result == expected


def test_bigger_case():
    result = print_string(10)
    expected = "12345678910"
    assert result == expected
