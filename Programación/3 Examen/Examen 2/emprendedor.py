from entidad import *

class Emprendedor(Entidad):
    def __init__(self, nombre, sector, año_incorporacion,habilidades):
        super().__init__(nombre, sector, año_incorporacion)
        self.proyectos = []
        self.habilidades = []
        print(f"Emprendedor {self.nombre} creado correctamente")

    def agregar_proyecto(self,proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
            print(f"El proyecto {proyecto} fue añadido correctamente")
        else:
            print(f"Ya constaba de que estaba trabajando en ese proyecto")

    def listar_habilidades(self):
        if self.habilidades.__len__ == 0:
            print("No hay ninguna habilidad, añada alguna primero")
        else:
            print(f"Habilidad(es) de {self.nombre}")
            for producto in self.habilidades:
                print(f"  -{producto}")