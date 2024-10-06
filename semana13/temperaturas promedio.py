def calcular_promedios_temperaturas(temperaturas):
    promedios_semanales = []
    promedios_generales = []
    semanas = len(temperaturas[0])  # Número de semanas
    dias = len(temperaturas[0][0])  # Número de días

    for ciudad in temperaturas:
        promedios_ciudad = []
        suma_total_ciudad = 0

        for semana in ciudad:
            suma_temperaturas = sum(semana)
            promedio_semanal = suma_temperaturas / dias
            promedios_ciudad.append(promedio_semanal)
            suma_total_ciudad += suma_temperaturas

        promedio_general = suma_total_ciudad / (semanas * dias)
        promedios_semanales.append(promedios_ciudad)
        promedios_generales.append(promedio_general)

    return promedios_semanales, promedios_generales


# Definir las ciudades, días y semanas
ciudades = ['Machala', 'Ibarra', 'Imbabura']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear la matriz 3D con nuevas temperaturas ficticias
temperaturas = [
    [  # Machala
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [24, 25, 26, 27, 28, 29, 30],  # Semana 2
        [23, 24, 25, 26, 27, 28, 29],  # Semana 3
        [22, 23, 24, 25, 26, 27, 28]  # Semana 4
    ],
    [  # Ibarra
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [19, 20, 21, 22, 23, 24, 25],  # Semana 2
        [18, 19, 20, 21, 22, 23, 24],  # Semana 3
        [17, 18, 19, 20, 21, 22, 23]  # Semana 4
    ],
    [  # Imbabura
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [14, 15, 16, 17, 18, 19, 20],  # Semana 2
        [13, 14, 15, 16, 17, 18, 19],  # Semana 3
        [12, 13, 14, 15, 16, 17, 18]  # Semana 4
    ]
]

# Llamar a la función y obtener los resultados
promedios_semanales, promedios_generales = calcular_promedios_temperaturas(temperaturas)

# Mostrar resultados para cada ciudad
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas diarias y promedios para {ciudad}:")
    for semana in range(semanas):
        print(f"\nSemana {semana + 1}:")
        for dia in range(len(dias)):
            print(f"{dias[dia]}: {temperaturas[i][semana][dia]}°C")
        print(f"Promedio de temperaturas en Semana {semana + 1}: {promedios_semanales[i][semana]:.2f}°C")

    print(f"\nPromedio general de las 4 semanas en {ciudad}: {promedios_generales[i]:.2f}°C")
