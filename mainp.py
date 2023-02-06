import numpy as np
import matplotlib.pyplot as plt
import debye_calculator as db
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
janela.geometry('390x220')
# -- Fixando o tamanho da janela
janela.resizable(False,False)

# -- Definindo e posicionando os textos da janela
t1 = Label(janela,text= 'Determine o Material',font='Times 15').place(x=16,y=15)
t2 = Label(janela,text='Escola de Engenharia de Lorena',font='Times 6').place(x=135,y=195)
t3 = Label(janela,text='T Mín:',font='Times 15').place(x=80,y=80)
t4 = Label(janela,text='T Máx:',font='Times 15').place(x=240,y=80)

# -- Definindo e posicionando o botão lista
Combo = ttk.Combobox(janela, values = lista_material)
Combo.place(x=200,y=19)
Combo.set(lista_material[0])

# -- Definindo e posicionando os botões slider
slider1 = Scale(janela, from_=10, to=500, orient=HORIZONTAL)
slider1.place(x=60,y=100)
slider2 = Scale(janela, from_=10, to=500, orient=HORIZONTAL)
slider2.place(x=220,y=100)

# -- Criando a função que irá calcular o calor específico e gerar nosso gráfico
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
        plt.ylabel('Specific heat (J/molK)')
        plt.xlabel('Temperature (K)')
        plt.show()
    else:
        messagebox.showerror(u'Error', u'T. Mín >= T. Máx\nAltere os valores')

# -- Criando o botão quit e plot
b1 = Button(janela,text='Exit',command=janela.destroy,width=8).place(x=220,y=160)
b2 = Button(janela,text='Plot',width=8,command=grafico).place(x=85,y=160)

janela.mainloop()


# -- Caso o material não faça parte do banco de dados
input1 = str(input('Informe o material: '))
input2 = int(input('Informe a temperatura de Debye do material (K): '))

temp_debye = db.Debye(input2)

#Tmin, Tmax, NT = 5, 500, 201
Tmin = int(input('Informe a temperatura mínima (K): '))
Tmax = int(input('Informe a temperatura máxima (K): '))
NT = 201

if Tmin<Tmax:
    T = np.linspace(Tmin,Tmax+1,NT)
else:
    T = np.linspace(Tmax,Tmin,NT)

if Tmin == 0:
    print('Error: x = tetad/0: indeterminação')
else:
    plt.plot(T,temp_debye.SpecificHeat(T))
    plt.title(f'{input1} (Θd: {input2} K)')
    plt.ylabel('Specific heat (J/molK)')
    plt.xlabel('Temperature (K)')
    plt.show()





