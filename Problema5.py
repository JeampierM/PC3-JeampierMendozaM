class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {self.notas}")

    def set_age(self, edad):
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
        else:
            self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

def main():
    while True:
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        if not nombre_alumno.isalpha():
            print("Error: El nombre debe contener solo letras. Intente nuevamente.")
        else:
            break

    while True:
        try:
            registro_alumno = int(input("Ingrese el número de registro del alumno: "))
            break
        except ValueError:
            print("Error: El número de registro debe ser un valor numérico. Intente nuevamente.")

    alumno = Alumno(nombre_alumno, registro_alumno)

    while True:
        try:
            edad_alumno = int(input("Ingrese la edad del alumno: "))
            alumno.set_age(edad_alumno)
            break
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico para la edad. Intente nuevamente.")

    notas_alumno = [float(nota) for nota in input("Ingrese las notas del alumno (separadas por coma): ").split(',')]
    alumno.set_notas(notas_alumno)

    alumno.display()

if __name__ == "__main__":
    main()
