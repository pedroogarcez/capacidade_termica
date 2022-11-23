#Nesse projeto, vamos calcular o calor específico molar de diferentes materiais para o modelo de Debye.
import scipy.integrate
import numpy as np
import tkinter as tk

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


'''
janela = tk.Tk()
janela.title('Capacidade térmica dos materiais')
janela.geometry('400x150')
janela.mainloop()
'''