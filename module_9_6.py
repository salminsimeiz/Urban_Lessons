def all_variants(text: str):
    for j in range(len(text)):
        for i in range(len(text)):
            if i + j + 1 <= len(text):
                yield text[i:(i + 1 + j)]


a = all_variants("banana")
for item in a:
    print(item)
