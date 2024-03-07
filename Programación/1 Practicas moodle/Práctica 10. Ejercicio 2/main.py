from espacio import *
from gestor import *
from reserva import *
from usuario import *

opcion="1"
gestor_reservas=Gestor()

def menu():
    print('''Bienvenido al programa gestor de reservas
          Características a ejecutar :
          1 - Registrar Usuario
          2 - Mostrar Usuarios
          3 - Crear un Espacio
          4 - Mostrar Espacios
          5 - Crear Reserva
          6 - Mostrar Reservas
          7 - Dar de baja Reserva
          0 - Salir ''')


def main():
    global opcion
    while opcion != "0" :
        menu()
        opcion=input("Introduzca la opcion que desea ejecutar : ")

        if opcion=="1":
            print("Ha elegido registrar un usuario")
            nombre=str(input("Introduzca el nombre de usuario a registrar : "))
            email=str(input("Introduzca el email del usuario : "))
            telefono=int(input("Introduzca el teléfono del usuario : "))
            usuario=Usuario(nombre,email,telefono)
            gestor_reservas.registrar_usuario(usuario)

        elif opcion=="2":
            gestor_reservas.getUsuarios()

        elif opcion=="3":
            print("Solo añadir un espacio cuando está disponible.")
            identificador=input("Introduzca el Identificador asociado al Espacio : ")
            tipo=(input("Introduzca el tipo de espacio : "))
            capacidad=int(input("Introduzca la capacidad del espacio : "))
            disponibilidad=True
            espacio=Espacio(identificador,tipo,capacidad,disponibilidad)
            gestor_reservas.añadir_espacio(espacio)

        elif opcion=="4":
            gestor_reservas.getEspacios()

        elif opcion=="5":
            print("IMPORTANTE : El usuario es el email.")
            print("Tiene que introducir tambien el ID del Espacio!")
            usuario=input("Introduzca el usuario : ")
            espacio=input("Introduzca el espacio : ")
            fecha=input("Introduzca la fecha (dia): ")
            hora=input("Introduzca la hora : ")
            duracion=input("Introduzca la duracion : ")
            reserva=Reserva(usuario,espacio,fecha,hora,duracion)
            gestor_reservas.añadir_reserva(reserva)

        elif opcion=="6":
            gestor_reservas.getReservas()

        elif opcion=="7":
            print("IMPORTANTE : El usuario es el email.")
            print("Tiene que introducir tambien el ID del Espacio!")
            usuario=input("Introduzca el usuario : ")
            espacio=input("Introduzca el espacio : ")
            fecha=input("Introduzca la fecha (dia): ")
            hora=input("Introduzca la hora : ")
            gestor_reservas.cancelar_reserva(usuario,espacio,fecha,hora)

        elif opcion=="0":
            print("Gracias por usar el programa.")
        else :
            print("Ha introducido una opción no válida, por favor vuelve a intentarlo o introduzca 0 para salir.")
if __name__=="__main__":
    main()