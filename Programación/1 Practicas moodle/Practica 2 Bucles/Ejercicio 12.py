'''
Descripción del programa:  Escribe un programa que pida el límite inferior y superior de
un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:

        - La suma de los números que están dentro del intervalo (intervalo abierto).
        - Cuántos números están fuera del intervalo.
        - He informa si hemos introducido algún número igual a los límites del intervalo.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lim_inf = 0
lim_sup = 0
finish = 0
user_num = 0
suma = 0
same_range = 0
out_range = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
while True:
    lim_inf = int(input("Introduzca un limite INFERIOR: "))
    lim_sup = int(input("Introduzca un limite SUPERIOR: "))
    if lim_inf < lim_sup:
        break
    elif lim_inf > lim_sup:
        print("El limite inferior no puede ser mayor que el limite superior, intentelo de nuevo")
    else:
        print("Error no especificado, intentelo de nuevo")

user_num = int(input("Introduzca un numero del rango o 0 para cancelar: "))
while user_num != 0:
        if user_num < lim_inf or user_num > lim_sup:
                out_range += 1
        elif user_num == lim_inf or user_num == lim_sup:
                same_range += 1
        else:
                suma += user_num
        user_num = int(input("Introduzca otro numero o 0 para cancelar: "))
print(f"La suma de los números introducidos dentro del rango es: {suma}")
print(f"{same_range} fueron iguales a uno de los límites del rango")
print(f"{out_range} estuvieron fuera de los límites del rango")