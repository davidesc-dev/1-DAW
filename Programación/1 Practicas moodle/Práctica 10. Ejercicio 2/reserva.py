class Reserva():

    def __init__(self,usuario,espacio,fecha,hora,duracion):
        self.usuario = usuario
        self.espacio = espacio
        self.fecha = fecha
        self.hora = hora
        self.duracion = duracion

    def __str__(self):
        return f"Reserva realizada por {self.usuario} en {self.espacio} dia {self.fecha} y hora {self.hora}"

