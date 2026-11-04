# Ejercicio 6 - Manejo de archivos

def leer_archivo_seguro(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'. Revisá el nombre.")
        return None


# Creamos un archivo para la prueba con un archivo que sí existe
with open("existe.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este archivo sí existe.")

print("Prueba 1 - archivo que existe:")
print(leer_archivo_seguro("existe.txt"))

print("\nPrueba 2 - archivo que no existe:")
leer_archivo_seguro("no_existe.txt")

print("\nEl programa siguió corriendo después del error.")
