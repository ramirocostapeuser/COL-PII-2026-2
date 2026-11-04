# Ejercicio 3 - Excepciones múltiples y finally

def dividir_100(texto):
    try:
        numero = int(texto)
        resultado = 100 / numero
        print(f"100 / {numero} = {resultado}")
    except ValueError:
        print(f"Error: '{texto}' no es un número")
    except ZeroDivisionError:
        print("Error: no se puede dividir por 0")
    finally:
        print("Fin de la operación \n")


dividir_100("4")
dividir_100("hola")
dividir_100("0")
