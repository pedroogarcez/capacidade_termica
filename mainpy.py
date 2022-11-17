#Nesse projeto, vamos calcular o calor específico molar de diferentes materiais para o modelo de Debye.
import scipy.integrate
import numpy as np

#Implmentando a função de Debye

lista_temperatura = [1,2,3,4,5]
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
print(valor_x)

#for i in range(len(valor_x)):
    #integral, erro = scipy.integrate.quad()

d = lambda u: (u**4 * np.exp(u))/(np.exp(u)*1)**2
integral = scipy.integrate.quad(d,1,5)
print(integral)

