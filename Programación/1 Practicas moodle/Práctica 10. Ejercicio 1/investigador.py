from participante import Participante

class Investigador(Participante):
    def __init__(self, nombre, identificacion, rol, especialidad):
        super().__init__(nombre, identificacion, rol)
        self.especialidad = especialidad
        self.proyectos = []

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print(f"{self.nombre} asignado al proyecto {proyecto.titulo}")
