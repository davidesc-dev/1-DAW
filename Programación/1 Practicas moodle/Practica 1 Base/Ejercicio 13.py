'''
Descripción del programa: Dos vehículos viajan a diferentes velocidades (v1 y v2)
y están distanciados por una distancia d. El que está detrás viaja a una
velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los
dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y
mostrar en qué tiempo (minutos) alcanzará el vehículo más rápido al otro.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
v1 = 0
v2 = 0
d = 0
v_diff = 0
t = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
v1 = int(input("Introduzca en km/h la velocidad del primer vehiculo: "))
v2 = int(input("Introduzca en km/h la velocidad del segundo vehiculo: "))
d = int(input("Introduzca en km la distancia que separa los dos vehiculos: "))

v_diff = abs(v2 - v1)
t = (d / v_diff) * 60

print(f"Los vehículos se cruzarán dentro de {t} minutos")