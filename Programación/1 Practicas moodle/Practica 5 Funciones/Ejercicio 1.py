'''
Descripción del programa: 
Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
primero es múltiplo del segundo.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
x = 0
y = 0


###### Fuciones y Procedimientos (Subprogramas) ######
def EsMultiplo (x,y):
    if y % x == 0:
        print(f"{x} es multiplo de {y}")
    else:
        print(f"{x} NO es multiplo de {y}")


###### Programa Principal #############
x = int(input("Introduzca un primer valor: "))
y = int(input("Introduzca un segundo valor: "))
EsMultiplo(x,y)