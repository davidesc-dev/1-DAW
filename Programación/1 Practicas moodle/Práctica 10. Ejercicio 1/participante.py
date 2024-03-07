class Participante:
    def __init__(self, nombre, identificacion, rol):
        self.nombre = nombre
        self.identificacion = identificacion
        self.rol = rol

    def mostrar_info(self):
        return f"{self.nombre} ({self.rol})"
