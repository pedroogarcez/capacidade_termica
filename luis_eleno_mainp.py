import numpy as np
import matplotlib.pyplot as plt
import debye_luis_eleno as db
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# -- Criando um dicionário com os valores das tabelas
df = pd.read_csv('debye - Página1.csv')
lista_material = df['material'].tolist()
lista_temperatura = df['temperatura de debye [K]'].tolist()
dicionario = dict(zip(lista_material,lista_temperatura))
# --


janela = Tk()
# -- Definindo o título da janela
janela.title('Capacidade térmica dos materiais')
# -- Definindo o tamanho da janela

janela.geometry('400x200')
# -- Definindo e posicionando os textos da janela
t1 = Label(janela,text= 'Determine o Material',font='Times 15').place(x=16,y=15)
t2 = Label(janela,text='Θd:',font='Times 15').place(x=160,y=53)
t3 = Label(janela,text='T Mín:',font='Times 15').place(x=80,y=80)
t4 = Label(janela,text='T Máx:',font='Times 15').place(x=240,y=80)

# -- Definindo e posicionando o botão lista
Combo = ttk.Combobox(janela, values = lista_material)
Combo.place(x=200,y=19)
Combo.set(lista_material[0])

# -- Definindo e posicionando o botão slider
slider1 = Scale(janela, from_=10, to=500, orient=HORIZONTAL)
slider1.place(x=60,y=100)
slider2 = Scale(janela, from_=10, to=500, orient=HORIZONTAL)
slider2.place(x=220,y=100)

# -- Criando a função que irá gerar nosso gráfico
def grafico():
    material = Combo.get()
    t_min = slider1.get()
    t_max = slider2.get()
    if t_min<t_max:
        debye_material = db.Debye(dicionario[material])
        T = np.linspace(t_min, t_max, 201)
        w = debye_material.SpecificHeat(T)
        plt.plot(T,debye_material.SpecificHeat(T))
        plt.title(f'{material} (Θd: {dicionario[material]}K)')
        plt.ylabel('cv (J/molK)')

        plt.show()


    else:
        messagebox.showerror(u'Error', u'T. Mín >= T. Máx.\nAltere os valores.')

# -- Criando o botão quit e plot
b1 = Button(janela,text='Exit',command=janela.destroy,width=8).place(x=240,y=160)
b2 = Button(janela,text='Plot',width=8,command=grafico).place(x=90,y=160)
janela.mainloop()



exit()

'''
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

'''