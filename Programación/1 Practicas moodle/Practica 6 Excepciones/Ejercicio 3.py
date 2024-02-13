'''
Descripción del programa: 
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
colores['blanco']



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }


###### Fuciones y Procedimientos (Subprogramas) ######
def main():
    try:
        colores['blanco']
    except KeyError:
        print("El indice introducido no está definido")


###### Programa Principal #############
if __name__ == "__main__":
    main()