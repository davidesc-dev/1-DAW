### EXAMEN B UNIDAD 4 DAVID ESCUTIA DE HARO ####

### IMPORTACION DE LAS CLASES ####
from entidad import *
from empresa import *
from emprendedor import *
from startup import *

### CLASE PRINCIPAL ####
class ParqueTecnologico():
    ### CONSTRUCTOR ####
    def __init__(self):
        self.entidades = {}

    def registrar_entidad(self):
        crear = int(input("Seleccione entidad a crear (1->Emprendedor/2->Empresa/3->Startup): "))
        if crear == 1:
            nombre = input("Nombre: ")
            sector = input("Sector: ")
            incorporacion = input("Año de incorporación: ")
            habilidades = []
            emprendedor = Emprendedor(nombre,sector,incorporacion,habilidades)
            self.entidades[nombre] = emprendedor

        elif crear == 2:
            nombre = input("Nombre: ")
            sector = input("Sector: ")
            incorporacion = input("Año de incorporación: ")
            numero_empleados = int(input("Numero de empleados de la empresa: "))
            empresa = Empresa(nombre,sector,incorporacion,numero_empleados)
            self.entidades[nombre] = empresa

        elif crear == 3:
            nombre = input("Nombre: ")
            sector = input("Sector: ")
            incorporacion = input("Año de incorporación: ")
            inversion_recibida = float(input("Inversion a dar: "))
            startup = Startup(nombre,sector,incorporacion,inversion_recibida)
            self.entidades[nombre] = startup
        else:
            print("Opcion incorrecta")

    def eliminar_entidad(self):
        busqueda = input("Introduzca nombre de la entidad a eliminar: ")
        if busqueda not in self.entidades.keys():
            print("Entidad no encontrada")
        elif busqueda in self.entidades.keys():
            del self.entidades[busqueda]
            print(f"Entidad {busqueda} eliminada correctamente")

    def mostrar_entidades(self):
        print("Emprendedores:")
        for objeto in self.entidades.values():
            if objeto.__class__.__name__ == "Emprendedor":
                print(f" - Nombre: {objeto.nombre} Sector: {objeto.sector} Año de incorporacion: {objeto.año_incorporacion}")
        print("\nEmpresas:")
        for objeto in self.entidades.values():
            if objeto.__class__.__name__ == "Empresa":
                print(f" - Nombre: {objeto.nombre} Sector: {objeto.sector} Año de incorporacion: {objeto.año_incorporacion} Nº Trabajadores: {objeto.numero_empleados}")
        print("\nStartups:")
        for objeto in self.entidades.values():
            if objeto.__class__.__name__ == "Startup":
                print(f" - Nombre: {objeto.nombre} Sector: {objeto.sector} Año de incorporacion: {objeto.año_incorporacion} Inversion recibida: {objeto.inversion_recibida}€")

    def buscar_entidad(self):
        encontrado = False
        busqueda = input("Escriba el nombre de la entidad a buscar: ")
        for valor in self.entidades.values():
            if (valor.nombre) == busqueda:
                encontrado = True
        if encontrado:
            print(f"Nombre: {valor.nombre} Sector: {valor.sector} Año de incorporación: {valor.año_incorporacion} Tipo: {valor.__class__.__name__}")
        else:
            print(f"Entidad {busqueda} no encontrada")

    def filtrar_entidades_por_sector(self):
        busqueda = input("Escriba el nombre del sector por el cual filtrar: ")
        for valor in self.entidades.values():
            if (valor.sector) == busqueda:
                print(f"Nombre: {valor.nombre} Sector: {valor.sector} Año de incorporación: {valor.año_incorporacion} Tipo: {valor.__class__.__name__}")
        else:
            print(f"No hay nada perteneciente al sector {busqueda}")

    def actualizar_datos_entidad(self):
        pass

### FUNCIONES DE MENU ####
    def mostrar_menu(self):
        print("\n--MENU PRINCIPAL--")
        print("1. Registrar entidad")
        print("2. Eliminar entidad")
        print("3. Mostrar entidades")
        print("4. Buscar entidad")
        print("5. Filtrar entidades por sector")
        print("0. Salir del programa")
        opcion = int(input("Introduzca una opcion: "))
        return opcion

    def ejecutar(self,opcion):
        if opcion == 1:
            self.registrar_entidad()
        elif opcion == 2:
            self.eliminar_entidad()
        elif opcion == 3:
            self.mostrar_entidades()
        elif opcion == 4:
            self.buscar_entidad()
        elif opcion == 5:
            self.filtrar_entidades_por_sector()
        elif opcion == 0:
            print("Saliendo...")
            exit()
        else:
            print("Opcion no especificada")

    def iniciar(self):
        while True:
            opcion = self.mostrar_menu()
            self.ejecutar(opcion)


### PROGRAMA PRINCIPAL ####
if __name__ == "__main__":
    parque = ParqueTecnologico()
    parque.iniciar()