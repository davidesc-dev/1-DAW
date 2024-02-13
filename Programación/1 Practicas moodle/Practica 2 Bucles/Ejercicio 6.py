'''
Descripción del programa: Mostrar en pantalla los N primero
número primos. Se pide por teclado la cantidad de números primos
que queremos mostrar.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
N = 0
num = 0
numero = 1
comprobante = 1

###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############

N = int(input("¿Cuantos numeros primos quieres?: "))
while numero < N:
    while numero % comprobante != 0:
        comprobante += 1
        if numero % comprobante == 0:
            print(f"El numero {numero} es primo")
            comprobante = 1
        else:
            comprobante +=1
            print (f"{numero}{comprobante}")
            continue 
    numero += 1
    print(numero,comprobante)