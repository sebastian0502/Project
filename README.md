# Sistema de Gestión de Inventario (Python POO)

Este proyecto es una implementación práctica de un **Sistema de Inventario** utilizando **Python** y los principios fundamentales de la **Programación Orientada a Objetos (POO)**.

El script simula la gestión de diferentes tipos de productos (Electrónica y Alimentos) con comportamientos específicos y compartidos.

## Conceptos Implementados

Este código demuestra el dominio de los siguientes conceptos:

* **Herencia:** Clases hijas (`Electronica`, `Alimentos`) que heredan atributos y métodos de una clase padre (`Producto`).
* **Polimorfismo:** Implementación personalizada del método `__str__` y `aplicar_descuento` para comportarse de forma distinta según el tipo de producto.
* **Encapsulamiento:** Uso de `self` y gestión de estado interno de los objetos.
* **Reutilización de Código:** Uso de `super().__init__` para optimizar los constructores.

## Estructura de Clases

### 1. Clase Padre: `Producto`
Define la estructura base para cualquier ítem del inventario.
* **Atributos:** `nombre`, `precio`, `cantidad`.
* **Métodos:**
    * `valor_inventario()`: Calcula el valor total (Precio × Cantidad).
    * `agregar_inventario()`: Aumenta el stock.

### 2. Clase Hija: `Electronica`
Extiende la funcionalidad para productos tecnológicos.
* **Atributos extra:** `garantia`, `marca`.
* **Métodos:** Aplica descuentos directos al precio base.

### 3. Clase Hija: `Alimentos`
Extiende la funcionalidad para productos perecederos.
* **Atributos extra:** `fecha_vencimiento`.

## Ejecución

No se requieren librerías externas. Solo necesitas tener Python instalado.

1. **Clonar el repositorio** (o descargar el archivo):
   ```bash
   git clone [https://github.com/tu-usuario/sistema-inventario-python.git](https://github.com/tu-usuario/sistema-inventario-python.git)
