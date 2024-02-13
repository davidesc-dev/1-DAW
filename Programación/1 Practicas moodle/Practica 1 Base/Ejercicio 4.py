'''Descripción del programa: Calcular la media de tres números pedidos por teclado.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
num1 = 0
num2 = 0
num3 = 0
media = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))
media = ((num1+num2+num3)/3)

print("La media de los numeros",num1,",",num2,"y",num3,", es:", media)