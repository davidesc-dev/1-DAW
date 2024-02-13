'''
Descripción del programa: Mostrar en pantalla los N primero
número primos. Se pide por teclado la cantidad de números primos
que queremos mostrar.


Version: 2.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
N = 0
contador = 0
numero = 2
es_primo = True

###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############

N = int(input("¿Cuántos números primos quieres?: "))
while contador < N:
    es_primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El número {numero} es primo")
        contador += 1

    numero += 1