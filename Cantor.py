import matplotlib.pyplot as plt
import random

def f(x,y):
    f1 = x/3
    f2 = y/3
    return f1, f2
def g(x,y):
    g1 = x/3 + 2/3
    g2 = y/3
    return g1, g2

x, y = 0, 0
pontos_x = []
pontos_y = []

for i in range(1000000):
    r = random.choice([f,g])

    x, y = r(x, y)

    pontos_x.append(x)
    pontos_y.append(y)

plt.scatter(pontos_x,pontos_y, s=0.01)
plt.title("Conjunto de Cantor")
plt.show()