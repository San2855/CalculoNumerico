def hilmat(a, b):
    return [[1 / (i + j + 1) for j in range(b)] for i in range(a)]
print(hilmat(3, 3))