import numpy as np
<<<<<<< HEAD
import scipy as sp

# -- Criando uma função que calcula os valores de x de acordo com o material informado e os valores de tmin e tmax
def x_calculator(tetad,t_min,t_max):
    l_temp = np.arange(t_min,t_max,10)
    x = tetad/l_temp
    return x
x = x_calculator(1849,10,500)
#print(x[0])

=======
import pandas as pd
import scipy

df = pd.read_csv('debye - Página1.csv')
lista_material = df['material'].tolist()
lista_temperatura = df['temperatura de debye [K]'].tolist()
dicionario = dict(zip(lista_material,lista_temperatura))

def calcula_x(material,t_min,t_max):
    global dicionario
    r = 8.31451
    t = np.arange(t_min,t_max+1,10)
    tetad = dicionario[material]
    x =  tetad/t
    return x
'''
material = str(input('Informe o material'))
t_min = int(input('Informe o valor da temperatura mínima'))
t_max = int(input('Informe o valor da temperatura máxima'))
'''

x = calcula_x('Alumínio',10,500)
print(x[0])
>>>>>>> f938728d4df10a1e2c3ffd61ed904c6dfecb6b2d
