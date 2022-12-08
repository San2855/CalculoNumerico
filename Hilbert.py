import math
a = int(input("Insira o número de linhas"))
b = int(input("Insira o número de colunas"))

def hilmat(a,b):
    li=[[0]]*a
    for i in range(a):
        for j in range(b):
            ele=math.pow((i+j+1),-1)
            li[i].append(ele)
    return li


print(hilmat(a,b))