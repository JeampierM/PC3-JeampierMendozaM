class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

def main():
    while True:
        try:
            largo_ingresado = float(input("Ingrese el largo del rectángulo: "))
        
            if largo_ingresado < 0:
                print("Error: El largo no puede ser negativo. Intente nuevamente.")
                continue  

            ancho_ingresado = float(input("Ingrese el ancho del rectángulo: "))
           
            if ancho_ingresado < 0:
                print("Error: El ancho no puede ser negativo. Intente nuevamente.")
                continue  

            mi_rectangulo = Rectangulo(largo_ingresado, ancho_ingresado)

            area_del_rectangulo = mi_rectangulo.calcular_area()
            print(f"El área del rectángulo es: {area_del_rectangulo}")

            break

        except ValueError:
            print("Por favor, asegúrese de ingresar valores numéricos para el largo y el ancho.")

if __name__ == '__main__':
    main()
