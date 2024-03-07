class Empresa:
    def __init__(self, nombre, sector):
        self.nombre = nombre
        self.sector = sector
        self.proyectos_apoyados = []

    def apoyar_proyecto(self, proyecto):
        self.proyectos_apoyados.append(proyecto)
        print(f"{self.nombre} apoya el proyecto {proyecto.titulo}")
