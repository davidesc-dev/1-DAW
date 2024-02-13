''' Descripción del programa: Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
    Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?


    Version: 1.0
    Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
num = 0
r2 = 0
r3 = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
num = int(input("Introduce un número: "))
r2 = num ** (1/2)
r3 = num ** (1/3)

print("La raiz cuadrada de",num,"es",r2,",y su raiz cúbica es",r3)