'''
Ejercicio JSON 4

Version: 1
Autor: David Escutia de Haro
'''
### Importar librerias ####
import json

### Variables globales ####
archivo = "EntornosDeDesarrollo/Ej4/ejercicio4.json"
UserChoice = 0

### Funciones ####
def cargarjson(archivo):
    global discos
    with open(archivo, encoding='utf-8') as file:
        discos = json.load(file)

def cargarmenu():
    print()
    print("---MENU METALLICA---")
    print("1. Listar info")
    print("2. Contar info")
    print("3. Buscar info")
    print("4. Cancion en disco")
    print("0. Salir")
    return int(input("Seleccione una opción: "))

def listinfo():
    for disco in discos:
        print(f"Album: {disco['album']['name']}")
        for song in disco['album']['tracks']['track']:
            print(f"  - {song['name']}")
        print()

def continfo():
    for disco in discos:
        print(f"Album: {len(disco['album']['tracks']['track'])} discos")

def busqinfo():
    oyentesmin = int(input("Numero minimo de oyentes: "))
    oyentesmax = int(input("Numero maximo de oyentes: "))
    for disco in discos:
        oyentes = int(disco['album']['listeners'])
        if oyentes > oyentesmin and oyentes < oyentesmax:
            print(disco['album']['name'])
            print(f"Oyentes: {disco['album']['listeners']}")
            for etiqueta in disco ['album']['tags']['tag']:
                tag = etiqueta['name']
                print(f"  - {tag}")
            print()

def cancionendisco():
    search = str(input("Introduzca cancion a buscar: "))
    for disco in discos:
        for canciones in disco['album']['tracks']['track']:
            if search == canciones['name']:
                print(f"Cancion encontrada en el album {disco['album']['name']}")

def main():
    cargarjson(archivo)
    while True:
        UserChoice = cargarmenu()
        if UserChoice == 1:
            listinfo()
        elif UserChoice == 2:
            continfo()
        elif UserChoice == 3:
            busqinfo()
        elif UserChoice == 4:
            cancionendisco()
        elif UserChoice == 0:
            break
        else:
            print("Introduzca una opcion válida")



### Programa principal ####
if __name__ == "__main__":
    main()