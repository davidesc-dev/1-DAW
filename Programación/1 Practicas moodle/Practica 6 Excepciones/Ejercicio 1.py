'''
Descripción del programa: 
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 10/0




Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
###### Fuciones y Procedimientos (Subprogramas) ######
def main():
    try:
        result = 10/0
    except ZeroDivisionError:
        print("No es posible dividir entre 0, intentelo de nuevo")


###### Programa Principal #############
if __name__ == "__main__":
    main()