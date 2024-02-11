class Producto:
    def __init__(self, nombre, marca, modelo, año, precio):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"""\
Nombre: {self.nombre}
Marca: {self.marca}
Modelo: {self.modelo}
Año: {self.año}
Precio: ${self.precio:.2f}
"""

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_catalogo(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Catálogo de productos:")
            print("-------------------------")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No hay productos para el año {año}.")
        else:
            print(f"Productos para el año {año}:")
            for producto in productos_filtrados:
                print(producto)

def main():
    catalogo = Catalogo()

    try:
        # Agregando productos al catálogo
        producto1 = Producto("Batería", "Energizer", "ABC123", 2022, 120.0)
        producto2 = Producto("Filtro de Aceite", "ACDelco", "XYZ456", 2021, 15.5)
        producto3 = Producto("Pastillas de Freno", "Brembo", "123DEF", 2022, 50.0)

        catalogo.agregar_producto(producto1)
        catalogo.agregar_producto(producto2)
        catalogo.agregar_producto(producto3)

        catalogo.mostrar_catalogo()

        # Filtrando por año
        año_filtro = int(input("Ingrese el año para filtrar productos: "))
        print(f"\nFiltrando productos para el año {año_filtro}:")
        catalogo.filtrar_por_año(año_filtro)

    except ValueError:
        print("Error: Ingrese un año válido como un número entero.")

if __name__ == "__main__":
    main()
