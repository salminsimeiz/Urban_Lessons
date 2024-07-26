# вводим исходный список
my_list = [int(number) for number in input("Введите числа через пробел ").split()]
print(f"my list = {my_list}")
i = 0
while my_list[i] >= 0:

    if my_list[i] == 0:
        i += 1
        continue
    else:
        print(my_list[i])
        i += 1
    if i == len(my_list): break

