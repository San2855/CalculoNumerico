import math
def f(x):
  return  math.sin(x) * math.exp(-x)
def derivada(x):
  return math.cos(x) * math.exp(-x) - math.sin(x) * math.exp(-x)
k=0
Ci = 3.1
x= Ci
e=0.00001
while math.fabs(f(x)) > e:
  k=k + 1
  x= x - (f(x) / derivada(x))
print("a solução encontrada foi", x)
print("A quantidade de interações foi", k)