# Ejercicio 1 - División segura

def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir por 0")
        return None


print("10 / 2 =", division_segura(10, 2))
print("10 / 0 =", division_segura(10, 0))
