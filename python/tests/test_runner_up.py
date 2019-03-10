from challenges.runner_up import runner_up

def test_runner_up():
    result = runner_up(5, [2, 3, 6, 6, 5])
    expected = 5
    assert result == expected
