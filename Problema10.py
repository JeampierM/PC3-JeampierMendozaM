from math import pi
from Problema3 import Circulo
from Problema4 import Rectangulo

def ingresar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: No se permiten valores negativos, ingrese de nuevo")
                continue
            return valor
        except ValueError:
            print("Error: Por favor, asegúrese de ingresar un valor numérico")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Digite una opcion: ")

        if opcion == '1':
            radio_ingresado = ingresar_numero("Ingrese el radio del círculo: ")
            mi_circulo = Circulo(radio_ingresado)
            area_del_circulo = mi_circulo.calcular_area()
            print(f"El área del círculo es: {area_del_circulo}")

        elif opcion == '2':
            largo_ingresado = ingresar_numero("Ingrese el largo del rectángulo: ")
            ancho_ingresado = ingresar_numero("Ingrese el ancho del rectángulo: ")
            mi_rectangulo = Rectangulo(largo_ingresado, ancho_ingresado)
            area_del_rectangulo = mi_rectangulo.calcular_area()
            print(f"El área del rectángulo es: {area_del_rectangulo}")

        elif opcion == '3':
            lado_cuadrado = ingresar_numero("Ingrese el lado del cuadrado: ")
            area_del_cuadrado = lado_cuadrado ** 2
            print(f"El área del cuadrado es: {area_del_cuadrado}")

        elif opcion == '4':
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4")

if __name__ == '__main__':
    menu()
