import numpy as np
import matplotlib.pyplot as plt

# Define os parâmetros do modelo
beta = 0.4
gamma = 0.035
N = 1000
S0 = 990
I0 = 10
R0 = 0

# Define as equações diferenciais do modelo SIR
def derivs(state, t, N, beta, gamma):
    S, I, R = state
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define o intervalo de tempo e as condições iniciais
t_inicial = 0
t_final = 60
dt = 1
t = np.arange(t_inicial, t_final, dt)
y0 = S0, I0, R0

# Usa o método de Runge-Kutta de ordem 2 para integrar as equações diferenciais
ret = np.array([y0])
for i in range(len(t) - 1):
    y = ret[-1]
    k1 = derivs(y, t[i], N, beta, gamma)
    k2 = derivs(y + dt * k1, t[i + 1], N, beta, gamma)
    ret = np.vstack([ret, (y[0] + dt * (k1[0] + k2[0]) / 2, 
                            y[1] + dt * (k1[1] + k2[1]) / 2, 
                            y[2] + dt * (k1[2] + k2[2]) / 2)])

# Plota as curvas S(t), I(t) e R(t) em um mesmo gráfico
fig = plt.figure(figsize=(10,5))
plt.plot(t, ret[:,0], 'b', label='Suscetíveis')
plt.plot(t, ret[:,1], 'r', label='Infectados')
plt.plot(t, ret[:,2], 'g', label='Recuperados')
plt.xlabel('Tempo (dias)')
plt.ylabel('Número de indivíduos')
plt.ylim(0, N)
plt.title('Modelo SIR')
plt.legend(loc='best')
plt.grid()
plt.show()
