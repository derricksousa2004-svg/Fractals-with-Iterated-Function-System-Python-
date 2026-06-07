import matplotlib.pyplot as plt
import random
import math as m

#Funções da Modelagem
def f(x,y):
    f1 = x/3
    f2 = y/3
    return f1, f2
def g(x,y):
    g1 = x/6 - m.sqrt(3) * y/6 + 1/3
    g2 = m.sqrt(3)*x/6 + y/6
    return g1, g2
def h(x,y):
    h1 =x/ 6 + m.sqrt(3) * y/6 + 1/2
    h2 = - m.sqrt(3) * x/6 + y/6 + m.sqrt(3)/6
    return h1,h2
def w(x,y):
    w1 = x/ 3 + 2/3
    w2 = y/3
    return w1,w2

x, y = 0, 0
pontos_x = []
pontos_y = []

for i in range(1000000):
    r = random.choice([f,g,h,w])

    x, y = r(x, y)

    pontos_x.append(x)
    pontos_y.append(y)

plt.scatter(pontos_x,pontos_y, s=0.01)
plt.title("Curva de Koch")
plt.show()