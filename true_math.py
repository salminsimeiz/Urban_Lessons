from math import inf


def divide(first: int, second: int) -> float:
    if second == 0:
        return inf
    else:
        return first / second


if __name__ is "__main__":
    print(divide(15, 0))
