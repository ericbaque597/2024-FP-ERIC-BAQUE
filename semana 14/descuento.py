def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el monto del descuento basado en el monto total y el porcentaje de descuento."""
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    # Llamadas a la función calcular_descuento
    monto1 = 350.0  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)  # Llamada con el porcentaje predeterminado
    monto_final1 = monto1 - descuento1

    print(f"Compra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    monto2 = 280.0  # Otro monto total de la compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento personalizado
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)  # Llamada con un porcentaje diferente
    monto_final2 = monto2 - descuento2

    print(f"Compra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento (15%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()
