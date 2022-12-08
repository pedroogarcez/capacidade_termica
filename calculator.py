import numpy as np
import scipy as sp
import pandas as pd

# -- Criando um dicionário com os valores das tabelas
df = pd.read_csv('debye - Página1.csv')
lista_material = df['material'].tolist()
lista_temperatura = df['temperatura de debye [K]'].tolist()
dicionario = dict(zip(lista_material,lista_temperatura))
# --

# -- Criando uma função que calcula os valores de x de acordo com o material informado e os valores de tmin e tmax
def calcula_x(material,t_min,t_max):
    global dicionario
    r = 8.31451
    t = np.arange(t_min,t_max+1,10)
    tetad = dicionario[material]
    x =  tetad/t
    return x
# --
w = calcula_x('Alumínio',10,500)
print(w)

# -- De acordo com os valores de x calculados, agora vamos calcular os valores da integral













