'''
Descripción del programa: Vamos a crear un programa que tenga el siguiente menú:
    1. Añadir número a la lista: 
        Me pide un número de la lista y lo añade al final de la lista.
    2. Añadir número de la lista en una posición: 
        Me pide un número y una posición, y si la posición existe en la lista lo
        añade a ella (la posición se pide a partir de 1).
    3. Longitud de la lista: 
        te muestra el número de elementos de la lista.
    4. Eliminar el último número: 
        Muestra el último número de la lista y lo borra.
    5. Eliminar un número: 
        Pide una posición, y si la posición existe en la lista lo borra de ella
        (la posición se pide a partir de 1).
    6. Contar números: 
        Te pide un número y te dice cuantas apariciones hay en la lista.
    7. Posiciones de un número: 
        Te pide un número y te dice en que posiciones está (contando desde 1).
    8. Mostrar números: 
        Muestra los números de la lista
    9. Salir



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lista = []
listaaux = []
userchoice = 0
counter = 0
modificar = 0
posicion = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
while userchoice != 9:
    print('''
1. Añadir número a la lista
2. Añadir número de la lista en una posición
3. Longitud de la lista
4. Eliminar el último número
5. Eliminar un número
6. Contar números
7. Posiciones de un número
8. Mostrar números
9. Salir
''')
    userchoice = int(input("Introduzca una opción: "))
    if userchoice == 1:
        modificar = int(input("Introduzca un numero a añadir: "))
        lista.append(modificar)
    elif userchoice == 2:
        modificar = int(input("Introduzca un numero a añadir: "))
        posicion = int(input(f"Introduzca la posición donde añadir (1-{len(lista)}): "))
        lista.insert(posicion,modificar)
    elif userchoice == 3:
        print(f"La lista tiene {len(lista)} números")
    elif userchoice == 4:
        del lista[-1]
    elif userchoice == 5:
        posicion = int(input(f"Introduzca la posición para eliminar (1-{len(lista)-1}): "))
    elif userchoice == 6:
        counter = 0
        userchoice = int(input(f"Introduzca un numero para saber cuantas veces aparece: "))
        for i in range(len(lista)):
            if lista[i] == userchoice:
                counter +=1
        if counter > 0: 
            print(f"El número {userchoice} aparece {counter} veces en la lista!")
        else:
            print(f"El número {userchoice} no está en la lista")
    elif userchoice == 7:
        listaaux = []
        userchoice = int(input(f"Introduzca un numero para saber en que posiciones está: "))
        for i in range(len(lista)):
            if lista[i] == userchoice:
                listaaux.append(i+1)
        if len(listaaux) > 0:
            print(f"Posiciones en las que se encuentra el número {userchoice}:")
            print(listaaux)
        else:
            print(f"El numero {userchoice} no se encuentra en la lista")
    elif userchoice == 8:
        print(lista)
    elif userchoice == 9:
        print("Hasta la proxima")
    else:
        print("Introduzca un numero válido")
        print()