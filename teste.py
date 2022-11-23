import scipy.integrate
import numpy as np
x_calculado = []
def calcula_x(teta):
    t = np.arange(1,20,4)
    for i in range(len(t)):
        x = teta/t[i]
        #print(x)
        d = lambda u: ((u ** 4 * np.exp(u)) / (np.exp(u) * 1) ** 2)*9/x**3
        integral = scipy.integrate.quad(d, 10, x)
        print(integral)
    return
diamante = 1841

calcula_x(diamante)

