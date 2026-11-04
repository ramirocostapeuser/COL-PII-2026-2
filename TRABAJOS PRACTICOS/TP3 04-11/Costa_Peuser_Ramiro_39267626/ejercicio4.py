# Ejercicio 4 - Escribir y leer archivos

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Alumno(nombre={self.nombre}, nota={self.nota})"


alumnos = [
    Alumno("Ana", 9),
    Alumno("Juan", 7),
    Alumno("Lucía", 8),
]

# Guardar
with open("alumnos.txt", "w", encoding="utf-8") as archivo:
    for alumno in alumnos:
        archivo.write(f"{alumno.nombre};{alumno.nota}\n")

# Leer el archivo y reconstruir los objetos Alumno
alumnos_leidos = []
with open("alumnos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, nota = linea.strip().split(";")
        alumnos_leidos.append(Alumno(nombre, int(nota)))

print("Alumnos reconstruidos desde el archivo:")
for alumno in alumnos_leidos:
    print(alumno)
