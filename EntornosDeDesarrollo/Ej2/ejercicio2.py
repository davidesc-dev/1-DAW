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
def CargarArchivo(archivo):
    global pruebas
    with open(archivo, encoding='utf8') as f:
        pruebas = json.load(f)

def Mostrar_Menu():
    print()
    print("---MENU PRUEBAS---")
    print("1. Mostrar número de pruebas")
    print("2. Mostrar pruebas de duración mayor a 2 horas")
    print("3. Mostrar URL de las pruebas no presenciales")
    print("4. Buscar por ID")
    print("5. Mostrar todas las pruebas")
    print("0. Salir")
    return int(input("Seleccione una opción: "))

def N_Pruebas():
    print(f"Hay un total de {len(pruebas)} pruebas actualmente")
    
def Pruebas2h():
    for prueba in pruebas:
        hora = int(prueba['Horas'])
        if hora > 2:
            print(f"{prueba['Titulo']} => {prueba['Horas']} horas")

def NoPresencial():
    for prueba in pruebas:
        presencialidad = str(prueba['TipoFormacion'])
        if "No" in presencialidad:
            print(f"{prueba['Titulo']} => {prueba['URL']}")
    
def BusquedaID():
    search = str(input("Introduzca un ID: "))
    for prueba in pruebas:
        while True:
            if search == str(prueba['ID']):
                coincide = True
                print(f"Prueba: {prueba['Titulo']} \nImpartido por:")
                for profesor in prueba['Profesorado']:
                    print(f"- {profesor['NombreCompleto']}")
                break
            else:
                coincide = False
                print("No se ha encontrado ninguna prueba con ese identificador, intentelo de nuevo")
                break
    
def MostrarTodo():
    for prueba in pruebas:
        print(f"-Prueba: {prueba['Titulo']} \nImpartido por:")
        for profesor in prueba['Profesorado']:
                print(f"- {profesor['NombreCompleto']}")
        print()

def main():
    CargarArchivo(archivo)
    while True:
        UserChoice = Mostrar_Menu()
        if UserChoice == 1:
            N_Pruebas()

        elif UserChoice == 2:
            Pruebas2h()

        elif UserChoice == 3:
            NoPresencial()

        elif UserChoice == 4:
            BusquedaID()

        elif UserChoice == 5:
            MostrarTodo()


        elif UserChoice == 0:
            break

        else:
            print("Error, introduzca un numero válido")


### Programa principal ####
if __name__ == "__main__":
    main()