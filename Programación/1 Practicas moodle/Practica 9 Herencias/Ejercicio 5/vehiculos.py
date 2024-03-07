from abc import ABC, abstractmethod

vehiculos = []

def agregar_vehiculo(vehiculo):
    vehiculos.append(vehiculo)

def imprimir_todo():
    for vehiculo in vehiculos:
        vehiculo.imprimir()

class Vehiculo(ABC):
    def __init__(self, matricula, modelo):
        self.__matricula = matricula
        self.__modelo = modelo

    def get_matricula(self):
        return self.__matricula

    def get_modelo(self):
        return self.__modelo

    @abstractmethod
    def imprimir(self):
        pass

class VehiculoTerrestre(Vehiculo):
    def __init__(self, matricula, modelo, numero_ruedas):
        super().__init__(matricula, modelo)
        self.__numero_ruedas = numero_ruedas

    def get_numero_ruedas(self):
        return self.__numero_ruedas

    def imprimir(self):
        pass

class Coche(VehiculoTerrestre):
    def __init__(self, matricula, modelo, numero_ruedas, aire_acondicionado):
        super().__init__(matricula, modelo, numero_ruedas)
        self.__aire_acondicionado = aire_acondicionado

    def get_aire_acondicionado(self):
        return self.__aire_acondicionado

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Nº ruedas: {self.get_numero_ruedas()}, Aire acondicionado: {self.__aire_acondicionado}")

class Moto(VehiculoTerrestre):
    def __init__(self, matricula, modelo, numero_ruedas, color):
        super().__init__(matricula, modelo, numero_ruedas)
        self.__color = color

    def get_color(self):
        return self.__color

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Nº ruedas: {self.get_numero_ruedas()}, Color: {self.__color}")

class VehiculoAcuatico(Vehiculo):
    def __init__(self, matricula, modelo, eslora):
        super().__init__(matricula, modelo)
        self.__eslora = eslora

    def get_eslora(self):
        return self.__eslora

    @abstractmethod
    def imprimir(self):
        pass

class Barco(VehiculoAcuatico):
    def __init__(self, matricula, modelo, eslora, motor):
        super().__init__(matricula, modelo, eslora)
        self.__motor = motor

    def get_motor(self):
        return self.__motor

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Eslora: {self.get_eslora()}, Motor: {self.__motor}")

class Submarino(VehiculoAcuatico):
    def __init__(self, matricula, modelo, eslora, profundidad_maxima):
        super().__init__(matricula, modelo, eslora)
        self.__profundidad_maxima = profundidad_maxima

    def get_profundidad_maxima(self):
        return self.__profundidad_maxima

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Eslora: {self.get_eslora()}, Profundidad máxima: {self.__profundidad_maxima}")

class VehiculoAereo(Vehiculo):
    def __init__(self, matricula, modelo, numero_asientos):
        super().__init__(matricula, modelo)
        self.__numero_asientos = numero_asientos

    def get_numero_asientos(self):
        return self.__numero_asientos

    @abstractmethod
    def imprimir(self):
        pass

class Avion(VehiculoAereo):
    def __init__(self, matricula, modelo, numero_asientos, tiempo_max_vuelo):
        super().__init__(matricula, modelo, numero_asientos)
        self.__tiempo_max_vuelo = tiempo_max_vuelo

    def get_tiempo_max_vuelo(self):
        return self.__tiempo_max_vuelo

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Nº asientos: {self.get_numero_asientos()}, Tiempo máximo de vuelo: {self.__tiempo_max_vuelo}")

class Helicoptero(VehiculoAereo):
    def __init__(self, matricula, modelo, numero_asientos, numero_helices):
        super().__init__(matricula, modelo, numero_asientos)
        self.__numero_helices = numero_helices

    def get_numero_helices(self):
        return self.__numero_helices

    def imprimir(self):
        print(f"Tipo: {self.__class__.__name__} Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Nº asientos: {self.get_numero_asientos()}, Nº hélices: {self.__numero_helices}")