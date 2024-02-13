'''
Descripción del programa: Escribe un programa que dados dos
números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede
utilizar el operador de potencia.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
base = 0
exponente = 0
resultado = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
base = int(input("Introduzca el numero base a usar: "))
resultado = base
exponente = int(input("Introduzca el exponente: "))
for i in range (exponente-1):
    resultado *= base

print(f"{base}^{exponente} = {resultado}")