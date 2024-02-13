'''
Descripción del programa: 
En el siguiente programa capture la excepción para evitar que un programador sume una
cadena de texto a un número y muestre el mensaje Los tipos de datos no cuadran
para hacer la operación:
def operar(a, b):
return a+b
def main():
a = int(input())
b = 'hola'
operar(a, b)
main()




Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
###### Fuciones y Procedimientos (Subprogramas) ######
def operar(a,b):
  try:
    return a+b
  except TypeError:
    print("Los tipos de datos no cuadran para hacer la operación")

def main():
  a = int(input("Introduzca numero: "))
  b = 'hola'
  operar(a,b)

###### Programa Principal #############
if __name__ == "__main__":
  main()