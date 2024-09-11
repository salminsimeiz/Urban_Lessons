def custom_write(file_name: str, strings: list) -> dict:
    result_ = {}
    nom_str = 0
    for string in strings:
        file = open(file_name, "a", encoding="utf8")
        nom_str += 1
        j = file.tell()
        file.write(string + "\n")
        result_[(nom_str, j)] = string
        file.close()
    return result_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
