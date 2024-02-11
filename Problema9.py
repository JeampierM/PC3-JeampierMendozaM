def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as e:
        return f"Error: {e}"
