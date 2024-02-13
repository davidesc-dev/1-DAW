'''
Descripción del programa: Una tienda ofrece un descuento
del 15% sobre el total de la compra y un cliente desea
saber cuánto deberá pagar finalmente por su compra.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
precio = 0
descuento = 0
precio_final = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
precio = float(input("Introduzca el precio de sus productos: "))
descuento = (precio) * 0.15
precio_final = precio - descuento

print(f"El precio a pagar seria de {precio_final}€, ¡Has ahorrado {descuento}€!")