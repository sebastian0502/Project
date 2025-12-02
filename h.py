class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_inventario(self):
        return self.precio * self.cantidad

    def agregar_inventario(self, cantidad):
        print("Aumenta la cantidad del producto en el inventario")
        self.cantidad += cantidad
        print(f"La nueva cantidad será: {self.cantidad}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Electronica(Producto):
    def __init__(self, nombre, precio, cantidad, garantia, marca):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia
        self.marca = marca

    def aplicar_descuento(self, porcentaje):
        descuento = (porcentaje / 100) * self.precio
        self.precio -= descuento
        print(f"Nuevo precio: {self.precio}")

    def __str__(self):
        return (f"""Electronico: {self.nombre},
              Precio: {self.precio} soles,
              Cantidad: {self.cantidad},
              Garantia: {self.garantia} años,
              Marca: {self.marca}
              """)


class Alimentos(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

    def aplicar_descuento(self, porcentaje):
        descuento = (porcentaje / 100) * self.precio
        self.precio -= descuento # Corrección aquí también
        print(f"Nuevo precio: {self.precio}")

    def __str__(self):
        return (f"""Alimento: {self.nombre},
              Precio: {self.precio},
              Cantidad: {self.cantidad},
              Fecha de vencimiento: {self.fecha_vencimiento}
              """)


producto1 = Electronica("Celular", 4000, 1, 4, "Samsung")
producto2 = Alimentos("Cereales", 4, 2, "27-12-2025")

producto1.agregar_inventario(10)
producto2.agregar_inventario(20)

producto1.aplicar_descuento(10)

print(producto1)
print(f"Valor de inventario: {producto1.valor_inventario()}")

print(producto2)
print(f"Valor de inventario: {producto2.valor_inventario()}")
