import time
import psutil

# формируем исходный список
numbers = [number for number in range(1, 16)]
begin_time = time.time()
print(f"Numbers = {numbers}")
primes = []
not_primes = []
dev = []  # вспомогательный список делителей
max_ = max(numbers)
for num in numbers:
    dev.clear()
    if num == 1:
        continue
    for i in range(2, max_):
        if num % i == 0:
            dev.append(i)
    if len(dev) > 1:
        not_primes.append(num)
    else:
        primes.append(num)
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
end_time = time.time()
working_time = end_time - begin_time
print(f"Время работы програмы: {working_time} c.")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
