''' Descripción del programa: Pide al usuario dos números y muestra la "distancia" entre ellos
    (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
num1 = 0
num2 = 0
diferencia = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
num1 = int(input("Introduce un primer número: "))
num2 = int(input("Introduce un segundo número: "))
diferencia = abs(num1 - num2)

print("La diferencia entre",num1,"y",num2,"es:",diferencia)