import scipy.integrate
import numpy as np
from tkinter import *
import pandas as pd
from tkinter import ttk


# -- Criando a base de dados com dicionário
df = pd.read_csv('debye - Página1.csv')
lista_material = df['material'].tolist()
lista_temperatura = df['temperatura de debye [K]'].tolist()
dicionario = dict(zip(lista_material,lista_temperatura))
# --

# -- Configurando a janela
janela = Tk()
janela.title('Capacidade térmica dos materiais')
janela.geometry('380x240')
# --

# -- Criadno os textos
t1 = Label(janela,text= 'Informe o Material',font='Times 15').place(x=30,y=20)
t2 = Label(janela,text='Θd:',font='Times 15').place(x=129,y=65)
t3 = Label(janela,text='TMÍN:',font='Times 15').place(x=60,y=100)
t4 = Label(janela,text='TMÁX:',font='Times 15').place(x=240,y=100)
# --

# -- Criando as caixas de entrada

combo = ttk.Combobox(values=lista_material,textvariable=StringVar())
combo.place(x=190,y=23)
mat_informado = combo.get()


# -- Criandoo a função que calcula a integral a partir do material informado no "combobox"


# --


# -- Criando o botão slider para Temp Mín
slide1 = Scale(janela,from_=10,to=500,orient=HORIZONTAL)
slide1.place(x=40,y=125)
t_min = slide1.get

# -- Criando o botão slider para Temp Máx.
slide2 = Scale(janela,from_=10,to=500,orient=HORIZONTAL)
slide2.place(x=220,y=125)
t_max = slide2.get()


# -- Criando uma função que calcula os valores de x de acordo com o material informado e os valores de tmin e tmax











# -- Criando o botão
Button(text='Limpar',width=10).place(x=25,y=190)
Button(text='Gerar gráfico',width=10).place(x=145,y=190)
Button(text='Sair',width=10,command=janela.destroy).place(x=270,y=190)
# --

# --
janela.mainloop()