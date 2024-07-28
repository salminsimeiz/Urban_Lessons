passes = []
for i in range(3, 21):
    passes.clear()
    for j in range(i):
        for k in range(1, j):
            if i % (j + k) == 0 and j + k != 1 and j != k:
                passes.append(k)
                passes.append(j)
    print(f"Числу {i} соответствует следующий набор паролей:", *passes)
