'''
Descripción del programa: Juego de adivinar el numero.


Version: 3.0
Autor: David Escutia de Haro
''' 

##### Declaración de variables #######
number = 0
secret_number = 0
dificulty = 0
vidas = 0
noplayers = 0
easy = 10
med = 5
hard = 3


##### Importar librerias externas #######
import random
import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


##### Presets #######
noplayers = int(input("Establece un numero de jugadores 1/2: "))

print(
"""
██████╗ ██████╗ ███████╗███████╗███████╗████████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝
██████╔╝██████╔╝█████╗  ███████╗█████╗     ██║   ███████╗
██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║   ╚════██║
██║     ██║  ██║███████╗███████║███████╗   ██║   ███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                         

""")
if noplayers == 1:
    n1 = int(input("Introduce un primer numero entre el que estará el número a adivinar: "))
    n2 = int(input("Introduce un segundo numero entre el que estará el número a adivinar: "))

    secret_number = random.randint(n1, n2)
elif noplayers == 2:
    secret_number = int(input("Introduzca el número secreto que la otra persona tratará de adivinar: "))
else:
    print ("No estableció un numero de jugadores válido")
    input()
    exit()

clear()


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
""")

if noplayers == 1:
    print(f"""                                                                                                  
+===================================+
| Introduce un número entero        |
| y adivina qué número he           |
| elegido para ti entre {n1} y {n2}  
|  Pero antes, escoge dificultad    |
|      Facil: 10 vidas              |
|      Medio: 5 vidas               |
|      Dificil: 3 vidas             |
+===================================+
""")
else:
    print("""
+===================================+
| Introduce un número entero        |
| y adivina qué número ha           |
| elegido para ti el jugador 1      | 
|  Pero antes, escoge dificultad    |
|      Facil: 10 vidas              |
|      Medio: 5 vidas               |
|      Dificil: 3 vidas             |
+===================================+
""")

##### Programa principal #######
while(dificulty != "facil" or dificulty != "medio" or dificulty != "dificil"):
    dificulty = input("Dificultad: ")
    if dificulty == "facil":
        vidas = int(easy)
        break
    elif dificulty == "medio":
        vidas = int(med)
        break
    elif dificulty == "dificil":
        vidas = int(hard)
        break
    else:
        print("Error al seleccionar la dificultad, intentelo de nuevo")

print("Has seleccionado el modo ", dificulty," y tienes ", vidas ," vidas, suerte",sep="")

number = int(input("Di un numero: "))

while number != secret_number and vidas != 0:
    vidas -= 1
    if number > secret_number:
        print("NO. El numero secreto es MAS PEQUEÑO, te quedan ", vidas , " vidas!",sep="")
    else:
        print("NO. El numero es MAS GRANDE, te quedan ", vidas , " vidas!",sep="")
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