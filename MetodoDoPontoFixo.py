import math
def f(x):
  return   math.exp(x) + x
def phi(x):
  return -math.exp(x)
e=0.00001
k=0
x_0 = -1
x= x_0
while math.fabs(f(x))>e:
  k=k + 1
  x= phi(x)
print("a solução encontrada foi", x)
print("A quantidade de interações foi", k)