def ordenar_fila(matriz, fila):
    """Ordena una fila específica de la matriz en orden ascendente."""
    matriz[fila].sort()

def mostrar_matriz(matriz):
    """Imprime la matriz en un formato legible."""
    for fila in matriz:
        print(fila)

def main():
    # Crear una matriz 3x3
    matriz = [
        [3, 1, 2],
        [9, 7, 8],
        [6, 4, 5]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    mostrar_matriz(matriz)

    # Especificar qué fila ordenar (0, 1 o 2)
    fila_a_ordenar = 1  # Por ejemplo, la segunda fila (índice 1)

    # Ordenar la fila especificada
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar la matriz después de ordenar la fila
    print("\nMatriz después de ordenar la fila", fila_a_ordenar + 1, ":")
    mostrar_matriz(matriz)

if __name__ == "__main__":
    main()
