# Ejercicio 8 - Validar contactos desde un archivo

import re

PATRON_DNI = r"^\d{7,8}$"
PATRON_EMAIL = r"^[\w.-]+@[\w-]+(\.[\w-]+)+$"


class ContactoInvalidoError(Exception):
    pass


def validar_contacto(nombre, dni, email):
    if not re.match(PATRON_DNI, dni):
        raise ContactoInvalidoError(f"DNI inválido ({dni})")
    if not re.match(PATRON_EMAIL, email):
        raise ContactoInvalidoError(f"email inválido ({email})")


# 1) Guardar la lista de contactos en un archivo (nombre;dni;email)
contactos = [
    "Ana López;12345678;ana@gmail.com",
    "Juan Pérez;123;juan@hotmail.com",          # DNI inválido
    "Lucía Gómez;7654321;lucia.gomez@empresa.com.ar",
    "Pedro Ruiz;23456789;pedro-arroba-mail.com",  # email inválido
    "Sofía Díaz;34567890;sofia@yahoo.com",
]

with open("contactos.txt", "w", encoding="utf-8") as archivo:
    for contacto in contactos:
        archivo.write(contacto + "\n")

# 2) Leer el archivo y validar cada contacto
validos = []
with open("contactos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, dni, email = linea.strip().split(";")
        try:
            validar_contacto(nombre, dni, email)
            validos.append(linea.strip())
            print(f"Válido: {nombre}")
        except ContactoInvalidoError as error:
            print(f"Descartado: {nombre} -> {error}")

# 3) Escribir solo los contactos válidos en el archivo de salida
with open("contactos_validos.txt", "w", encoding="utf-8") as archivo:
    for contacto in validos:
        archivo.write(contacto + "\n")

print(f"\nSe guardaron {len(validos)} contactos válidos en contactos_validos.txt")
