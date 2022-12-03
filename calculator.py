import numpy as np
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
