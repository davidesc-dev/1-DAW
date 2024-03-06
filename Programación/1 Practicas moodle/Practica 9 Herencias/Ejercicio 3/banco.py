## NOTA ##
'''
En mi codigo he considerado que el IBAN es generado de manera aleatoria y que las cuentas
empiezan con un saldo de 0 hasta que se ingrese o se haga un traspaso de dinero ya que lo
veo algo mas realista.
Tambien para optimizar el código principal, hice que todo fuesen funciones.
'''



### IMPORTAR LIBRERIAS ####
from abc import ABC, abstractmethod
import random


### VARIABLES ####
TIPO_CUENTA = ["",""]
blacklist = []
cuentas = {}
cuentasahorro = []
cuentascorrientes = []


### CLASES ####
class CuentaBancaria(ABC):
    interes_anual_basico = 0.06
    
    def __init__(self, iban, saldo):
        self.iban = iban
        self.saldo = saldo
    
    def consultar_datos(self):
        print("IBAN:", self.iban)
        print(f"Saldo: {self.saldo}€")
    
    def ingresar_dinero(self, cantidad):
        self.añadir(cantidad)
        print(f"Se han ingresado {cantidad}€ en la cuenta {self.iban}.")
    
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No hay suficiente saldo para retirar esa cantidad.")
        else:
            self.añadir(-cantidad)
            print(f"Se han retirado {cantidad}€ de la cuenta {self.iban}.")
    
    def traspasar_dinero(self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            print("No hay suficiente saldo para realizar el traspaso.")
        else:
            self.añadir(-cantidad)
            otra_cuenta.añadir(cantidad)
            print(f"Se han traspasado {cantidad}€ de la cuenta {self.iban} a la cuenta {otra_cuenta.iban}.")
    
    @abstractmethod
    def añadir(self, cantidad):
        pass
    
    @abstractmethod
    def calcular_intereses(self):
        pass


class CuentaCorriente(CuentaBancaria):
    def añadir(self, cantidad):
        self.saldo += cantidad
    
    def calcular_intereses(self):
        intereses = self.saldo * self.interes_anual_basico
        print(f"Los intereses de la cuenta corriente {self.iban} son: {intereses}€.")
        return intereses


class CuentaAhorro(CuentaBancaria):
    saldo_minimo = 1000
    
    def añadir(self, cantidad):
        self.saldo += cantidad
    
    def calcular_intereses(self):
        if self.saldo < self.saldo_minimo:
            intereses = self.saldo * (self.interes_anual_basico / 2)
        else:
            intereses = self.saldo * (self.interes_anual_basico * 2)
        print(f"Los intereses de la cuenta ahorro {self.iban} son: {intereses}€.")
        return intereses
    
### FUNCIONES ####
def menu():
    print("\n---MENU PRINCIPAL---")
    print("   └🚹 1. Abrir una cuenta nueva")
    print("   └🪙  2. Ver el saldo disponible")
    print("   └💵 3. Hacer un ingreso")
    print("   └💸 4. Hacer una retirada")
    print("   └💱 5. Hacer una transferencia a otra cuenta")
    print("   └💰 6. Calcular intereses")
    print("   └🛂 7. (Admin) Mostrar todas las cuentas corrientes")
    print("   └🛂 8. (Admin) Mostrar todas las cuentas de ahorro")
    print("   └🔚 0. Salir")
    
    return input("Seleccione una opción: ")

def crearcuenta():
    while True:
        tipocuenta = input("Introduzca un tipo de cuenta (Corriente/Ahorro): ").strip().lower()
        if tipocuenta == "corriente" or tipocuenta == "ahorro":
            saldo = 0
            while True:
                iban = random.randint(10000000,99999999)
                if iban not in blacklist:
                    blacklist.append(iban)
                    break
            if tipocuenta == "corriente":
                cuentas[iban] = CuentaCorriente(iban, saldo)
                cuentascorrientes.append(cuentas[iban])
                print(f"Su cuenta corriente con iban {iban} ha sido creada exitosamente ✅")
                break
            else:
                cuentas[iban] = CuentaCorriente(iban, saldo)
                cuentasahorro.append(cuentas[iban])
                print(f"Su cuenta ahorro con iban {iban} ha sido creada exitosamente ✅")
                break
        else: 
            print("Introduzca un tipo de cuenta válido o vuelva a intentarlo")

def consultardatos():
    iban = int(input("Ingrese IBAN de la cuenta a consultar: "))
    if iban in cuentas:
        cuentas[iban].consultar_datos()
    else:
        print("No se encontró ninguna cuenta con ese IBAN.")
def ingreso():
    iban = int(input("Ingrese IBAN de la cuenta en la que desea ingresar dinero: "))
    if iban in cuentas:
        cantidad = float(input("Ingrese la cantidad a ingresar: "))
        cuentas[iban].ingresar_dinero(cantidad)
    else:
        print("No se encontró ninguna cuenta con ese IBAN.")

def retirada():
    iban = int(input("Ingrese IBAN de la cuenta de la que desea retirar dinero: "))
    if iban in cuentas:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuentas[iban].retirar_dinero(cantidad)
    else:
        print("No se encontró ninguna cuenta con ese IBAN.")

def transferencia():
    iban_origen = int(input("Ingrese IBAN de la cuenta de origen: "))
    iban_destino = int(input("Ingrese IBAN de la cuenta de destino: "))
    if iban_origen in cuentas and iban_destino in cuentas:
        cantidad = float(input("Ingrese la cantidad a traspasar: "))
        cuentas[iban_origen].traspasar_dinero(cuentas[iban_destino], cantidad)
    else:
        print("No se encontró alguna de las cuentas especificadas.")

def calcularintereses():
    iban = int(input("Ingrese IBAN de la cuenta para calcular intereses: "))
    if iban in cuentas:
        cuentas[iban].calcular_intereses()
    else:
        print("No se encontró ninguna cuenta con ese IBAN.")

def mostrarcuentascorrientes():
    print("---CUENTAS CORRIENTES---")
    print(f"  Nº de cuentas corrientes: {len(cuentascorrientes)}")
    contador = 1
    for cuenta in cuentascorrientes:
        print(f"  └ Cuenta {contador}: {cuenta.iban} - {cuenta.saldo}€")
        contador +=1

def mostrarcuentasahorro():
    print("---CUENTAS AHORRO---")
    print(f"  Nº de cuentas corrientes: {len(cuentasahorro)}")
    contador = 1
    for cuenta in cuentasahorro:
        print(f"  └ Cuenta {contador}: {cuenta.iban} - {cuenta.saldo}€")
        contador +=1