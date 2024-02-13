'''
Descripción del programa: 
Crear una función recursiva que permita calcular el factorial de un número. Realiza un
programa principal donde se lea un entero y se muestre el resultado del factorial.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
n = 0
fact = 0


###### Fuciones y Procedimientos (Subprogramas) ######
def CalcularFactorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * CalcularFactorial(n - 1)


###### Programa Principal #############
n = int(input("Introduzca un numero a calcular factorizar: "))
CalcularFactorial(n)