'''
Descripción del programa: Escribir un programa que
imprima todos los números pares entre dos números 
que se le pidan al usuario.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
num1 = 0
num2 = 0
contador = -1


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
num1 = int(input("Introduce un primer número: "))
num2 = int(input("Introduce un segundo número: "))
contador = num1 - 1
print(f"Números pares entre {num1} y {num2}")
for i in range (num1,num2 + 1):
    contador += 1
    if contador % 2 == 0:
        print(contador)