'''
Descripción del programa: 
Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior.


Version: 1.0
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
def calcularMaxMin():
    global Min, CurrentMin, Max, CurrentMax
    for i in range(len(lista)):
        if lista[i] < CurrentMin:
            CurrentMin = lista[i]
        if lista[i] > CurrentMax:
            CurrentMax = lista[i]
    Min = CurrentMin
    Max = CurrentMax


###### Programa Principal #############
for i in range(5):
    UserChoice = int(input(f"Introduzca numero {i+1}/5: "))
    lista.append(UserChoice)

calcularMaxMin()
print(lista)
print("El maximo es:",Max)
print("El minimo es:",Min)