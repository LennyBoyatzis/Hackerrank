from typing import List
import ipdb


def runner_up(n: int, arr: List) -> int:
    sorted_set = sorted(arr, reverse=True)

    sorted_set.remove(arr_max)
    return sorted_set.pop()


if __name__ == "__main__":
    result = runner_up(5, [2, 3, 6, 6, 5])
    print(f"result {result}")
