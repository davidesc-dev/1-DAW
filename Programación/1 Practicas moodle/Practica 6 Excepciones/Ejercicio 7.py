'''
Descripción del programa: 
Capture la excepción que valide cuando se trata de obtener una llave que no se encuentra
en un diccionario y muestre el mensaje Intenta acceder una llave que no se
encuentra en el diccionario:
def main():
dict = {'Arles': 'Java', 'Dennis' : 'C', 'Das':'Python'}
print(dict['Ada'])
main()
 


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
###### Fuciones y Procedimientos (Subprogramas) ######
def main():    
    dict = {'Arles': 'Java', 'Dennis' : 'C', 'Das':'Python'}
    try:
        print(dict['Ada'])
    except KeyError:
        print("Intenta acceder una llave que no se encuentra en el diccionario")

###### Programa Principal #############
if __name__ == "__main__":
    main()