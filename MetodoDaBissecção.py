import math
def f(x):
  return  math.sin(x) * math.exp(-x)

#intervalo inicial
a= 3
b= 4

#iterações
k=0

#precisão
erro= 0.0001

while((b-a)>erro):
  M= (a+b)/2
  if f(a)*f(M)<0:
    b=M
  else:
    a=M
  k=k+1 

print("A solução encontrada foi", M)   
print("Número de iterações", k)