class Proyecto():
    def __init__(self,titulo,area_investigacion,estado):
        self._titulo = titulo
        self._area_investigación = area_investigacion
        self._estado = estado
        self.participantes = []

    def __str__(self):
        print(f"Titulo: {self._titulo} area: {self._area_investigación} estado: {self._estado}")

    def agregarparticipante(self,participante):
        if participante not in self.participantes:
            self.participantes.append(participante)
        else:
            print(f"El participante {participante} ya existe")
    
    def actualizarestado(self,nestado):
        self.estado = nestado

    def listarparticipantes(self):
        for participante in self.participantes:
            print(f"-{participante}")
