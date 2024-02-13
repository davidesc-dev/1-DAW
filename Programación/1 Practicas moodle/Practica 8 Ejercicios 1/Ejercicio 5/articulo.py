class Articulo:
    def __init__(self,nombre,precio,iva,stock):
        self.nombre = nombre
        self.precio = precio
        self.iva = 21
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio}€ - IVA: {self.iva}% - PVP: {(self.precio + (self.precio * self.iva / 100))}€ - Stock: {self.stock} uds."
    
    def get_info(self):
        print(f"--{self.nombre}--\n  └📁 Precio: {self.precio}€ - IVA: {self.iva}%\n  └📁 Stock: {self.stock} uds.\n")

    def get_pvp(self):
        print(f"PVP: {(self.precio + (self.precio * self.iva / 100))}€")

    def get_pvp_descuento(self):
        descuento = int(input("Introduzca un descuento para el articulo: "))
        pvp = (self.precio + (self.precio * self.iva / 100))
        descuento = (pvp*(descuento/100))
        print(f"Precio: {pvp}€\nDescuento: {descuento}€\n-----------------\nTotal: {pvp-descuento}€")


    # def sell(self):

        
    # def store(self):



pijama = Articulo("Pijama",10,0,100)
cepillo = Articulo("Cepillo de dientes",2,0,213)

pijama.get_pvp_descuento()