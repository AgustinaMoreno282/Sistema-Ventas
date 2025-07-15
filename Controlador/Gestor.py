from Modelo.Inventario import Inventario
from Modelo.Venta import Venta

class GestorSistema:
    def __init__(self):
        self.inventario = Inventario()
        self.historial_ventas = []

    def agregar_producto(self, producto):
        self.inventario.agregar_producto(producto)

    def eliminar_producto(self, nombre):
        return self.inventario.eliminar_producto(nombre)

    def listar_productos(self):
        return self.inventario.listar_productos()

    def realizar_venta(self, productos_vendidos: list):
        total = 0
        detalles = []

        for item in productos_vendidos:
            nombre = item['nombre']
            cantidad = item['cantidad']
            producto = self.inventario.buscar_producto(nombre)
            if producto is None:
                raise ValueError(f"Producto no encontrado: {nombre}")
            if producto.cantidad < cantidad:
                raise ValueError(f"Stock insuficiente para {nombre}")
            producto.reducir_stock(cantidad)
            total += producto.precio * cantidad
            detalles.append({'nombre': producto.nombre, 'cantidad': cantidad})

        venta = Venta(detalles, total)
        self.historial_ventas.append(venta)
        return venta

    def ver_historial_ventas(self):
        return self.historial_ventas
