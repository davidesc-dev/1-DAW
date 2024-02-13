### Importar librerias ####
import json

### Funciones ####
def contar_libros(libros):
    print(f"Hay {len(libros)} libros en la libreria")

def LibrosEnRango_precios(libros, precio_inferior, precio_superior):
    LibrosEnRango = [libro for libro in libros if precio_inferior <= float(libro['price']) <= precio_superior]
    return LibrosEnRango

def buscar_por_titulo(libros, cadena):
    libros_coincidentes = [libro for libro in libros if libro['title']['__text'].startswith(cadena)]
    return libros_coincidentes

def obtener_titulos_y_autores(libros):
    titulos_autores = [(libro['title']['__text'], libro['author']) for libro in libros]
    return titulos_autores

def mostrar_menu():
    print('''
MENU LIBRERIA
-1) Contar libros
-2) Rango de precio
-3) Busqueda
-4) Mostrar titulos y autores
-0) Salir
''')

### Programa principal ####
archivo = "EntornosDeDesarrollo/ejercicio1.json"
with open(archivo) as file:
    libreria = json.load(file)

libros = libreria["bookstore"]["book"]

mostrar_menu()
UserChoice = int(input("Elija una opción: ")) 
while UserChoice != 0:
    if UserChoice == 1:
        contar_libros(libros)
        
    elif UserChoice == 2:
        precio_inferior = float(input("Ingrese el límite inferior de precio: "))
        precio_superior = float(input("Ingrese el límite superior de precio: "))
        libros_intervalo = LibrosEnRango_precios(libros, precio_inferior, precio_superior)
        print("Libros en el intervalo de precios:")
        for libro in libros_intervalo:
            print(f"- {libro['title']['__text']}, Precio: ${libro['price']}")            

    elif UserChoice == 3:
        cadena_busqueda = input("Ingrese una cadena para buscar títulos: ")
        libros_coincidentes_titulo = buscar_por_titulo(libros, cadena_busqueda)
        print("Libros cuyo título empieza por la cadena:")
        for libro in libros_coincidentes_titulo:
            print(f"- Título: {libro['title']['__text']}, Año: {libro['year']}")            

    elif UserChoice == 4:
        titulos_autores = obtener_titulos_y_autores(libros)
        print("Títulos de libros con lista de autores:")
        for titulo, autores in titulos_autores:
            print(f"- Título: {titulo}, Autores: {', '.join(autores) if isinstance(autores, list) else autores}")
            
    elif UserChoice == 0:
        print("Hasta la proxima")
    else:
        print("Introduzca una opcion válida de las especificadas en el menú")
    print()
    mostrar_menu()
    UserChoice = int(input("Elija una opción: ")) 