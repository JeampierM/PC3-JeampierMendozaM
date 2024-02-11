import random

def generar_numeros_aleatorios(n=20, rango=(0, 100)):
    return [random.randint(rango[0], rango[1]) for _ in range(n)]

def mostrar_lista(lista):
    print("Lista de números:")
    print(lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
