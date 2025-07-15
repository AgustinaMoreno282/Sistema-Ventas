from Modelo.Producto import Producto

class ProductoFactory:
    @staticmethod
    def crear_producto(tipo: str, nombre: str, precio: float, cantidad: int) -> Producto:
        # En el futuro podrías tener diferentes clases: Alimento, Ropa, Electrónico, etc.
        if tipo == "generico":
            return Producto(nombre, precio, cantidad)
        else:
            raise ValueError(f"Tipo de producto desconocido: {tipo}")