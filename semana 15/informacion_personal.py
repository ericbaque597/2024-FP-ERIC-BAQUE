# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Eric Baque",
    "edad": 30,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de "ciudad"
print(f"Ciudad original: {informacion_personal['ciudad']}")
informacion_personal["ciudad"] = "Quito"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para "telefono"
informacion_personal["telefono"] = "123-456-789"

# Verificar existencia de la clave "telefono"
if "telefono" in informacion_personal:
    print(f"Teléfono encontrado: {informacion_personal['telefono']}")
else:
    print("La clave 'telefono' no existe.")

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("La clave 'edad' ha sido eliminada.")

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
