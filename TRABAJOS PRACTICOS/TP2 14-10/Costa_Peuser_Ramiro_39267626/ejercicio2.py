# Ejercicio 3 - reduce

from functools import reduce

carrito = [1500.50, 320.00, 4999.99, 870.25, 2100.00]

total = reduce(lambda acumulado, precio: acumulado + precio, carrito)
mas_caro = reduce(lambda a, b: a if a > b else b, carrito)

print("Precios del carrito:", carrito)
print(f"Total de la compra: ${total:.2f}")
print(f"Precio más caro: ${mas_caro:.2f}")
