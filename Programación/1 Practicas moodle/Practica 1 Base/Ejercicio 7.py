''' 
Descripción del programa: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
minutos = 0
horas = 0
minutos_restantes = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60

# Mostrar el resultado por pantalla
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")