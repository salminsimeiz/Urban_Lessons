calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> ():
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: ["", "", ""]) -> True | False:
    count_calls()
    new_list = []
    for element in list_to_search:
        new_list.append(element.lower())
    if string.lower() in new_list:
        return True
    else:
        return False


print(string_info("BaLaBon"))
print(string_info("DURLex"))
print(is_contains("MaloPomalu", ["Honolulu", "TOMATO", "malopomalu"]))
print(is_contains("Hamster", ["ham", "HaMsTeR", "hamOn"]))
print(is_contains("bella", ["chao", "Shalom", "Hi"]))
print(calls)
