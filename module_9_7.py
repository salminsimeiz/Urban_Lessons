def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for n in range(2, res):
            if res % n == 0:
                print(f"{res} - составное число")
                break
        else:
            print(f"{res} - простое число")
        return res
    return wrapper


@is_prime
def sum_three(*args):
    result_ = sum(args)
    return result_


result = sum_three(1, 93, 63)
print(result)
