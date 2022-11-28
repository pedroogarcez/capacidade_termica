#Nesse projeto, vamos calcular o calor específico molar de diferentes materiais para o modelo de Debye.
import scipy.integrate
import numpy as np
from tkinter import *

#Implmentando a função de Debye

lista_temperatura = np.arange(0,100,2)
valor_x = []
def calor_especifico(lista_temperatura):
    r = 8.31451
    theta = 1849
    for i in range(len(lista_temperatura)):
        t = lista_temperatura[i]
        x = theta/t
        valor_x.append(x)
    return
calor_especifico(lista_temperatura)
#print(valor_x)

#for i in range(len(valor_x)):
    #integral, erro = scipy.integrate.quad()

d = lambda u: (u**4 * np.exp(u))/(np.exp(u)*1)**2
integral = scipy.integrate.quad(d,1,5)
#print(integral)

<<<<<<< HEAD
janela = Tk()
=======

'''
janela = tk.Tk()
>>>>>>> 739efcf72e8372796df5876362853ef40fa08e0b
janela.title('Capacidade térmica dos materiais')
janela.geometry('400x150')

# -- Texto
t1 = Label(janela,text= 'Informe o Material',font='Times 15').grid(row=0,column=0,padx=5,pady=10)
t2 = Label(janela,text='Θd:',font='Times 15').place(x=125,y=45)
t3 = Label(janela,text='x1:',font='Times 15').place(x=129,y=85)

#Função botão calcular
def retorna_tetad():
    tetad = 1849
    temperatura = np.arange(10, 101, 10)
    r = 8.31451
    material = str(m.get())
    if material == 'Alumínio':
        Label(text='1849K',font='15').grid(row=1,column=1)
        for i in range(len(temperatura)):
            t = temperatura[i]
            x = tetad/t
        Label(text=f'{x}',font='15').place(x=166,y=88)




    else:
        Label(text='Material não encontrado',font='15').grid(row=1, column=1)

# -- Material informado
material = StringVar()
m = Entry(janela, textvariable=material, width=25)
m.place(x=170,y=15)



# -- Botão calcular
Button(text='Cacular',command=retorna_tetad).place(x=330,y=10)

# -- tetad



janela.mainloop()
'''