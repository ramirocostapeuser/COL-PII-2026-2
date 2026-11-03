# Ejercicio 1 - Funciones lambda básicas

cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7]

for n in numeros:
    print(f"Número: {n} | Cuadrado: {cuadrado(n)} | ¿Es par?: {es_par(n)}")