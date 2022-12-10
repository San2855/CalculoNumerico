# Essa funçao soma os elementos da linha
def VetorB(A):
  lista = []
  for i in range(len(A)):
      soma = 0
      for j in range(len(A[i])):
            soma += A[i][j]
      lista.append(soma)
  return lista

# Essa funçao faz o escalonamento
def Gauss(A, b):
  n = len(b)
  for k in range(0, n-1):
      for i in range(k+1, n):
          m = A[i][k]/A[k][k]
          for j in range(k, n):
            A[i][j] = A[i][j]-m*A[k][j]
          b[i] = b[i]-m*b[k]
  return A, b

# Essa funçao faz a substituição reversa
def solucao(A, b):
   n = len(b)
   x = n*[0]
   x[n-1] = b[n-1]/A[n-1][n-1]
   for k in range(n-2, -1, -1):
     s = 0
     for j in range(k+1, n):
       s = s + A[k][j]*x[j]
     x[k] = (b[k]-s)/A[k][k]
   return x

# Essa função constroi uma matriz de hilbert com os parametros que você escolher
def hilmat(a, z):
    if a == z:
      return [[1 / (i + j + 1) for j in range(z)] for i in range(a)]
    else:
      print("Essa forma de matriz não é valida")

# Execução do código
a = int(input("insira o número de linhas da sua matriz: "))
z = int(input("insira o número de colunas da sua matriz: "))
A = hilmat(a, z)
b = VetorB(A)
print(Gauss(A, b))
print(20*"-")
print(solucao(A, b))
print(20*"-")

