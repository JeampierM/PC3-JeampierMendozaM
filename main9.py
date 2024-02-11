from Problema9 import suma, resta, producto, division

def main():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            while b == 0:
                print("Error: No es posible dividir entre cero")
                b = float(input("Ingrese un segundo número diferente de cero: "))

            print(f"Suma: {suma(a, b)}")

            print(f"Resta: {resta(a, b)}")

            print(f"Producto: {producto(a, b)}")

            print(f"División: {division(a, b)}")

            break  

        except ValueError:
            print("Error: Ingrese solo números")

if __name__ == '__main__':
    main()

