class ReporteBase:
    def generar(self):
        return ""
class ReporteProductos(ReporteBase):
    def __init__(self, productos):
        self.productos = productos

    def generar(self):
        texto = "📦 Reporte de Productos:\n"
        for prod in self.productos:
            texto += f"- {prod.nombre}: {prod.cantidad} unidades - ${prod.precio:.2f}\n"
        return texto

class ReporteDecorator(ReporteBase):
    def __init__(self, componente):
        self._componente = componente

    def generar(self):
        return self._componente.generar()

class ReporteConTotal(ReporteDecorator):
    def __init__(self, componente, productos):
        super().__init__(componente)
        self.productos = productos

    def generar(self):
        reporte = super().generar()
        total = sum(p.precio * p.cantidad for p in self.productos)
        return reporte + f"\n💰 Valor total del inventario: ${total:.2f}\n"
