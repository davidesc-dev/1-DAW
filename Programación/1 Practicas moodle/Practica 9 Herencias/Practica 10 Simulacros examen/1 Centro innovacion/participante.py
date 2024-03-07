from abc import ABC, abstractmethod

class Participante(ABC):
    def __init__(self,nombre,identificacion,rol):
        self._nombre = nombre
        self._identificacion = identificacion
        self._rol = rol

    def __str__(self):
        print(f"Nombre: {self._nombre} ID: {self._identificacion} Rol: {self._rol}")

    @abstractmethod
    def mostrarinfo():
        pass