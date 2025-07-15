from Modelo.Fabrica_producto import ProductoFactory
from Controlador.Gestor import GestorSistema
import tkinter as tk
from Vista.Interfaz import InterfazApp
from Utils.Decorator import ReporteProductos, ReporteConTotal

gestor = GestorSistema()

# Crear productos
p1 = ProductoFactory.crear_producto("generico", "Lapicera", 120.0, 50)
p2 = ProductoFactory.crear_producto("generico", "Cuaderno", 500.0, 30)

gestor.agregar_producto(p1)
gestor.agregar_producto(p2)

# Listar productos
print(" Productos en inventario:")
for prod in gestor.listar_productos():
    print(prod)

# Realizar una venta
venta = gestor.realizar_venta([
    {"nombre": "Lapicera", "cantidad": 2},
    {"nombre": "Cuaderno", "cantidad": 1}
])

print("\n Venta realizada:")
print(venta)

# Ver stock actualizado
print("\n Stock después de la venta:")
for prod in gestor.listar_productos():
    print(prod)

# Ver historial de ventas
print("\n Historial de ventas:")
for v in gestor.ver_historial_ventas():
    print(v)

productos = gestor.listar_productos()

# Reporte simple
reporte_base = ReporteProductos(productos)

# Decoramos con total
reporte_con_total = ReporteConTotal(reporte_base, productos)

print(reporte_con_total.generar())

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()
