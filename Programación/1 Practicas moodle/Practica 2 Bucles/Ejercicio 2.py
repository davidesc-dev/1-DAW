'''
Descripción del programa: Realizar un algoritmo que pida números (se pedirá por teclado
la cantidad de números a introducir). El programa debe informar de cuantos números
introducidos son mayores que 0, menores que 0 e iguales a 0.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
finish = -1
mayores = 0
menores = 0
iguales = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
numero = int(input("Introduzca un numero: "))
while numero != finish:
    if numero < 0:
        menores += 1
    elif numero > 0:
        mayores += 1
    else:
        iguales += 1
    numero = int(input(f"Introduzca otro numero o {finish}: "))

print(f"De los números introducidos, {mayores} son mayores, {menores} son menores y {iguales} son iguales que 0")