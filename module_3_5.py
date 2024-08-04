def get_multiplied_digit(number:int):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digit(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digit(40203))
print(get_multiplied_digit(4))

# вывод:
# C:\Users\-\PycharmProjects\learning24\.venv\Scripts\python.exe C:\Users\-\PycharmProjects\learning24\module_3_5.py
# 24
# 4
#
# Process finished with exit code 0