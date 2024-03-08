from entidad import *

class Empresa(Entidad):
    def __init__(self, nombre, sector, año_incorporacion,numero_empleados):
        super().__init__(nombre, sector, año_incorporacion)
        self.numero_empleados = numero_empleados
        self.productos = []

    def agregar_productos(self,producto):
        if producto not in self.productos:
            self.productos.append(producto)
            print(f"El producto {producto} fue añadido correctamente")
        else:
            print(f"El producto {producto} ya se encontraba en la lista")

    def mostrar_productos(self):
        if self.productos.__len__ == 0:
            print("No hay ningun producto, añada alguno primero")
        else:
            print(f"Mostrando {self.productos.__len__} producto(s)")
            for producto in self.productos:
                print(f"  -{producto}")