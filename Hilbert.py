def hilmat(a, z):
    return [[1 / (i + j + 1) for j in range(z)] for i in range(a)]