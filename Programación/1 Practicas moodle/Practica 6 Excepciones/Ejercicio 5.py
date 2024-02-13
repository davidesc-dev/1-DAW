'''
Descripción del programa: 
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento.
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún
elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de
tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego
muestra su contenido.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
elementos = [1,5,-2]


###### Fuciones y Procedimientos (Subprogramas) ######
def AgregarElemento():
    while True:
        try:
            ElementoAgregado = int(input("Introduzca el elemento que desea agregar: ")) 
        except ValueError:
            print("El valor especificado no puede ser añadido")
            break
        if ElementoAgregado in elementos:
            print(f"Error: Imposible añadir elementos duplicados => {ElementoAgregado}.")
            break
        else:
            elementos.append(ElementoAgregado)
            print("Elemento añadido correctamente")
            break
def main():
    print(f"Lista => {elementos}")
    while True:
        opcion = input("Desea añadir un elemento más? (S/N): ")
        if opcion == "S":
            AgregarElemento()
        elif opcion == "N":
            print(elementos)
            break
        else:
            print("Opcion no válida, intentelo de nuevo")


###### Programa Principal #############
if __name__ == "__main__":
    main()