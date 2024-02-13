'''Descripción del programa: Calcular el perímetro y área de un rectángulo dada su base y su altura.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
base = 0
altura = 0
a_rectangulo = 0
p_rectangulo = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
base = int(input("Introduzca valor de la base en cm: "))        #La variable "base" se define en funcion del numero introducido por el usuario
altura = int(input("Introduzca valor de la altura en cm: "))    #La variable "base" se define en funcion del numero introducido por el usuario
a_rectangulo = (base * altura)                                  #Se calcula el area
p_rectangulo = (base * 2 + altura * 2)                          #Se calcula el perímetro

print ("El rectangulo tendría un area de", a_rectangulo, "cm², y un perímetro de ", p_rectangulo,"cm")  #Se muestra un texto indicando los valores que se han calculado anteriormente