my_string = input("Input any word: ")
my_list = list(my_string)
# создаем словарь:
my_dict = {}
for i in my_list:
    my_dict.setdefault(i, 0)
    my_dict[i] += 1
a = my_dict["r"]  # значение для ключа "r"
b = my_dict.get("z")   # значение для ключа "z"
my_dict0 = my_dict.copy()
my_dict0.update({"j": 5, "o": 7})  # добавляем элементы в словарь
my_dict1 = my_dict0.copy()
c = my_dict1.pop("a")   # вытаскиваем значение для ключа "а"
print(f"Dict: {my_dict}\nExisting value: {a}\nNot existing value: {b}\nUpdated dict: {my_dict0}")
print(f"Deleted value: {c}\nModified dict: {my_dict1} ")

# создаем множество
my_set = set(my_list)
print(my_set)
my_set.add((1,))
my_set.add("oxigen")
my_set.discard("d")
print(my_set)


