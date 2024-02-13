'''
Descripción: Hacer que el usuario introduzca los datos de las peliculas y se añada a un catalogo u otro en funcion de la región especificada.

Version 2
Modificado por David Escutia de Haro
'''


##### Modulos y Librerias #####
##### Variables #####
nombre = 0
duracion = 0
año = 0
pais = 0


#### Clases ######
class Pelicula:
	# Constructor de clase
	def __init__(self, titulo, duracion, lanzamiento, pais):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		self.pais = pais
		print('Se ha creado la película:', self.titulo)

	def __str__(self):
		return 'El titulo es {}, la duracion es {} y el año de lanzamiento es {}.'.format(self.titulo, self.duracion, self.lanzamiento)

class Catalogo:
	peliculas = [] # Esta lista contendrá objetos de la clase Pelicula     
	def __init__(self, nombre, peliculas=[]):
		self.peliculas = peliculas
		self.nombre=nombre
		# print('Se ha creado el catalogo: ', self.nombre)

	def agregar(self, p): # p será un objeto Pelicula
		self.peliculas.append(p)

	def mostrar(self):
		print(f"\nEl catalogo {self.nombre} tiene las siguientes peliculas: ")
		for p in self.peliculas:
			print(p) # Print toma por defecto str(p)
		
#### Programa Principal #######
	# Crear los catálogos
catalogousa = Catalogo("USA", [])
catalogoesp = Catalogo("ESPAÑA", [])

	# Formulario
nombre = input("Introduzca el nombre de la pelicula o no introduzca nada para finalizar: ")
while nombre != "":
	duracion = input("Introduzca la duracion de la pelicula en minutos: ")
	lanzamiento = input("Introduzca el año de lanzamiento de la pelicula: ")
	while True:
		pais = input("Introduzca el pais de la pelicula: ")
		if pais not in ["esp","usa","ESP","USA"]:
			print("Revise la ortografia e intentelo de nuevo (esp/usa)")
		else:
			break
	pelicula = Pelicula(nombre, duracion, lanzamiento, pais)
	if pais in ["usa","USA"]:
		catalogousa.agregar(pelicula)
	else:
		catalogoesp.agregar(pelicula)

	nombre = input("Introduzca el nombre de la pelicula o no introduzca nada para finalizar: ")
	
	# Mostrar los catalogos al terminar de añadir peliculas
catalogousa.mostrar()
catalogoesp.mostrar()
