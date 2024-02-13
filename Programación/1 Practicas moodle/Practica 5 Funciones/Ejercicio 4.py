'''
Descripción del programa: 
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
función en un programa principal que lea el radio de una circunferencia y muestre su área y
perímetro.

Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import math


##### Declaración de Variables #######
radio = 0
area = 0
circunferencia = 0


###### Fuciones y Procedimientos (Subprogramas) ######
def AreaPerimetroCircunferencia():
    area = 2 * math.pi * radio
    circunferencia = math.pi * radio ** 2
    print("El area del circulo es:",area)
    print("La longitud de la circunferencia es:",circunferencia)


###### Programa Principal #############
radio = int(input("Introduzca el radio del circulo: "))
AreaPerimetroCircunferencia()