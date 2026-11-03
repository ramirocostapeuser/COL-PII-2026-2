# Ejercicio 4 - Comprensión de listas y diccionarios

productos = [
    ("Teclado", 15000),
    ("Mouse", 8000),
    ("Monitor", 120000),
    ("Auriculares", 25000),
    ("Webcam", 32000),
]

# Lista con el 10% de descuento aplicado a cada precio
precios_con_descuento = [round(precio * 0.9, 2) for nombre, precio in productos]

# Diccionario nombre -> precio con descuento
dicc_descuentos = {nombre: round(precio * 0.9, 2) for nombre, precio in productos}

print("Precios con 10% de descuento:", precios_con_descuento)
print("Diccionario nombre -> precio con descuento:")
for nombre, precio in dicc_descuentos.items():
    print(f"  {nombre}: ${precio}")
