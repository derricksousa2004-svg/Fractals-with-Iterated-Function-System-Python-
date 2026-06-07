import matplotlib.pyplot as plt
import random

def f(x,y):
    f1 = x / 3
    f2 = y / 3
    return f1, f2
def g(x,y):
    g1 = -y/3 + 1/3
    g2 = x/3
    return g1, g2
def h(x,y):
    h1 = x/3 + 1/3
    h2 = y/3 + 1/3
    return h1,h2
def w(x,y):
    w1 = -y/3 + 2/3
    w2 = x/3
    return w1,w2
def t(x, y):
    t1 = x / 3 + 1/3
    t2 = y/3
    return t1, t2
def p(x, y):
    p1 = y/3 + 1/3
    p2 = -x/3
    return p1, p2
def l(x, y):
    l1 = x/3 + 1/3
    l2 = y/3 - 1/3
    return l1, l2
def m(x, y):
    m1 = y/3 + 2/3
    m2 = -x/3
    return m1, m2
def n(x, y):
    n1 = x/3 + 2/3
    n2 = y/3
    return n1, n2

x, y = 0, 0
pontos_x = []
pontos_y = []

for i in range(1000000):
    r = random.choice([f,g,h,w,t,p,l,m,n])

    x, y = r(x, y)

    pontos_x.append(x)
    pontos_y.append(y)

plt.scatter(pontos_x, pontos_y, s=1)
plt.title("Curva de Peano")
plt.show()