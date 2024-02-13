'''
Ejercicio 2 JSON


Version: 1
Autor: David Escutia de Haro
'''
### Importar librerias ####
import json


### Definir variables globales ####
archivo = "EntornosDeDesarrollo/Ej2/ejercicio2.json"
UserChoice = 0


### Funciones ####
# Función para cargar el contenido del archivo JSON en la variable global 'pruebas'
def CargarArchivo(archivo):
    global pruebas  # Se declara la variable global 'pruebas'
    with open(archivo) as f:  # Se abre el archivo en modo lectura
        pruebas = json.load(f)  # Se carga el contenido del archivo JSON en la variable 'pruebas'

# Función para mostrar el menú de opciones
def Mostrar_Menu():
    print()
    print("---MENU PRUEBAS---")  # Se imprime el encabezado del menú
    print("1. Mostrar número de pruebas")
    print("2. Mostrar pruebas de duración mayor a 2 horas")
    print("3. Mostrar URL de las pruebas no presenciales")
    print("4. Buscar por ID")
    print("5. Mostrar todas las pruebas")
    return int(input("Seleccione una opción: "))  # Se lee la opción seleccionada por el usuario y se retorna como un entero

# Función para mostrar el número total de pruebas
def N_Pruebas():
    print(f"Hay un total de {len(pruebas)} pruebas actualmente")  # Se imprime la cantidad total de pruebas

# Función para mostrar pruebas con duración mayor a 2 horas
def Pruebas2h():
    for prueba in pruebas:  # Se itera sobre cada prueba en la lista
        hora = int(prueba['Horas'])  # Se convierte la duración de la prueba a entero
        if hora > 2:  # Se verifica si la duración es mayor a 2 horas
            print(f"{prueba['Titulo']} => {prueba['Horas']} horas")  # Se imprime el título y la duración de la prueba

# Función para mostrar URL de pruebas no presenciales
def NoPresencial():
    for prueba in pruebas:  # Se itera sobre cada prueba en la lista
        presencialidad = str(prueba['TipoFormacion'])  # Se obtiene el tipo de formación como cadena
        if "No" in presencialidad:  # Se verifica si el tipo de formación contiene "No"
            print(f"{prueba['Titulo']} => {prueba['URL']}")  # Se imprime el título y la URL de la prueba no presencial

# Función para buscar una prueba por ID
def BusquedaID():
    search = str(input("Introduzca un ID: "))  # Se solicita al usuario que introduzca un ID
    for prueba in pruebas:  # Se itera sobre cada prueba en la lista
        if search == str(prueba['ID']):  # Se verifica si el ID de la prueba coincide con el ID buscado
            print(f"Prueba: {prueba['Titulo']} \nImpartido por:")  # Se imprime el título de la prueba y un encabezado
            for profesor in prueba['Profesorado']:  # Se itera sobre cada profesor en el profesorado de la prueba
                print(f"- {profesor['NombreCompleto']}")  # Se imprime el nombre completo de cada profesor

# Función para mostrar todas las pruebas
def MostrarTodo():
    for prueba in pruebas:  # Se itera sobre cada prueba en la lista
        print(f"-Prueba: {prueba['Titulo']} \nImpartido por:")  # Se imprime el título de la prueba y un encabezado
        for profesor in prueba['Profesorado']:  # Se itera sobre cada profesor en el profesorado de la prueba
            print(f"  |  Profesor: {profesor['NombreCompleto']}")  # Se imprime el nombre completo de cada profesor
        print()  # Se imprime una línea en blanco para separar las pruebas

# Función principal
def main():
    CargarArchivo(archivo)  # Se carga el archivo JSON al inicio del programa
    while True:
        UserChoice = Mostrar_Menu()  # Se muestra el menú y se lee la opción del usuario
        if UserChoice == 1:
            N_Pruebas()  # Si la opción es 1, se muestra el número total de pruebas

        elif UserChoice == 2:
            Pruebas2h()  # Si la opción es 2, se muestran las pruebas con duración mayor a 2 horas

        elif UserChoice == 3:
            NoPresencial()  # Si la opción es 3, se muestran las URLs de las pruebas no presenciales

        elif UserChoice == 4:
            BusquedaID()  # Si la opción es 4, se realiza la búsqueda de una prueba por ID

        elif UserChoice == 5:
            MostrarTodo()  # Si la opción es 5, se muestran todas las pruebas

        elif UserChoice == 0:  # Si la opción es 0, se sale del bucle while y termina el programa
            break

        else:
            print("Error, introduzca un numero válido")  # Si la opción no es válida, se imprime un mensaje de error

### Programa principal ####
if __name__ == "__main__":
    main()  # Se ejecuta la función principal al iniciar el programa
