'''
Descripción del programa: Algoritmo que pida números hasta que se introduzca 
un cero. Debe imprimir la suma y la media de todos los números introducidos.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
counter = 0
sumatoria = 0
media = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
numero = int(input("Introduce un numero o 0 para salir: "))
if numero <= 0:
    print ("Número invalido")
    exit()
else:
    while numero != 0:
        sumatoria += numero
        counter += 1
        numero = int(input("Introduce otro numero o 0 para terminar: "))

media = sumatoria / counter

print(f"La suma de todos los números es {sumatoria}, y la media es {media}")