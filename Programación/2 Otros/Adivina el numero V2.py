'''
Descripción del programa: Juego de adivinar el numero.


Version: 2.0
Autor: David Escutia de Haro
''' 
##### Declaración de variables #######
number = 0
secret_number = 777
dificulty = 0
vidas = 0
easy = 10
med = 5
hard = 3

##### Importar librerias externas #######
import random


secret_number = int(input("Persona 1, introduzca el número secreto: "))

from os import system
system("cls")
##### Introducción #######
print(
"""
▀█████████▄   ▄█     ▄████████ ███▄▄▄▄    ▄█    █▄     ▄████████ ███▄▄▄▄    ▄█  ████████▄   ▄██████▄  
  ███    ███ ███    ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███▀▀▀██▄ ███  ███   ▀███ ███    ███ 
  ███    ███ ███▌   ███    █▀  ███   ███ ███    ███   ███    █▀  ███   ███ ███▌ ███    ███ ███    ███ 
 ▄███▄▄▄██▀  ███▌  ▄███▄▄▄     ███   ███ ███    ███  ▄███▄▄▄     ███   ███ ███▌ ███    ███ ███    ███ 
▀▀███▀▀▀██▄  ███▌ ▀▀███▀▀▀     ███   ███ ███    ███ ▀▀███▀▀▀     ███   ███ ███▌ ███    ███ ███    ███ 
  ███    ██▄ ███    ███    █▄  ███   ███ ███    ███   ███    █▄  ███   ███ ███  ███    ███ ███    ███ 
  ███    ███ ███    ███    ███ ███   ███ ███    ███   ███    ███ ███   ███ ███  ███   ▄███ ███    ███ 
▄█████████▀  █▀     ██████████  ▀█   █▀   ▀██████▀    ██████████  ▀█   █▀  █▀   ████████▀   ▀██████▀  
                                                                                                      
+================================+
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|  Pero antes, escoge dificultad |
|      Facil: 10 vidas           |
|      Medio: 5 vidas            |
|      Dificil: 3 vidas          |
+================================+
""")

##### Programa principal #######
dificulty = input("Dificultad: ")
if dificulty == "facil":
    vidas = int(easy)
elif dificulty == "medio":
    vidas = int(med)
else:
    vidas = int(hard)

print("Has seleccionado el modo ", dificulty," y tienes ", vidas ," vidas, suerte",sep="")

number = int(input("Di un numero: "))

while number != secret_number and vidas != 0:
    vidas -= 1
    if number > secret_number:
        print("NO. El numero secreto es mas pequeño, te quedan ", vidas , " vidas!",sep="")
    else:
        print("NO. El numero es mas grande, te quedan ", vidas , " vidas!",sep="")
    number = int(input("Di otro numero: "))

if vidas > 0:
    print ("""
   ___                   _       
  / __|__ _ _ _  __ _ __| |_ ___ 
 | (_ / _` | ' \/ _` (_-<  _/ -_)
  \___\__,_|_||_\__,_/__/\__\___|
                                       
""")
else:
    print ("""
 ___            _ _    _       
 | _ \___ _ _ __| (_)__| |_ ___ 
 |  _/ -_) '_/ _` | (_-<  _/ -_)
 |_| \___|_| \__,_|_/__/\__\___|
""")
    print("El numero secreto era:",secret_number)