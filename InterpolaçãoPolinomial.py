
def p(x, a):
  r = 0
  n = len(a)
  for i in range(0, n):
    r += a[i] * (x**i)
    return r


def Gauss(A, b):
  n = len(b)
  for k in range(0, n-1):
    for i in range(k+1, n):
        m = A[i][k]/A[k][k]
        for j in range(k, n):
          A[i][j] = A[i][j]-m*A[k][j]
        b[i] = b[i]-m*b[k]
    return A, b


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


def vandermonde_matrix(x):
    n = len(x)
    V = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(x[i]**j)
        V.append(row)
    return V
  

x = [30, 35, 40]
y = [0.99826, 0.99818, 0.99828]

w = [20, 25, 30, 35, 40, 45, 50]
z = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878]

V = vandermonde_matrix(x)
D = vandermonde_matrix(w)

V_t, y_t = Gauss(V, y)
a = solucao(V_t, y_t)

D_t, z_t = Gauss(D, z)
c = solucao(D_t, z_t)

print("Esse é o valor para um polinomio de grau 2:", p(32.5, a))
print("Esse é o valor para um polinomio de grau 6:", p(32.5, c))

