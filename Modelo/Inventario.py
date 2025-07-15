from Utils.Observer import Observable

class Inventario(Observable):
    def __init__(self):
        super().__init__()
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.notificar_observadores()

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            self.notificar_observadores()
            return True
        return False

    def buscar_producto(self, nombre):
        for prod in self.productos:
            if prod.nombre == nombre:
                return prod
        return None

    def listar_productos(self):
        return self.productos
