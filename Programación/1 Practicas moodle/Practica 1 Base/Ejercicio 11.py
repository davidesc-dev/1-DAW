'''
Descripción del programa: Un vendedor recibe un sueldo
base más un 10% extra por comisión de sus ventas, el
vendedor desea saber cuánto dinero obtendrá por
concepto de comisiones por las tres ventas que realiza 
en el mes y el total que recibirá en el mes tomando en
cuenta su sueldo base y comisiones.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
s_base = 0
venta1 = 0
venta2 = 0
venta3 = 0
comisiones = 0
s_total = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
s_base = float(input("Indique su sueldo base: "))
venta1 = float(input("Indique cuanto facturó en la primera venta: "))
venta2 = float(input("Indique cuanto facturó en la segunda venta: "))
venta3 = float(input("Indique cuanto facturó en la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.1
s_total = s_base + comisiones

print(f"El sueldo total a cobrar este mes sería de {s_total}€, siendo {comisiones}€ comisiones")