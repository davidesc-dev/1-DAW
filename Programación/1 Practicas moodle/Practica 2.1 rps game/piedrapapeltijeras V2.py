'''
Descripción del programa: juego de piedra papel o tijeras vs el ordenador pero con rondas


Version: 2.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import random


##### Declaración de Variables #######
jugar = True
user_choice = 0
bot_choice = 0
rondas = 0


###### Funciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
print("Bienvenido a mi juego de piedra, papel o tijeras")
rondas = int(input("Introduzca un número de rondas para jugar: "))
for nronda in range (rondas):
    bot_choice = random.randint(1,3)
    if bot_choice == 1:
        bot_choice = "piedra"
    elif bot_choice == 2:
        bot_choice = "papel"
    elif bot_choice == 3:
        bot_choice = "tijeras"
    
    print(f"RONDA Nº {nronda}")
    user_choice = input("Introduzca su eleccion (piedra/papel/tijeras): ")
    if bot_choice == "piedra":
        if user_choice == "piedra":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("El resultado fue empate")
        elif user_choice == "papel":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has ganado")
        elif user_choice == "tijeras":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has perdido")
        else:
            print("Error en la escritura de la seleccion, intentelo de nuevo")

    elif bot_choice == "papel":
        if user_choice == "piedra":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has perdido")
        elif user_choice == "papel":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("El resultado fue empate")
        elif user_choice == "tijeras":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has ganado")
        else:
            print("Error en la escritura de la seleccion, intentelo de nuevo")

    else:
        if user_choice == "piedra":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has ganado")
        elif user_choice == "papel":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("Has perdido")
        elif user_choice == "tijeras":
            print(f"Tu eleccion fue {user_choice}")
            print(f"La eleccion del bot fue {bot_choice}")
            print("El resultado fue empate")
        else:
            print("Error en la escritura de la seleccion, intentelo de nuevo")