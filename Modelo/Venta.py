from datetime import datetime

class Venta:
    def __init__(self, productos_vendidos: list, total: float):
        self.productos_vendidos = productos_vendidos
        self.total = total
        self.fecha = datetime.now()

    def __str__(self):
     productos_str = ", ".join([f"{p['nombre']} (x{p['cantidad']})" for p in self.productos_vendidos])
     return f"{self.fecha.strftime('%Y-%m-%d %H:%M:%S')} - Total: ${self.total:.2f} - Productos: {productos_str}"
