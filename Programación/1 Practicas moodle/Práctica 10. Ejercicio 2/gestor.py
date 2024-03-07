class Gestor():

    def __init__(self):
        self.usuarios = {}
        self.reservas = []
        self.espacios = []

    def registrar_usuario(self,objeto):
        repetido=0
        for i in self.usuarios:
            if objeto.email==i :
                repetido+=1
        if repetido==0:
            self.usuarios[objeto.email]=objeto
            print("Usuario añadido con exito.")
        else :
            print("El usuario ya existe, volviendo.")

    def getUsuarios(self):
         print(self.usuarios)

    def añadir_espacio(self,objeto):
        repetido=0
        for i in self.espacios :
            if i.identificador == objeto.identificador :
                repetido+=1
        if repetido == 0 :
            self.espacios.append(objeto)
            print("Espacio añadido con exito.")
        else :
            print("El espacio ya existe, volviendo.")

    def getEspacios(self):
        for i in self.espacios:
            print(i)

    def añadir_reserva(self,objeto):
        if objeto.usuario in self.usuarios:
            print("Usuario confirmado.")
            for i in self.espacios :
                if i.identificador == objeto.espacio:
                    print("Sitio Confirmado.")
                    if i.getDisponibilidad()==True:
                        self.reservas.append(objeto)
                        print("Reservado con exito.")
                        i.reservar()
                        print("Por favor, si va a cancelar hágalo con tiempo.")
                    else:
                        print("Lo siento ya está reservado")   
                else:
                    print("Lo siento el sitio no existe.")   
        else:
            print("Lo siento el usuario no existe.")

    def getReservas(self):
        for i in self.reservas:
            print(i)

    def cancelar_reserva(self,usuario,espacio,fecha,hora) : 
        for i in self.reservas:
            if i.usuario == usuario:
                if i.espacio == espacio:
                    if i.fecha == fecha:
                        if i.hora == hora :
                            self.reservas.remove(i)
                            print("Reserva Anulada")
                            for i in self.espacios:
                                if i.identificador==espacio:
                                    i.cancelar_reserva()
                                print("Reserva cancelada")
                        else:
                            print("Lo siento en esa hora no existe reserva")
                    else:
                        print("Lo siento en esa fecha no existe reserva")   
                else:
                    print("Lo siento en ese sitio no existe reserva.")   
            else:
                print("Lo siento el usuario no tiene asignada ninguna reserva.")