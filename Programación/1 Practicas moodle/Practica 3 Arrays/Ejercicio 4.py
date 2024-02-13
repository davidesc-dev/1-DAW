'''
Descripción del programa: Realizar un programa que inicialice una
lista con 10 valores aleatorios (del 1 al 10) y posteriormente
muestre en pantalla cada elemento de la lista junto con su cuadrado
y su cubo.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import random


##### Declaración de Variables #######
lista = []
cuadrados = []
cubos = []


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
    #Generacion de la lista
for i in range(10):
    lista.append(random.randint(1,10))
print(lista)

    #Bucle cuadrados
for i in range(10):
    cuadrados.append(lista[i]*(1/2))
print(cuadrados)

    #Bucle cubos
for i in range(10):
    cubos.append(lista[i]*(1/3))
print(cubos)