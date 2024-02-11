import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está sobre el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        vector_resultante = Punto(otro_punto.x - self.x, otro_punto.y - self.y)
        return vector_resultante

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return round(distancia, 2)

def main():
    while True:
        try:
            x1 = float(input("Ingrese la coordenada X del primer punto: "))
            y1 = float(input("Ingrese la coordenada Y del primer punto: "))
            punto1 = Punto(x1, y1)

            x2 = float(input("Ingrese la coordenada X del segundo punto: "))
            y2 = float(input("Ingrese la coordenada Y del segundo punto: "))
            punto2 = Punto(x2, y2)

            print(f"Punto 1: {punto1}")
            print(f"Punto 2: {punto2}")

            print(f"Cuadrante Punto 1: {punto1.cuadrante()}")
            print(f"Cuadrante Punto 2: {punto2.cuadrante()}")

            vector_resultante = punto1.vector(punto2)
            print(f"Vector resultante entre Punto 1 y Punto 2: {vector_resultante}")

            distancia_entre_puntos = punto1.distancia(punto2)
            print(f"Distancia entre Punto 1 y Punto 2: {distancia_entre_puntos}")

            break  

        except ValueError:
            print("Error: Ingrese coordenadas válidas como números.")

if __name__ == "__main__":
    main()
