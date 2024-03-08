from emprendedor import *
from empresa import *

class Startup(Entidad):
    def __init__(self, nombre, sector, año_incorporacion,inversion_recibida):
        super().__init__(nombre, sector, año_incorporacion)
        self.inversion_recibida = inversion_recibida
        self.mentores = []

    def agregar_mentor(self,mentor):
        if mentor not in self.mentores:
            self.mentores.append(mentor)
            print(f"El mentor {mentor} fue añadido correctamente")
        else:
            print(f"El mentor {mentor} ya se encontraba en la lista")

    def mostrar_info(self):
        return super().mostrar_info()