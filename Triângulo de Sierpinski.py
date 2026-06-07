import matplotlib.pyplot as plt
import random

def f(x,y):
    f1 = x/2
    f2 = y/2
    return f1, f2
def g(x,y):
    g1 = x/2 + 1
    g2 = y/2
    return g1, g2
def h(x,y):
    h1 = x/2 + 1/2
    h2 = y/2 + 1
    return h1, h2

x, y = 0, 0
pontos_x = []
pontos_y = []

for i in range(100000):
    r = random.choice([f,g,h])

    x, y = r(x, y)

    pontos_x.append(x)
    pontos_y.append(y)

plt.scatter(pontos_x,pontos_y, s=1)
plt.title("Triângulo de Sierpinski")
plt.show()