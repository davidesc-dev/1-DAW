''' Descripción del programa: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
    Recordar que la fórmula para la conversión es: C = (F-32)*5/9


    Version: 1.0
    Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
ftemp = 0
ctemp = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
ftemp = int(input("Introduzca una cantidad en Fahrenheit: "))
ctemp = ((ftemp-32)*5/9)
print ( ftemp ,"ºF son ",ctemp ,"ºC")