# Ejercicio 2 - Excepción personalizada

class EdadInvalidaError(Exception):
    pass


class Persona:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise EdadInvalidaError(f"La edad no puede ser negativa ({edad})")
        self.nombre = nombre
        self.edad = edad

try: 
    persona1 = Persona("Ana", 30)
    print(f"Persona creada: {persona1.nombre}, {persona1.edad} años")
except EdadInvalidaError as error:
    print("No se pudo crear la persona:", error)

try:
    persona2 = Persona("Juan", -5)
except EdadInvalidaError as error:
    print("No se pudo crear la persona:", error)

print("El programa sigue funcionando")
