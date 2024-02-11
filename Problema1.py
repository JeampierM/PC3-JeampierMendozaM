def obtener_porcentaje(f):
    try:
        partes = f.split('/')
        if len(partes) != 2:
            raise ValueError("Formato de fracción incorrecto")

        # Convertiendo las partes a números enteros
        x, y = map(int, partes)

        if not (0 <= x <= y) or y == 0:
            raise ValueError("X debe ser menor o igual a Y, y Y no puede ser cero")

        porcentaje = (x / y) * 100

        # Determinadno la categoría según el porcentaje
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f"{round(porcentaje)}%"

    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        fraccion = input("Ingrese una fracción en formato X/Y: ")

        try:
            x, y = map(int, fraccion.split('/'))
        except ValueError:
            print("Error: Ambos valores deben ser números enteros.")
            continue

        resultado = obtener_porcentaje(fraccion)

        if resultado is not None:
            print(f"La cantidad de combustible en el tanque es: {resultado}")
            break

if __name__ == "__main__":
    main()
