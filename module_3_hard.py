def calculate_structure_sum(el):
    global s
    if isinstance(el, (list, tuple, set)):
        for sub_el in el:
            calculate_structure_sum(sub_el)
    elif isinstance(el, str):
        s += len(el)
    elif isinstance(el, dict):
        for keys, volumes in el.items():
            s += (len(keys) + volumes)
    elif isinstance(el, (int, float)):
        s += el
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

s = 0
result = calculate_structure_sum(data_structure)
print(result)
