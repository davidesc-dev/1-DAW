'''
Descripción del programa: 
Vamos a realizar dos funciones: una que nos permita convertir un número entero a binario, y
otra que nos permita convertir un numero binario a decimal.
    ● ConvertirABinario: Función que recibe un número entero y devuelve una cadena con
      la representación del número en binario.
    ● ConvertirADecimal: Función que recibe una cadena con la representación binaria de
      un número y devuelve el número en decimal.
      
Crea un programa principal que permita convertir de decimal a binario y de binario a
decimal.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
userchoice = 0


###### Fuciones y Procedimientos (Subprogramas) ######
def ConvertirABinario(n):
    
def ConvertirADecimañl(n):
    


###### Programa Principal #############
print ('''
1. Convertir numero a binario
2. Convertir numero a decimal
0. Salir
''')
userchoice = int(input("Seleccione una accion: "))
while userchoice != 0:
    if userchoice == 1:
        print("DECIMAL => BINARIO")
    elif userchoice == 2:
        print("BINARIO => DECIMAL")
    elif userchoice == 0:
        print("Hasta la próxima")
    else:
        print("Introduzca una opcion válida")