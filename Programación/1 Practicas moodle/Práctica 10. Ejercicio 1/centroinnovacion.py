from investigador import Investigador
from empresa import Empresa
from proyecto import Proyecto

class CentroInnovacion:
    def __init__(self):
        self.proyectos = {}
        self.participantes = {}
        self.empresas = {}

    def registrar_investigador_empresa(self):
        tipo = input("¿Desea registrar un investigador o una empresa? (I/E): ")
        nombre = input("Nombre: ")
        if tipo.upper() == 'I':
            identificacion = input("Identificación: ")
            rol = input("Rol: ")
            especialidad = input("Especialidad: ")
            investigador = Investigador(nombre, identificacion, rol, especialidad)
            self.participantes[identificacion] = investigador
        elif tipo.upper() == 'E':
            sector = input("Sector: ")
            empresa = Empresa(nombre, sector)
            self.empresas[nombre] = empresa

    def crear_proyecto(self):
        titulo = input("Título del proyecto: ")
        area_investigacion = input("Área de investigación: ")
        proyecto = Proyecto(titulo, area_investigacion)
        self.proyectos[titulo] = proyecto

    def asignar_a_proyecto(self):
        identificacion = input("Identificación del investigador: ")
        titulo_proyecto = input("Título del proyecto: ")
        if identificacion in self.participantes and titulo_proyecto in self.proyectos:
            investigador = self.participantes[identificacion]
            proyecto = self.proyectos[titulo_proyecto]
            proyecto.agregar_participante(investigador)

    def actualizar_proyecto(self):
        titulo = input("Título del proyecto: ")
        nuevo_estado = input("Nuevo estado del proyecto: ")
        if titulo in self.proyectos:
            proyecto = self.proyectos[titulo]
            proyecto.actualizar_estado(nuevo_estado)

    def ver_proyectos(self):
        for titulo, proyecto in self.proyectos.items():
            print(f"{titulo} - {proyecto.estado}")

    def mostrar_menu(self):
        print("1. Registrar Investigador/Empresa")
        print("2. Crear Proyecto")
        print("3. Asignar a Proyecto")
        print("4. Actualizar Proyecto")
        print("5. Ver Proyectos")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        return opcion

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.registrar_investigador_empresa()
        elif opcion == 2:
            self.crear_proyecto()
        elif opcion == 3:
            self.asignar_a_proyecto()
        elif opcion == 4:
            self.actualizar_proyecto()
        elif opcion == 5:
            self.ver_proyectos()
        elif opcion == 6:
            print("Saliendo del programa...")
            exit()

    def iniciar(self):
        while True:
            opcion = self.mostrar_menu()
            self.ejecutar_opcion(opcion)


# Uso de la clase
if __name__ == "__main__":
    centro_innovacion = CentroInnovacion()
    centro_innovacion.iniciar()
