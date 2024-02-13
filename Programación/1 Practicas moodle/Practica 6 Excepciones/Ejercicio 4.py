'''
Descripción del programa: 
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 15 + "20"

Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
###### Fuciones y Procedimientos (Subprogramas) ######
def main():
    try: 
        resultado = 15 + "12"
    except TypeError:
        print("El numero no puede ser operado junto con una cadena de texto")


###### Programa Principal #############
if __name__ == "__main__":
    main()