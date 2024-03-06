empleadosempresa = []

class Empleados:

    def __init__(self, nombre, dni, sueldo_bruto, edad, telefono, direccion):

        self.nombre = nombre
        self.dni = dni
        self.sueldobruto = sueldo_bruto
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):

        return f"Empleado: {self.nombre}"
    
    def introducirEmpleados(self):

        if self.nombre not in empleadosempresa:

            empleadosempresa.append(self.nombre)

            print(empleadosempresa)
    

    def mostrarInfo(self):

        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Sueldo Bruto: {self.sueldobruto}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")

    def sueldoNeto(self):

        if self.sueldobruto < 12000:

            self.sueldobruto = (self.sueldobruto * 20) / 100

            print(f"El sueldo neto del empleado es: {self.sueldobruto}€")

        elif self.sueldobruto >= 12000 and self.sueldobruto <= 25000:

            self.sueldobruto = (self.sueldobruto * 30) / 100

            print(f"El sueldo neto del empleado es: {self.sueldobruto}€")

        elif self.sueldobruto > 25000:

            self.sueldobruto = (self.sueldobruto * 40) / 100

            print(f"El sueldo neto del empleado es: {self.sueldobruto}€")

    def mostrarTodo(self):

        for i in empleadosempresa:

            print(f"Nombre: {self.nombre}")
            print(f"DNI: {self.dni}")
            print(f"Sueldo Bruto: {self.sueldobruto}")
            print(f"Edad: {self.edad}")
            print(f"Teléfono: {self.telefono}")
            print(f"Dirección: {self.direccion}")





class Empresas(Empleados):

    def __init__(self, nombre, cif, telefono, direccion, empleados):

        self.nombre = nombre
        self.cif = cif
        self.telefono = telefono
        self.direccion = direccion
        self.empleados = empleados

    def __str__(self):

        return f"Nombre: {self.nombre}"

    def agregarEliminar(self):

        agregaroeliminar = ""

        while agregaroeliminar != "000":

            agregaroeliminar = input("¿Que desea agregar un empleado o eliminar uno? (agregar/eliminar) [000 - Salir]: ")

            print()

            if len(empleadosempresa) == 0 and agregaroeliminar == "eliminar":

                print("[ERROR] - Tu empresa no contiene empleados.")

                break

            if agregaroeliminar == "agregar":

                empleado = input("Nombre Empleado: ")

                if empleado not in empleadosempresa:

                    empleadosempresa.append(empleado)

                    print("Empleado agregado satisfactoriamente --> ", empleadosempresa)

            elif agregaroeliminar == "eliminar":

                empleadoeliminar = input("¿Que empleado desea eliminar?: ")

                for i in empleadosempresa:

                    if empleadoeliminar == i:

                        empleadosempresa.remove(i)

                        print("Empleado eliminado satisfactoriamente --> ", empleadosempresa)

    def mostrarTodo(self):
        return super().mostrarTodo()

        

## PRUEBAS ###
    
empleados = Empleados

empleado1 = Empleados("David", "5252351G", 15000, 19, 675892345, "Sector 7")

empleado2 = Empleados("Ernestoa", "5252351G", 3000, 23, 675615814, "Calle 18")

empleado1.introducirEmpleados()

empleado2.introducirEmpleados()

empresa = Empresas

empresa1 = Empresas("Dvix CORP", 341, 666666666, "Calle 123", 0)

empresa1.agregarEliminar()

empleado1.mostrarTodo()