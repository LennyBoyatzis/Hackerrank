from typing import List, Set


def calc_happiness(arr: List, set_a: Set, set_b: Set) -> int:
    return sum([1 if i in set_a else -1 if i in set_b else 0 for i in arr])

if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    print(f"running n: {n} and m: {m}")
