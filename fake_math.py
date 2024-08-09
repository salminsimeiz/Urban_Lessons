def divide(first: int, second: int) -> float:
    if second == 0:
        return "Mistake"
    else:
        return first / second


if __name__ == "__main__":
    print(divide(3, 1))
