'''
Descripción del programa: Hacer un programa que muestre un cronómetro,
indicando las horas, minutos y segundos.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import time


##### Declaración de Variables #######
horas = 0
minutos = 0
segundos = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
while True:
    time.sleep(1)
    segundos += 1
    if segundos >= 60:
        minutos += 1
        segundos = 0
    elif minutos >= 60:
        horas += 1
        minutos = 0
    print(f"[{horas}:{minutos}:{segundos}]")
