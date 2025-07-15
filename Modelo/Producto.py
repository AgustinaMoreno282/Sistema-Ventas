class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def reducir_stock(self, cantidad_vendida: int):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
        else:
            raise ValueError("Stock insuficiente")

    def aumentar_stock(self, cantidad_agregada: int):
        self.cantidad += cantidad_agregada

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.cantidad}"
