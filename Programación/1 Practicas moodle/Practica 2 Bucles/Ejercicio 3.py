''' 
Descripción del programa: Realizar un algoritmo que muestre 
la tabla de multiplicar de un número introducido por teclado.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
numero = 0
contador = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
numero = int(input("Introduzca numero del que quiere saber la tabla: "))
resultado = numero
print ("La tabla del", numero)
for i in range (1, 11):
    contador += 1
    print (numero,"x",contador,"=",resultado)
    resultado += numero