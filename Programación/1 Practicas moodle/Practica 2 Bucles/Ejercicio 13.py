'''
Descripción del programa: Una persona adquirió un producto para pagar
en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 €
y así sucesivamente. Realizar un algoritmo para determinar cuánto debe
pagar mensualmente y el total de lo que pagó después de los 20 meses.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
mes = 0
pagomes = 10
pagototal = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for i in range (20):
    mes += 1
    pagototal += pagomes
    print(f"Pago del mes nº {mes} -> {pagomes}€")
    pagomes *= 2

print(f"Pago total: {pagototal}€")