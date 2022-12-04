import numpy as np
import scipy as sp

# -- Criando uma função que calcula os valores de x de acordo com o material informado e os valores de tmin e tmax
def x_calculator(tetad,t_min,t_max):
    l_temp = np.arange(t_min,t_max,10)
    x = tetad/l_temp
    return x
x = x_calculator(1849,10,500)
#print(x[0])

