'''
Descripción del programa: Crea una lista e inicializala con 5 cadenas de caracteres leídas
por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra
sus elementos por la pantalla.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lista = []
caracteres = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for i in range(5):
    caracteres = input(f"Introduzca la cadena de caracteres {i+1}/5: ")
    lista.append(caracteres)
listarevertida = lista[:]
listarevertida.reverse()
print(listarevertida)