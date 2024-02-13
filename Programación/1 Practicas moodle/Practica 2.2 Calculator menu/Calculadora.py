'''
Descripción del programa: DESCRIPCION


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
user_choice = 1
num1 = 0
num2 = 0
result = 0


###### Funciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
print("Calculadora de David")
while(user_choice != 0):
    print("""
    ╔═══════════════════════════════════╗
    ║   1. Suma/resta                   ║
    ║   2. Multiplicacion/division      ║
    ║   0. Salir                        ║
    ╚═══════════════════════════════════╝
    """)
    user_choice = int(input("Elección: "))
    if user_choice == 1:
        num1 = int(input("Introduzca un primer número: "))
        num2 = int(input("Introduzca un segundo número: "))
        while(user_choice != 0):
            print("""
            ╔═════════════════════════╗
            ║   1. Sumar              ║
            ║   2. Restar             ║
            ║   3. Menu principal     ║
            ║   0. Salir              ║
            ╚═════════════════════════╝
            """)
            user_choice = int(input("Elección: "))
            print()
            if user_choice == 1:
                result = num1 + num2
                print(f"{num1}+{num2}={result}")
            elif user_choice == 2:
                result = num1 - num2
                print(f"{num1}-{num2}={result}") 
            elif user_choice == 3:
                break 
            elif user_choice == 0:
                print("Hasta la proxima")   
            else:
                print("Elección incorrecta, vuelva a intentarlo")     


    elif user_choice == 2:
        num1 = int(input("Introduzca un primer número: "))
        num2 = int(input("Introduzca un segundo número: "))
        while(user_choice != 0):
            print("""
            ╔═════════════════════════╗
            ║   1. Multiplicar        ║
            ║   2. Dividir            ║
            ║   3. Menu principal     ║
            ║   0. Salir              ║
            ╚═════════════════════════╝
            """)
            user_choice = int(input("Elección: "))
            print()
            if user_choice == 1:
                result = num1 * num2
                print(f"{num1}x{num2}={result}")
            elif user_choice == 2:
                result = num1 / num2
                print(f"{num1}/{num2}={result}") 
            elif user_choice == 3:
                break     
            elif user_choice == 0:
                print("Hasta la proxima")
            else:
                print("Elección incorrecta, vuelva a intentarlo")  
    elif user_choice == 0:
        print("Hasta la proxima")
    else:
        print("Elección incorrecta, vuelva a intentarlo")