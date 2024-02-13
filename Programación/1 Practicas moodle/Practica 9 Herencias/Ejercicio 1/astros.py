class astros(object):
    def __init__(self,nombre,radio,rotacion,masa,temp_media,gravedad):
        self.nombre = nombre
        self.radio = radio
        self.rotacion = rotacion
        self.masa = masa
        self.temp_media = temp_media
        self.gravedad = gravedad

    def muestra(self):
        print(f"radio,rotacion,masa,temp_media,gravedad")

class planetas(astros):
    def __init__(self,nombre,radio,rotacion,masa,temp_media,gravedad,dist_sol,orbita_sol,tiene_satelites):
        super().__init__(nombre,radio,rotacion,masa,temp_media,gravedad)
        self.dist_sol = dist_sol
        self.orbita_sol = orbita_sol
        self.tiene_satelites = tiene_satelites
        print(f"Planeta creado correctamente")
        self.satelites = []

    def __str__(self):
        return f"Planeta"
    
    def agregar_satelite(self,satelite):
        self.satelites.append(satelite)

    def muestra(self):
        print(f"Nombre: {self.nombre}\nGravedad: {self.gravedad}\nSatelites?: {self.tiene_satelites}")
    
class satelites(astros):
    def __init__(self,nombre,radio,rotacion,masa,temp_media,gravedad,dist_planeta,orbita_planeta,planeta_perteneciente):
        super().__init__(nombre,radio,rotacion,masa,temp_media,gravedad)
        self.dist_planeta = dist_planeta
        self.orbita_planeta = orbita_planeta
        self.planeta_perteneciente = planeta_perteneciente
        print(f"Satelite creado correctamente")

    def __str__(self):
        return self.nombre
    
    def muestra(self):
        print(f"Nombre: {self.nombre}\nGravedad: {self.gravedad}\nPertenece a: {self.planeta_perteneciente.nombre}")

Tierra = planetas("Tierra",60,24,99999,35,9.8,35454,365,True)
Luna = satelites("Luna",50,20,7777,32,9.2,1232,654,Tierra)

Tierra.muestra()
print()
Luna.muestra()
Tierra.agregar_satelite(Luna.nombre)
print(Tierra.satelites)