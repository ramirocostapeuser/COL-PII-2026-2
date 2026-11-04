# Ejercicio 7 - Expresiones regulares

import re

PATRON_DNI = r"^\d{7,8}$"
PATRON_EMAIL = r"^[\w.-]+@[\w-]+(\.[\w-]+)+$"

dnis = ["12345678", "1234567", "123456", "12A45678", "123456789"]

print("Validación de DNIs:")

for dni in dnis:
    valido = re.match(PATRON_DNI, dni) is not None
    print(f"  {dni}: {'válido' if valido else 'inválido'}")

emails = ["ana@gmail.com", "juan.perez@empresa.com.ar", "sin-arroba.com", "mal@dominio"]
print("\nValidación de emails:")
for email in emails:
    valido = re.match(PATRON_EMAIL, email) is not None
    print(f"  {email}: {'válido' if valido else 'inválido'}")

texto = """Hola, escribime a ana@gmail.com para más info.
Si no respondo, probá con soporte@empresa.com.ar
o con el equipo de ventas: ventas.online@tienda.com
Gracias!"""

encontrados = re.findall(r"[\w.-]+@[\w-]+(?:\.[\w-]+)+", texto)
print("\nEmails encontrados en el texto:")
for email in encontrados:
    print(" ", email)
