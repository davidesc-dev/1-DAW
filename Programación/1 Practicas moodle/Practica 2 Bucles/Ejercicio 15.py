'''
Realizar un ejemplo de menú, donde podemos escoger las distintas
opciones hasta que seleccionamos la opción de "Salir".


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
palabra = 0
num1 = 0
num2 = 0
resultado = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
print("La calculadora de David")
while palabra != "salir":
    palabra = input("Indique si quiere sumar, restar, multiplicar, dividir o salir: ")
    if palabra == "sumar":
        palabra = input("Introduzca un primer numero: ")
        num1 = int(palabra)
        palabra = input("Introduzca un primer numero: ")
        num2 = int(palabra)
        resultado = num1 + num2
        print(f"{num1}+{num2}={resultado}")

    elif palabra == "restar":
        palabra = input("Introduzca un primer numero: ")
        num1 = int(palabra)
        palabra = input("Introduzca un primer numero: ")
        num2 = int(palabra)
        resultado = num1 - num2
        print(f"{num1}-{num2}={resultado}")

    elif palabra == "multiplicar":
        palabra = input("Introduzca un primer numero: ")
        num1 = int(palabra)
        palabra = input("Introduzca un primer numero: ")
        num2 = int(palabra)
        resultado = num1 * num2
        print(f"{num1}*{num2}={resultado}")

    elif palabra == "dividir":
        palabra = input("Introduzca un primer numero: ")
        num1 = int(palabra)
        palabra = input("Introduzca un primer numero: ")
        num2 = int(palabra)
        resultado = num1 / num2
        print(f"{num1}/{num2}={resultado}")

    elif palabra == "salir":
        print("Hasta la próxima")
        
    else:
        print("Intentelo de nuevo")