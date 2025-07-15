from Modelo.Fabrica_producto import ProductoFactory
from Controlador.Gestor import GestorSistema
import tkinter as tk
from Vista.Interfaz import InterfazApp
from Utils.Decorator import ReporteProductos, ReporteConTotal

    
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()
