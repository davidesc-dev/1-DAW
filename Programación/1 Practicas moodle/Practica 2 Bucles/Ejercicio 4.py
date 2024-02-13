'''
Descripción del programa: Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
contador = 0

###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for numero in range (1, 6):
    resultado = numero
    print ("La tabla del", numero)
    for i in range (1, 11):
        contador += 1
        print (numero,"x",contador,"=",resultado)
        resultado += numero
    print()