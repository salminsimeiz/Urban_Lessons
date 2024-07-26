import time
import psutil

# вводим исходный список
numbers = [int(number) for number in input("Введите числа через пробел ").split()]
begin_time = time.time()
print(f"Numbers = {numbers}")
primes = []
not_primes = []
deviders = []  # вспомогательный список делителей
max_ = max(numbers)
for num in numbers:
    deviders.clear()
    if num == 1:
        continue
    for i in range(2, max_):
        if num % i == 0:
            deviders.append(i)
    if len(deviders) > 1:
        not_primes.append(num)
    else:
        primes.append(num)
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
end_time = time.time()
working_time = end_time - begin_time
print(f"Время работы програмы: {working_time} c.")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
