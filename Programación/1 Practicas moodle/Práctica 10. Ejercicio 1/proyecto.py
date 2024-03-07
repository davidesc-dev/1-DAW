class Proyecto:
    def __init__(self, titulo, area_investigacion):
        self.titulo = titulo
        self.area_investigacion = area_investigacion
        self.estado = 'Inicial'
        self.participantes = []

    def agregar_participante(self, participante):
        self.participantes.append(participante)
        print(f"Participante {participante.nombre} agregado al proyecto {self.titulo}")

    def actualizar_estado(self, estado):
        self.estado = estado
        print(f"Estado del proyecto {self.titulo} actualizado a {estado}")
