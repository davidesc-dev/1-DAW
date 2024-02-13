'''
Examen python 1 Tipo B

Autor: David Escutia de Haro
'''
#### Declaración de variables ######
user_choice = 0
num1 = 0
num2 = 0
multi = 0
divi = 0
restante = 0
gender = 0
weight = 0
height = 0
age = 0
activity_level = 0
objetive = 0
daily_calories = 0
repeat = True
objetive_multiplier = 0
activity_multiplier = 0


#### Programa principal ######
    ### Menú principal ####
print("Examen python 1 David Escutia de Haro (Tipo B)")
while user_choice != 4:
    print(
    """
    Menú principal:
    1. Ejercicio 1: Multiplicacion sin operador
    2. Ejercicio 2: Division sin operador
    3. Ejercicio 3: Calculadora de calorias diarias
    4. Salir del Examen
    """)
    user_choice = int(input("Elección: "))

        ### Programa Ejercicio 1 ####
    if  user_choice == 1:                                               # Si la eleccion es 1, se siguen las siguientes instrucciones
        print("Ejercicio 1: Multiplicacion sin operador")               # Se imprime el titulo del ejercicio
        num1 = int(input("Introduzca un primer número: "))              # Se pide un numero
        num2 = int(input("Introduzca un segundo número: "))             # Se pide otro número
        for i in range(num2):                                           # Se hace un bucle for, ya que una multiplicacion no es mas que un numero que se repite otro numero de veces
            multi += num1                                               # Se usa una variable que va guardando la suma de los numeros en cada vuelta del bucle
        print("El resultado de",num1,"x",num2,"es",multi)               # Se imprime el resultado

        ### Programa Ejercicio 2 ####
    elif(user_choice == 2):                                             # Si la eleccion es 2, se siguen las siguientes instrucciones
        restante = 0
        divi = 0
        print("Ejercicio 2: Division sin operador")                     # Se imprime el titulo del ejercicio
        num1 = int(input("Introduzca un primer número: "))              # Se pide un numero
        num2 = int(input("Introduzca un segundo número: "))             # Se pide otro numero
        while (restante < num1):                                        # Una division es un contador de cuantas veces podemos sumar un numero consigo mismo hasta llegar a otro numero sin pasarnos 
            restante += num2                                            # Esta es la variable que va aumentando para ser comparada con el numero que no se puede exceder
            divi += 1                                                   # Contador que va sumando uno en cada vuelta del bucle, este será el resultado
        print("El resultado de",num1,"/",num2,"es",divi)                # Se imprime el resultado

        ### Programa ejercicio 3 ####
    elif(user_choice == 3):                                                             # Si la eleccion es 3 se siguen las siguientes instrucciones
        print("Ejercicio 3: Calculadora de calorias diarias")                           # Titulo del ejercicio
        repeat = True
        while repeat:                                                                   # Bucle while de control para repetir en caso de que el usuario quiera mientras la variable repeat sea true
            while (True):                                                               # Bucle de control para evitar errores de escritura del usuario
                gender = input("Género (masculino/femenino): ")                         # Se le pide al usuario que introduzca un valor de cadena de caracteres para la variable de genero
                if (gender == "masculino" or gender == "femenino"):                     # Se comprueba que la variable genero sea masculino o femenino
                    break                                                               # Se rompe el bucle en caso de que se cumpla la condicion anterior
                else:                                                                   # En caso de que la variable no sea la que se ha pedido especificamente
                    print("Error de escritura, intentelo de nuevo")                     # Se imprime este mensaje de error
            weight = int(input("Peso en kilogramos: "))                                 # Se pide numero entero para la variable de peso
            height = int(input("Altura en centímetros: "))                              # Se pide numero entero para la variable de altura
            age = int(input("Edad en años: "))                                          # Se pide numero entero para la variable de edad
            print()                                                                     # Linea para dejar un espacio, y a continuacion se especifican las opciones del siguiente menu
            print("""                                                                   
Nivel de actividad:
1. Sedentario (poco o ningun ejercicio)
2. Ligero (ejercicio ligero o deportes 1-3 dias a la semana)
3. Moderado (ejercicio lmoderado o deportes 3-5 dias a la semana)
4. Activo (ejercicio diario o deportes 6-7 dias a la semana)
5. Muy activo (ejercicio intenso y deportes todos los dias)
            """)                                                                        
            while (True):                                                                                       # Bucle while para evitar errores del usuario
                activity_level = int(input("Seleccione su nivel de actividad (1-5): "))                         # Se pide numero entero para la variable de nivel de actividad
                if activity_level == 1 or activity_level == 2 or activity_level == 3 or activity_level == 4 or activity_level == 5:         # Se comprueba que la variable del nivel de actividad sea un numero de dentro del rango
                    break                                                               # Se rompe el bucle
                else:                                                                   # En caso de que la variable no sea la que se ha pedido especificamente
                    print("Número incorrecto, intentelo de nuevo")                      # Mensaje de error
            print()                                                                     # Linea para dejar un espacio, y a continuacion se especifican las opciones del siguiente menu
            print("""
            Objetivo:
1. Mantenimiento
2. Pérdida de peso
3. Ganancia de peso
            """)
            while (True):                                                               # Bucle while para evitar errores del usuario
                objetive = int(input("Seleccione su objetivo (1-3): "))                 # Se pide numero entero para la variable de nivel de actividad
                if objetive == 1 or objetive == 2 or objetive == 3:                     # Se comprueba que sea un numero de entre el rango especificado
                    break                                                               # Se rompe el bucle
                else:                                                                   # En caso de que la variable no sea la que se ha pedido especificamente
                    print("Número incorrecto, intentelo de nuevo")                      # Mensaje de error
            print()                                                                     # Linea para dejar un espacio
            if objetive == 1:                                                           # Condiciones para establecer un multiplicador segun el objetivo especificado por el usuario
                objetive_multiplier = 1
            elif objetive == 2:
                objetive_multiplier = 0.95
            elif objetive == 3:
                objetive_multiplier = 1.05

            if activity_level == 1:                                                     # Condiciones para establecer un multiplicador segun la actividad especificada por el usuario
                activity_multiplier == 1
            elif activity_level == 2:
                activity_multiplier = 1.2
            elif activity_level == 3:
                activity_multiplier = 1.4
            elif activity_level == 4:
                activity_multiplier = 1.6
            elif activity_level == 5:
                activity_multiplier = 1.8

            if gender == "masculino":                                                                                                                   # Se establece la formula que hay que seguir en caso del genero masculino
                daily_calories = objetive_multiplier * (88.362 + (13.397 * weight) + (4.799 * height) - (5.667 * age) * activity_multiplier)            # Formula del genero masculino
            elif gender == "femenino":                                                                                                                  # Se establece la formula que hay que seguir en caso del genero femenino
                daily_calories = objetive_multiplier * (447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age) * activity_multiplier)            # Formula del genero femenino
            print(f"Tus calorias diarias recomendadas son: {daily_calories}")                                                                           # Se imprime un mensaje con el numero de calorias diarias 
            print()                                                                                                                                     # Espacio en blanco en el terminal por cuestiones estéticas

            while True:                                                                                 # Bucle de control para evitar errores del usuario
                user_choice = input("¿Desea calcular sus calorias nuevamente? (si/no): ")               # Se pregunta al usuario que si desea repetir y su respuesta se guarda en una variable
                if user_choice == "si":                                                                 # En caso de que escriba un si, repeat sigue siendo true, por lo que la condicion que mantiene en el bucle principal sigue siendo True
                    repeat = True
                    break
                elif user_choice == "no":                                                               # En caso de que escriba un no, repeat pasa a ser False, por lo que la condicion que mantiene en el bucle principal no se cumple, y el usuario sale del bucle
                    repeat = False
                    break
                else:                                                                                   # En caso de que se introduzca cualquier otra cadena de texto no especificada, se imprime un mensaje de error
                    print("Error de escritura, intentelo de nuevo")                                     # Mensaje de error a imprimir

    elif(user_choice == 4):                                                             # Si el usuario selecciona la opcion 4, se incumple la condicion que saca del bucle, pero se despide para que no se ejecute el else
        print("Hasta la proxima")                                                       # Mensaje de despedida

    else:                                                                               # Si el usuario escoge una opcion no especificada se imprime un mensaje de error
        print("Error en la selección, intentelo de nuevo")                              # Mensaje de error