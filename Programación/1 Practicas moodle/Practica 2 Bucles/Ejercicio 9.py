'''
Descripción del programa: Crea una aplicación que permita adivinar
un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número
a adivinar es mayor o menor que el introducido,además de los
intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al límite de intentos
te muestra el número que había generado.



Version: 1.0
Autor: David Escutia de Haro
''' 
##### Importar librerias externas #######
import random


##### Declaración de Variables #######
number = 0
secret_number = 0
vidas = 10


###### Fuciones y Procedimientos (Subprogramas) ######
secret_number = random.randint(1, 100)


##### Programa principal #######
number = int(input("Di un numero entre 1 y 100: "))

while number != secret_number and vidas != 0:
    vidas -= 1
    if number > secret_number:
        print("NO. El numero secreto es MAS PEQUEÑO, te quedan ", vidas , " vidas!",sep="")
    else:
        print("NO. El numero es MAS GRANDE, te quedan ", vidas , " vidas!",sep="")
    number = int(input("Di otro numero: "))

if vidas > 0:
    print ("Ganaste")
else:
    print ("Perdiste")
    print("El numero secreto era:",secret_number)