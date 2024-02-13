'''
Descripción del programa: 
Crear una función que calcule el MCD de dos número por el método de Euclides. El método
de Euclides es el siguiente:
    ● Se divide el número mayor entre el menor.
    ● Si la división es exacta, el divisor es el MCD.
    ● Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa
      de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
mcd = 0


###### Fuciones y Procedimientos (Subprogramas) ######
def MCD(n1,n2):
  div = 0
  mcd = 0
  if n1 > n2:
    div = n1/n2
    if div == 0:
      mcd = div
    elif div != 0:
      while n1 / n2 != 0:
        div /= (%)      
  else:
    div = n1/n2
    if div == 0:
      mcd = div


###### Programa Principal #############
num1 = int(input("Introduzca número 1 a sacar MCD: "))
num2 = int(input("Introduzca número 2 a sacar MCD: "))
MCD(num1,num2)