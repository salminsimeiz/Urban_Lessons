def get_matrix(n: int, m: int, volume: int) -> list:
    if n <= 0 or m <= 0 or volume <= 0:
     matrix = []
    else:
        matrix = []
        el = []
        for i in range(n):
            matrix.append(el)
        for j in range(m):
            el.append(volume)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
