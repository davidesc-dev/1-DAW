''' 
Descripción del programa: Crea una aplicación que pida un número
y calcule su factorial (El factorial de un número es el producto
de todos los enteros entre 1 y el propio número y se representa
por el número seguido de un signo de exclamación.
Por ejemplo 5! = 1x2x3x4x5=120)


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
contador = 1
resultado = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
numero = int(input("Introduzca numero cuyo factorial desea saber: "))
resultado = numero
for i in range (numero-1):
    resultado *= contador
    contador += 1
    
print(f"{numero}! = {resultado}")