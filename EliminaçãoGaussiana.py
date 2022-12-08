def Gauss(A, b):
  n= len(b)
  for k in range(0, n-1):
    for i in range(k+1, n):
        m= A[i][k]/A[k][k]
        for j in range(k,n):
          A[i][j]= A[i][j]-m*A[k][j]
        b[i]= b[i]-m*b[k]
    return A, b

def solucao(A,b):
  n= len(b)
  x= n*[0]
  x[n-1] = b[n-1]/A[n-1][n-1]
  for k in range(n-2, -1, -1):
    s = 0
    for j in range(k+1,n):
      s= s+ A[k][j]*x[j]
    x[k]= (b[k]-s)/A[k][k]  
  return x 
    
A= [[3,2,4],[1,1,2],[4,3,-2]]
b= [1,2,3]
A_t, b_t = Gauss(A,b)
print(Gauss(A,b))
print(solucao(A_t,b_t))