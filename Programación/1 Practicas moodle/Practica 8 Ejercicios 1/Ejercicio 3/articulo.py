class Articulo:
    def __init__(self,nombre,precio,iva,stock):
        self.nombre = nombre
        self.precio = precio
        self.iva = 21
        self.stock = stock

    def __str__(self):
        return f"--{self.nombre}--\n  └📁 Precio: {self.precio}€ - IVA: {self.iva}% - PVP: {(self.precio + (self.precio * self.iva / 100))}€\n  └📁 Stock: {self.stock} uds.\n"
    
pijama = Articulo("Pijama",10,0,100)
cepillo = Articulo("Cepillo de dientes",2,0,213)

print(pijama)
print(cepillo)