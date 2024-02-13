### CLASES ####
class CuentaBancaria(object):
    def __init__(self,iban,saldo,interesAnualBasico):
        self.iban = iban
        self.saldo = saldo
        self.interesAnualBasico = interesAnualBasico
        print(f"La cuenta con iban:{self.iban} fue dada de alta correctamente")

    def getnumeroCuenta(self):
        print(f"Nº de cuenta: {self.iban}")

    def getSaldo(self):
        print(f"Saldo de la cuenta: {self.saldo}€")

    def ingresar(self):
        ingreso = float(input("Cuanto desea ingresar: "))
        self.saldo += ingreso
        print(f"Ingreso efectuado correctamente, ahora el sald cuenta es de {self.saldo}€")

    def retirar(self):
        retirada = float(input("Cuanto desea retirar: "))
        self.saldo -= retirada
        print(f"Retirada efectuada correctamente, ahora el saldo de la cuenta es de {self.saldo}€")

    def traspaso(self,acc2):
        añadir = float(input("Cuanto dinero desea traspasar: "))
        self.saldo -= añadir
        acc2.saldo += añadir
        print(f"El traspaso de {añadir}€ se ha efectuado correctamente a la cuenta con iban: {acc2.iban}")

    def calcularIntereses():
        print("ola cocacola")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, iban, saldo, interesAnualBasico):
        super().__init__(iban, saldo, interesAnualBasico)
    
    def calcularIntereses():
        print("ola caracola")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, iban, saldo, interesAnualBasico,saldoMinimo):
        super().__init__(iban, saldo, interesAnualBasico)
        self.saldoMinimo = saldoMinimo
    
    def calcularIntereses():
        print("ola caracola")


### FUNCIONES ####
def menu():
    opcion = int(input("Introduzca una opcion: "))
    while True:
        if opcion == 1:
            iban

def main():
    menu()
    cuenta1 = CuentaCorriente(221213312,200,2)
    cuenta2 = CuentaCorriente(894789456,50,2)
    cuenta1.getSaldo()
    cuenta2.getSaldo()
    cuenta1.traspaso(cuenta2)
    cuenta1.getSaldo()
    cuenta2.getSaldo()
    cuenta1.ingresar()
    cuenta1.getSaldo()
    cuenta1.ingresar()
    cuenta1.getSaldo()
    cuenta1.ingresar()

### PROGRAMA PRINCIPAL ####
if __name__ == "__main__":
        main()

