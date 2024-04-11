# graficar una funcion cuadratica

import matplotlib.pyplot as plt
def cuadratica(a, b, c):
    x = range(-10, 11)
    y = [a*i**2 + b*i + c for i in x]
    return x, y

x, y = cuadratica(1, 2, -1)

plt.plot(x, y)

plt.show()

# funcion(1, 2, 3, 4)

# # def funcion(x, a,b,c):
