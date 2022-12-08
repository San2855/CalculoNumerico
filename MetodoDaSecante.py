import math
def f(x):
  return math.sin(x) * math.exp(-x)
k=0
x_0 = 3
x_1 = 4
x = 3
e=0.00001
while math.fabs(f(x)) > e:
  k=k + 1
  x= (x_0*f(x_1) - x_1*f(x_0)) / (f(x_1) - f(x_0))
  x_0 = x_1
  x_1 = x
print("a solução encontrada foi", x_1)
print("A quantidade de interações foi",k)