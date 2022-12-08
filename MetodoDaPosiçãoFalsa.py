import math
def f(x):
 return  math.sin(x) * math.exp(-x)
a=3
b=4
e=0.00001
k=0
M=(a + b)/2
if f(a)*f(b)<0:
  while math.fabs(f(M))>e:
    M=(a*f(b) - b*f(a))/(f(b) - f(a))
    k=k + 1
    if f(a)*f(M)<0:
      b=M
else:
  a=M
print("a solução encontrada foi", M)
print("A quantidade de interações foi", k)