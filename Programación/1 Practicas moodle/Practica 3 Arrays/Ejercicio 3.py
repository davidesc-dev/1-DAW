''' 
Descripción del programa: Hacer un programa que inicialice una lista
de números con valores aleatorios (10 valores), y posterior ordene
los elementos de menor a mayor.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import random


##### Declaración de Variables #######
lista = []
numero = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for i in range(10):
    numero = random.randint(-9999,9999)
    lista.append(numero)
lista.sort()
print(lista)