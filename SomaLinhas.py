
def VetorB(A):
  lista=[]
  for i in range(len(A)):
        soma = 0
        for j in range(len(A[i])):
            soma += A[i][j]
        lista.append(soma)
  print(lista)
  return lista

def hilmat(a, z):
    return [[1 / (i + j + 1) for j in range(z)] for i in range(a)]

A= hilmat(3,3)
VetorB(A)