import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return round(area, 3)

def main():
    while True:
        try:
            radio_ingresado = float(input("Ingrese el radio del círculo: "))
            
            if radio_ingresado < 0:
                print("Error: El radio no puede ser negativo. Intente de nuevo")
            else:
                break  

        except ValueError:
            print("Error: Por favor, asegúrese de ingresar un valor numérico para el radio")

    mi_circulo = Circulo(radio_ingresado)
    area_del_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo es: {area_del_circulo}")

if __name__ == '__main__':
    main()
