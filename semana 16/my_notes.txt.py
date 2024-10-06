# Escritura de Archivo de Texto
# Crear y abrir el archivo my_notes.txt en modo escritura
with open('my_notes.txt', 'w') as archivo:
    # Escribir notas personales en el archivo
    archivo.write("Nota 1: Recordar comprar leche.\n")
    archivo.write("Nota 2: Llamar a Juan sobre la reunión.\n")
    archivo.write("Nota 3: Terminar el proyecto antes del viernes.\n")

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt en modo lectura
with open('my_notes.txt', 'r') as archivo:
    # Leer y mostrar el contenido del archivo línea por línea
    print("Contenido de my_notes.txt:")
    for linea in archivo:
        print(linea.strip())  # Usar strip() para eliminar el salto de línea

# El archivo se cierra automáticamente al salir del bloque with
