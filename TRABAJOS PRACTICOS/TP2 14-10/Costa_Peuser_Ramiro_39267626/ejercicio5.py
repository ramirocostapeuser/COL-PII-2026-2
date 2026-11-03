# Ejercicio 5 - Generador simple

def multiplos_de(n, limite):
    """Produce, de a uno, los múltiplos de n hasta limite (inclusive)."""
    multiplo = n
    while multiplo <= limite:
        yield multiplo
        multiplo += n


print("Múltiplos de 3 hasta 20:")
for m in multiplos_de(3, 20):
    print(m)

print("\nMúltiplos de 7 hasta 50:")
for m in multiplos_de(7, 50):
    print(m)
