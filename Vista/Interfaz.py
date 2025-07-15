import tkinter as tk
from tkinter import messagebox
from Controlador.Gestor import GestorSistema
from Modelo.Fabrica_producto import ProductoFactory

class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE VENTAS - Control de Stock y Ventas")
        self.root.geometry("400x400")

        self.gestor = GestorSistema()

        self.crear_menu()

    def crear_menu(self):
        label = tk.Label(self.root, text="Menú Principal", font=("Arial", 16))
        label.pack(pady=20)

        btn_agregar = tk.Button(self.root, text="Agregar Producto", width=25, command=self.ventana_agregar_producto)
        btn_listar = tk.Button(self.root, text="Listar Productos", width=25, command=self.listar_productos)
        btn_vender = tk.Button(self.root, text="Realizar Venta", width=25, command=self.ventana_realizar_venta)
        btn_historial = tk.Button(self.root, text="Ver Historial de Ventas", width=25, command=self.mostrar_historial)

        btn_agregar.pack(pady=5)
        btn_listar.pack(pady=5)
        btn_vender.pack(pady=5)
        btn_historial.pack(pady=5)

    def ventana_agregar_producto(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        tk.Label(ventana, text="Precio:").grid(row=1, column=0)
        tk.Label(ventana, text="Cantidad:").grid(row=2, column=0)

        entry_nombre = tk.Entry(ventana)
        entry_precio = tk.Entry(ventana)
        entry_cantidad = tk.Entry(ventana)

        entry_nombre.grid(row=0, column=1)
        entry_precio.grid(row=1, column=1)
        entry_cantidad.grid(row=2, column=1)

        def agregar():
            try:
                nombre = entry_nombre.get()
                precio = float(entry_precio.get())
                cantidad = int(entry_cantidad.get())

                producto = ProductoFactory.crear_producto("generico", nombre, precio, cantidad)
                self.gestor.agregar_producto(producto)
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Agregar", command=agregar).grid(row=3, column=0, columnspan=2, pady=10)

    def listar_productos(self):
        productos = self.gestor.listar_productos()
        if not productos:
            messagebox.showinfo("Inventario", "No hay productos registrados.")
            return
        ventana = tk.Toplevel(self.root)
        ventana.title("Productos en Stock")

        for i, prod in enumerate(productos):
            tk.Label(ventana, text=str(prod)).pack(anchor="w", padx=10)

    def ventana_realizar_venta(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Realizar Venta")

        tk.Label(ventana, text="Nombre del producto:").grid(row=0, column=0)
        tk.Label(ventana, text="Cantidad:").grid(row=1, column=0)

        entry_nombre = tk.Entry(ventana)
        entry_cantidad = tk.Entry(ventana)

        entry_nombre.grid(row=0, column=1)
        entry_cantidad.grid(row=1, column=1)

        def vender():
            try:
                nombre = entry_nombre.get()
                cantidad = int(entry_cantidad.get())
                venta = self.gestor.realizar_venta([{"nombre": nombre, "cantidad": cantidad}])
                messagebox.showinfo("Venta realizada", str(venta))
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error en la venta", str(e))

        tk.Button(ventana, text="Vender", command=vender).grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_historial(self):
        historial = self.gestor.ver_historial_ventas()
        if not historial:
            messagebox.showinfo("Historial", "Aún no hay ventas registradas.")
            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Historial de Ventas")

        for venta in historial:
            tk.Label(ventana, text=str(venta)).pack(anchor="w", padx=10, pady=2)
