# Ejercicio 3 - reduce

from functools import reduce

# Lista de precios de los productos de la tienda
precios = {
    "Teclado": 15000,
    "Mouse": 8000,
    "Monitor": 120000,
    "Webcam": 32000,
    "Auriculares": 25000,
}

# Productos que el cliente agregó al carrito
carrito = ["Teclado", "Monitor", "Mouse", "Webcam"]

# Precios de los productos del carrito
precios_carrito = [precios[producto] for producto in carrito]

total = reduce(lambda acumulado, precio: acumulado + precio, precios_carrito)
mas_caro = reduce(lambda a, b: a if a > b else b, precios_carrito)

print("Carrito:")
for producto in carrito:
    print(f"  {producto}: ${precios[producto]}")
print(f"Total de la compra: ${total}")
print(f"Precio más caro: ${mas_caro}")
