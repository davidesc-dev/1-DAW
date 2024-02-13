'''
Descripción del programa: Escribe un programa que diga
si un número introducido por teclado es o no primo. Un
número primo es aquel que sólo es divisible entre él
mismo y la unidad. Nota: Es suficiente probar hasta la
raíz cuadrada del número para ver si es divisible por
algún otro número.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
es_primo = True

###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
numero = int(input("Introduzca un numero o 0 para salir: "))
while numero != 0:
    es_primo = True
    for cont in range(2, numero):
        if numero % cont == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El número {numero} SI es primo")
    else:
        print(f"El número {numero} NO es primo")
    numero = int(input("Introduzca un numero o 0 para salir: "))