from participante import *

class Investigador(Participante):
    def __init__(self, nombre, identificacion, rol, especialidad):
        super().__init__(nombre, identificacion, rol)
        self._especialidad = especialidad
        self.proyectos = []

    def __str__(self):
        print(f"Nombre: {self._nombre} ID: {self._identificacion} Rol: {self._rol} Especialidad: {self._especialidad} Proyectos: {self.proyectos}")

    def asignarproyectos(self,proyecto):
        
        self.mostrarinfo()
