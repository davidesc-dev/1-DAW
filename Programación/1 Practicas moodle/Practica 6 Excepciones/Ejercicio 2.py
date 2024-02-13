'''
Descripción del programa: 
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
lista = [1, 2, 3, 4, 5]
lista[10]


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lista = [1, 2, 3, 4, 5]

###### Fuciones y Procedimientos (Subprogramas) ######
def main():
    try:
        lista[10]
    except IndexError:
        print("El elemento indicado no existe.")


###### Programa Principal #############
if __name__ == "__main__":
    main()