''' 
Descripción del programa: Algoritmo que pida caracteres e imprima 'VOCAL' si son
vocales y 'NO VOCAL' en caso contrario, el programa termina cuando se introduce
un espacio.


Version: 2.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
caracter = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
caracter = input("Introduzca un caracter o un espacio para salir: ")
while caracter != " ":
    if caracter in "aeiouAEIOU":
        print("VOCAL")
    else:
        print("NO VOCAL")
    caracter = input("Introduzca otro caracter o un espacio para salir: ")