from vehiculos import *

coche = Coche("4654KHW", "Corvette", 4, True)
moto = Moto("8945JAS", "Harley Davison", 2, "Rojo")
barco = Barco("4326JHF", "Lagoon", 20, True)
submarino = Submarino("8762JHA", "Submarin", 50, 100)
avion = Avion("7862KJD", "Vueling", 300, 10)
helicoptero = Helicoptero("8211LKT", "Apache", 6, 4)

agregar_vehiculo(coche)
agregar_vehiculo(moto)
agregar_vehiculo(barco)
agregar_vehiculo(submarino)
agregar_vehiculo(avion)
agregar_vehiculo(helicoptero)

imprimir_todo()