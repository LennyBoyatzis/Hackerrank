"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""


def py_printer(n: int) -> None:
    is_even = n % 2 == 0

    if not is_even:
        print("Weird")
        return "Weird"
    elif is_even and n in range(2, 6):
        print("Not Weird")
        return "Not Weird"
    elif is_even and n in range(6, 21):
        print("Weird")
        return "Weird"
    elif is_even and n > 21:
        print("Not Weird")
        return "Not Weird"


if __name__ == "__main__":
    py_printer(1)
