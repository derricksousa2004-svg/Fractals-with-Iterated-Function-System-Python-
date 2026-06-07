import matplotlib.pyplot as plt
import random

def f(x, y):
    f1 = x / 3
    f2 = y / 3
    return f1, f2

def g(x, y):
    g1 = x / 3
    g2 = y / 3 + 1 / 3
    return g1, g2

def h(x, y):
    h1 = x / 3
    h2 = y / 3 + 2 / 3
    return h1, h2

def w(x, y):
    w1 = x / 3 + 1 / 3
    w2 = y / 3
    return w1, w2

def j(x, y):
    j1 = x / 3 + 1 / 3
    j2 = y / 3 + 2 / 3
    return j1, j2

def k(x, y):
    k1 = x / 3 + 2 / 3
    k2 = y / 3
    return k1, k2

def t(x, y):
    t1 = x / 3 + 2 / 3
    t2 = y / 3 + 1 / 3
    return t1, t2

def u(x, y):
    u1 = x / 3 + 2 / 3
    u2 = y / 3 + 2 / 3
    return u1, u2

x, y = 0, 0
pontos_x = []
pontos_y = []

for i in range(10000000):
    r = random.choice([f, g, h, w, j, k, t, u])

    x, y = r(x, y)

    pontos_x.append(x)
    pontos_y.append(y)

plt.scatter(pontos_x, pontos_y, s=1)
plt.title("Tapete de Sierpinski")
plt.show()