class Empresa():
    def __init__(self,nombre,sector):
        self.nombre = nombre
        self.sector = sector
        self.proyectos_apoyados = []

    def __str__(self):
        print(f"Nombre: {self.nombre} Sector: {self.sector} Proyectos apoyados: {self.proyectos_apoyados}")

    def apoyarproyecto(self,proyecto):
        self.proyectos_apoyados.append(proyecto)
        print(f"La empresa {self.nombre} ahora apoya el proyecto {proyecto}")