from vehiculos.py import *

programa = Programa()

coche1 = Coche("1234ABC", "Toyota", 4, True)
moto1 = Moto("5678DEF", "Honda", 2, "Rojo")
barco1 = Barco("ABC123", "Yate", 20, True)
submarino1 = Submarino("XYZ456", "Submarino 1", 50, 100)
avion1 = Avion("ABCD123456", "Boeing", 300, 10)
helicoptero1 = Helicoptero("WXYZ9876", "Apache", 6, 4)

programa.agregar_vehiculo(coche1)
programa.agregar_vehiculo(moto1)
programa.agregar_vehiculo(barco1)
programa.agregar_vehiculo(submarino1)
programa.agregar_vehiculo(avion1)
programa.agregar_vehiculo(helicoptero1)

programa.imprimir_vehiculos()