def main():
    while True:
        calificaciones_cadena = input("Introduce las calificaciones separadas por comas: ")

        # Dividiendo la cadena en calificaciones individuales
        listaCalificaciones = calificaciones_cadena.split(',')

        calificaciones_enteros = []

        # Convertiendo cada calificación en un entero
        for calificacion in listaCalificaciones:
            try:
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)
            except ValueError:
                print(f"Error: '{calificacion}' no es un valor válido. Por favor, introduce valores numéricos separados por comas.")
                break  

        if len(calificaciones_enteros) == len(listaCalificaciones):
            print("Calificaciones ingresadas:", calificaciones_enteros)
            break

if __name__ == "__main__":
    main()
