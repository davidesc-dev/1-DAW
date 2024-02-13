'''
Descripción del programa: Dado un número de dos
cifras, diseñe un algoritmo que permita obtener
el número invertido. Ejemplo, si se introduce
23 que muestre 32.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
n = 0
p1 = 0
p2 = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
n = int(input("Introduzca un numero de dos cifras: "))
p1 = n % 10
p2 = n // 10

print("El numero ",n," invertido, sería ",p1,p2,sep="")