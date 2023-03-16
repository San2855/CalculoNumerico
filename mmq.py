import math  # Importa a biblioteca math para acessar funções matemáticas comuns
# Importa a biblioteca matplotlib.pyplot para gerar visualizações gráficas dos dados
import matplotlib.pyplot as plt
# Importa a biblioteca numpy para trabalhar com matrizes e vetores de forma eficiente
import numpy as np


def mmq(g_1, g_2, x, y):
    # Define a função de ajuste que calcula os coeficientes a1 e a2 de uma função não-linear para um conjunto de dados
    # Recebe como argumentos duas funções de base g_1 e g_2, e dois vetores x e y com os valores de entrada e saída, respectivamente

    a_1 = 0  # Inicializa os coeficientes a1 e a2 com zero
    a_2 = 0

    # Calcula as quatro somas necessárias para a matriz G
    G_11 = np.dot(g_1(x), g_1(x))
    G_12 = np.dot(g_1(x), g_2(x))
    G_21 = np.dot(g_2(x), g_1(x))
    G_22 = np.dot(g_2(x), g_2(x))

    # Cria a matriz G
    G = [[G_11, G_12], [G_21, G_22]]

    # Calcula os vetores b1 e b2
    b_1 = np.dot(y, g_1(x))
    b_2 = np.dot(y, g_2(x))

    # Cria o vetor b
    b = [b_1, b_2]

    # Resolve o sistema linear G*a = b e armazena os coeficientes a1 e a2
    a = np.linalg.solve(G, b)
    a_1 = a[0]
    a_2 = a[1]

    return a_1, a_2  # Retorna os coeficientes a1 e a2


# Define as funções de base g_1, g_2 e g_3 à serem ajustadas:
def g_1(r):
    # Retorna um vetor de comprimento len(r) com todos os valores iguais a 1
    return np.ones(len(r))


def g_2(r):
    return np.sqrt(r)  # Retorna o vetor com a raiz quadrada dos elementos de r


def g_3(t):
    # Retorna o vetor com o logaritmo natural dos elementos de t
    return np.log(t)


# Considera o conjunto de dados:
x = np.array([1, 1.5, 2, 2.5, 3])  # Define os valores de entrada x
y = np.array([1.6, 5.6, 6, 7.1, 7])  # Define os valores de saída y

# Calcula os coeficientes de ajuste para as funções de base g_1 e g_2
a_1, a_2 = mmq(g_1, g_2, x, y)

# Calcula os coeficientes de ajuste para as funções de base g_1 e g_3
a_3, a_4 = mmq(g_1, g_3, x, y)

# Define as funções de ajuste phi e phi2


def phi(z):
    return a_1 + a_2 * g_2(z)


def phi2(z):
    return a_3 + a_4*g_3(z)


# Gerando 100 valores igualmente espaçados no intervalo [1, 3]
# que serão utilizados como entrada para as funções de ajuste
x_r = np.linspace(1, 3, 100)
x_t = np.linspace(1, 3, 100)

# Aplicando as funções de ajuste aos valores gerados acima
# para obter os valores da curva de ajuste correspondente
y_r = phi(x_r)
y_t = phi2(x_t)

# Plotando os pontos do conjunto de dados e as curvas de ajuste
# A opção 'o' indica que os pontos devem ser plotados como círculos
plt.plot(x, y, 'o')

# Plotando a curva de ajuste correspondente a phi(x)
# A opção label define o texto que aparecerá na legenda da figura
plt.plot(x_r, y_r, label='Sqrt(x)')

# Plotando a curva de ajuste correspondente a phi2(x)
# A opção label define o texto que aparecerá na legenda da figura
plt.plot(x_t, y_t, label='ln(x)')

# Adicionando uma legenda à figura
plt.legend()

# Mostrando a figura
plt.show()

# Calcula o erro referente a função sqrt(x)
erro = 0
for i in range(len(x)):
  erro += (y[i] - phi(x[i]))**2
print("O erro em sqrt(x) foi:", erro)

# Calcula o erro referente a função ln(x)
erro2 = 0
for i in range(len(x)):
  erro2 += (y[i] - phi2(x[i]))**2
print("O erro em ln(x) foi:", erro2)