'''
Descripción del programa: Programa que declare una lista y la vaya llenando de números hasta
que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos 
introducidos).


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lista = []
number = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
number = int(input("Introduzca un primer numero para introducir a la lista y un negativo para terminar: "))
while 0 < number:
    lista.append(number)
    number = int(input("Introduzca un numero para introducir a la lista y un negativo para terminar: "))
print(lista)