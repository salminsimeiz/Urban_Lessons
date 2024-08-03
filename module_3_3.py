def print_params(a=1, b="hola", c=True):
    print(a, b, c)


values_list = [56, "prego", ["s", "w", "o", "r", "d"]]
values_dict = {"a": 1, "b": "stop", "c": False}
values_list_2 = [(4.2,), (2, 3, 4)]

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 5)
