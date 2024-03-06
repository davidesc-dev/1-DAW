from vehiculos import *

coche1 = Coche("4654KHW", "Corvette", 4, True)
moto1 = Moto("8945JAS", "Harley Davison", 2, "Rojo")
barco1 = Barco("ABC123", "Lagoon", 20, True)
submarino1 = Submarino("XYZ456", "Submarin", 50, 100)
avion1 = Avion("ABCD123456", "Vueling", 300, 10)
helicoptero1 = Helicoptero("WXYZ9876", "Apache", 6, 4)

agregar_vehiculo(coche1)
agregar_vehiculo(moto1)
agregar_vehiculo(barco1)
agregar_vehiculo(submarino1)
agregar_vehiculo(avion1)
agregar_vehiculo(helicoptero1)

imprimir_vehiculos()