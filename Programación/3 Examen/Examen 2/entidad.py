from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self,nombre,sector,año_incorporacion):
        self.nombre = nombre
        self.sector = sector
        self.año_incorporacion = año_incorporacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} Sector: {self.sector} Año incorporación: {self.año_incorporacion}")

    def antigüedad(self):
        año_actual = 2024
        antigüo = (año_actual - self.año_incorporacion)
        print(f"Esta entidad tiene una antigüedad de {antigüo} años")