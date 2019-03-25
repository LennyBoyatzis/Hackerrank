from challenges.second_lowest import second_lowest


def test_returns_second_lowest_result():
    students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]]

    result = second_lowest(students)
    expected = 37.21
    assert result == expected

