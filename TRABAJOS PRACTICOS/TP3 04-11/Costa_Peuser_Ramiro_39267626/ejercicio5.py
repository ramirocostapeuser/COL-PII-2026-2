# Ejercicio 5 - Modos de apertura: registro con append

def registrar_operacion(mensaje):
    # Modo 'a': agrega al final sin borrar lo que ya estaba escrito
    with open("log.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


mensajes = [
    "Usuario inició sesión",
    "Se realizó una compra",
    "Usuario cerró sesión",
]

for mensaje in mensajes:
    registrar_operacion(mensaje)
    # Modo 'r': lectura del archivo para verificar que se haya escrito correctamente
with open("log.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del log:")
print(contenido)

for mensaje in mensajes:
    if mensaje in contenido:
        print(f"OK: '{mensaje}' está en el log")
    else:
        print(f"FALTA: '{mensaje}' no está en el log")
