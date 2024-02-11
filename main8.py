from Problema8 import generar_numeros_aleatorios, mostrar_lista, ordenar_y_mostrar

def main():
    # Generando lista de 20 números aleatorios entre 0 y 100
    numeros_aleatorios = generar_numeros_aleatorios()

    # Mostrando la lista 
    mostrar_lista(numeros_aleatorios)

    # Ordenando los valores de la lista
    ordenar_y_mostrar(numeros_aleatorios)

if __name__ == '__main__':
    main()
