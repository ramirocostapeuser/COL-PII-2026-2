# Ejercicio 7 - Decorador

import time
from functools import wraps


def mide_tiempo(funcion):
    """Decorador que muestra cuánto tardó en ejecutarse la función envuelta."""
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[mide_tiempo] '{funcion.__name__}' tardó {fin - inicio:.6f} segundos")
        return resultado
    return envoltura


@mide_tiempo
def sumar_hasta(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    resultado = sumar_hasta(10_000_000)
    print(f"Resultado de sumar del 1 al 10.000.000: {resultado}")
