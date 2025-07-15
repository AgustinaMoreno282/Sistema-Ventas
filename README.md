## 📟 SISTEMA DE VENTAS– Sistema de Stock y Ventas

Aplicación de escritorio para el control de stock y ventas en una pequeña empresa, desarrollada en Python con Tkinter y Programación Orientada a Objetos.
Incluye patrones de diseño y principios SOLID para asegurar escalabilidad y mantenibilidad.

---

### 🛠️ Tecnologías Usadas

* Python 3.10+
* Tkinter (GUI)
* POO (Programación Orientada a Objetos)
* Principios SOLID
* Patrones de diseño: Factory, Decorator, Observer

---

### 📦 Funcionalidades

* ✅ Agregar productos al inventario
* ✅ Listar productos disponibles
* ✅ Realizar ventas (con actualización automática de stock)
* ✅ Ver historial de ventas
* ✅ Generar reportes del inventario con valor total

---

### 🧐 Patrones de Diseño Implementados

| Patrón        | Descripción                                                           |
| ------------- | --------------------------------------------------------------------- |
| **Factory**   | Crea objetos `Producto` mediante `ProductoFactory`.                   |
| **Decorator** | Agrega funciones extra a los reportes sin modificar su clase base.    |
| **Observer**  | `Inventario` notifica a observadores cuando hay cambios en productos. |

---

### 🧱 Principios SOLID Aplicados

| Principio | Aplicación                                                                     |
| --------- | ------------------------------------------------------------------------------ |
| **S**     | Cada clase tiene una única responsabilidad clara.                              |
| **O**     | El sistema es fácilmente extensible sin modificar código existente.            |
| **L**     | Preparado para subclases sin romper funcionalidad (ej. productos específicos). |
| **I**     | Clases pequeñas y enfocadas, sin métodos innecesarios.                         |
| **D**     | Módulos de alto nivel no dependen de módulos de bajo nivel directamente.       |

---

### 📁 Estructura del Proyecto

```
sistema_ventas/
│
├── Main.py                       # Punto de entrada
├── Modelo/                       # Lógica del dominio
│   ├── Producto.py
│   ├── Venta.py
│   ├── Fabrica_producto.py
│   └── Inventario.py
├── Controlador/
│   └── Gestor.py                 # Lógica del sistema
├── Vista/
│   └── Interfaz.py               # Interfaz gráfica (Tkinter)
├── Utils/                        # Herramientas y patrones
    ├── Decorator.py
    └── Observer.py
```

---

### ▶️ Cómo Ejecutar

1. Asegurate de tener Python 3.10 o superior instalado.
2. Cloná el repositorio o descargá el proyecto.
3. Ejecutá desde la raíz:

python Main.py

