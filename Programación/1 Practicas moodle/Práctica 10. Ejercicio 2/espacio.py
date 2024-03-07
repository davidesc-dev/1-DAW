class Espacio():

    def __init__(self,identificador,tipo,capacidad,disponibilidad=True):

        self.identificador=identificador
        self.tipo=tipo
        self.capacidad=capacidad
        self.disponibilidad=disponibilidad

    def __str__(self):
        return f"Sala {self.identificador} del tipo {self.tipo} con capacidad {self.capacidad} y disponibilidad {self.disponibilidad}."
    
    def getDisponibilidad(self):
        return self.disponibilidad
    
    def reservar(self):
        self.disponibilidad=False

    def cancelar_reserva(self) :
        self.disponibilidad=True