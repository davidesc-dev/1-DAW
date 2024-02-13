'''
Descripción del programa: 
Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior.


Version: 2.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
UserChoice = 0
CurrentMin = 999999999999999999
Min = 0
CurrentMax = -999999999999999999
Max = 0
lista = []


###### Fuciones y Procedimientos (Subprogramas) ######
def calcularMin():
    global Min, CurrentMin
    for i in range(len(lista)):
        if lista[i] < CurrentMin:
            CurrentMin = lista[i]
    Min = CurrentMin

def calcularMax():
    global Max, CurrentMax
    for i in range(len(lista)):
        if lista[i] > CurrentMax:
            CurrentMax = lista[i]
    Max = CurrentMax


###### Programa Principal #############
for i in range(5):
    UserChoice = int(input(f"Introduzca numero {i+1}/5: "))
    lista.append(UserChoice)
calcularMax()
print("El maximo es:",Max)
calcularMin()
print("El minimo es:",Min)