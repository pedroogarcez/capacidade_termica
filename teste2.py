#Nesse projeto, vamos calcular o calor específico molar de diferentes materiais para o modelo de Debye.
import scipy.integrate
import numpy as np
from tkinter import *
import debye_calculator as db


d = lambda u: (u**4 * np.exp(u))/(np.exp(u)*1)**2
integral = scipy.integrate.quad(d,1,5)

x
janela = Tk()

janela.title('Capacidade térmica dos materiais')

janela.geometry('400x190')

# -- Texto
t1 = Label(janela,text= 'Informe o Material',font='Times 15').grid(row=0,column=0,padx=5,pady=10)
t2 = Label(janela,text='Θd:',font='Times 15').place(x=125,y=40)
t3 = Label(janela,text='x1:',font='Times 15').place(x=129,y=65)
t4 = Label(janela,text='xn:',font='Times 15').place(x=230,y=65)
t5 = Label(janela,text='Função de Debye:',font='Times 15').place(x=11,y=90)
t6 = Label(janela,text='Calor específico:',font='Times 15').place(x=16,y=115)


#Função botão calcular
def retorna_tetad():
    temperatura = np.arange(10, 501, 10)
    r = 8.31451
    lista_x = []
    lista_integral = []

    material = str(m.get())
    if material == 'Alumínio':
        tetad = 1849
        Label(text='1849K',font='15').place(x=166,y=42)
        for i in range(len(temperatura)):
            t = temperatura[i]
            x = tetad/t

        Label(text=f'{x}',font='15').place(x=166,y=88)
        lista_x.append(x)
        Label(text=f'{lista_x[0]}',font='15').place(x=166,y=68)
        Label(text=f'{lista_x[-1]}', font='15').place(x=267, y=68)
        d = lambda u: ((u ** 4 * np.exp(u)) / (np.exp(u) * 1) ** 2)*(9/x**3)
        integral = scipy.integrate.quad(d, 1, x)
        lista_integral.append(integral[0])
        Label(text=f'{(lista_integral[0])}', font='15').place(x=166, y=94)
    else:
        Label(text='Material não encontrado',font='15').place(x=166,y=43)
        Label(text='--', font='15').place(x=166, y=68)
        Label(text='--', font='15').place(x=267, y=68)
        Label(text='--', font='15').place(x=166, y=94)



# -- Material informado
m = Entry(janela, textvariable=StringVar(), width=25)
m.place(x=170,y=15)



# -- Botão calcular

Button(text='Cacular',command=retorna_tetad).place(x=330,y=10)
Button(text='Calcular',command=retorna_tetad).place(x=330,y=10)
Button(text='Gráfico').place(x=170,y=150)



janela.mainloop()
