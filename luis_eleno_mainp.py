import numpy as np
import matplotlib.pyplot as plt
import debye_luis_eleno as db
import pandas as pd
from tkinter import *

janela = Tk()
# -- Definindo o título da janela
janela.title('Capacidade térmica dos materiais')
# -- Definindo o tamanho da janela
janela.geometry('400x190')
# -- Definindo e posicionando os textos da janela
t1 = Label(janela,text= 'Determine o Material',font='Times 15').place(x=16,y=15)
t2 = Label(janela,text='Θd:',font='Times 15').place(x=125,y=50)
t3 = Label(janela,text='T Mín:',font='Times 15').place(x=16,y=80)
t3 = Label(janela,text='T Máx:',font='Times 15').place(x=36,y=125)


# -- Definindo e posicionando os botões


janela.mainloop()
exit()
# -- Criando um dicionário com os valores das tabelas
df = pd.read_csv('debye - Página1.csv')
lista_material = df['material'].tolist()
lista_temperatura = df['temperatura de debye [K]'].tolist()
dicionario = dict(zip(lista_material,lista_temperatura))
# --

material_informado = str(input('Informe o material'))
debye_material = db.Debye(dicionario[material_informado])

#Tmin, Tmax, NT = 5, 500, 201
Tmin = int(input('Informe a temperatura mínima'))
Tmax = int(input('Informe a temperatura máxima'))
NT = 201
T = np.linspace(Tmin,Tmax,NT)

plt.plot(T,debye_material.SpecificHeat(T))
plt.title(f'{material_informado}')
plt.show()

