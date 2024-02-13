'''
Descripción del programa: 
Crear una función que calcule la temperatura media de un día a partir de la temperatura
máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya
pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El
programa pedirá el número de días que se van a introducir.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
days = 0
tMed = 0
userchoice = 0
minimas = []
maximas = []
medias = []


###### Fuciones y Procedimientos (Subprogramas) ######
def GetTemp():
    for i in range(days):
        userchoice = int(input(f"Introduzca la temperatura minima del dia {i+1}: "))
        minimas.append(userchoice)
        userchoice = int(input(f"Introduzca la temperatura maxima del dia {i+1}: "))
        maximas.append(userchoice)

def TempMedia():
    for temp in range(days):
        tMed = (minimas[temp] + maximas[temp]) / 2
        medias.append(tMed)
    print("Minimas:\n", minimas, "\nMaximas:\n",maximas,"\nMedia:\n", medias)


###### Programa Principal #############
days = int(input("Introduzca el numero de dias: "))
GetTemp()
TempMedia()