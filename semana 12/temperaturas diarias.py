# Definir las ciudades, días y semanas
ciudades = ['Machala', 'Ibarra', 'Imbabura']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear la matriz 3D con temperaturas
temperaturas = [
    [  # Machala
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [21, 22, 23, 24, 25, 26, 27],  # Semana 2
        [22, 23, 24, 25, 26, 27, 28],  # Semana 3
        [23, 24, 25, 26, 27, 28, 29]  # Semana 4
    ],
    [  # Ibarra
        [18, 19, 20, 21, 22, 23, 24],  # Semana 1
        [19, 20, 21, 22, 23, 24, 25],  # Semana 2
        [20, 21, 22, 23, 24, 25, 26],  # Semana 3
        [21, 22, 23, 24, 25, 26, 27]  # Semana 4
    ],
    [  # Imbabura
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [16, 17, 18, 19, 20, 21, 22],  # Semana 2
        [17, 18, 19, 20, 21, 22, 23],  # Semana 3
        [18, 19, 20, 21, 22, 23, 24]  # Semana 4
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
promedios = []

for ciudad in range(len(ciudades)):
    promedios_ciudad = []
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[ciudad][semana])
        promedio = suma_temperaturas / len(dias)
        promedios_ciudad.append(promedio)

    promedios.append(promedios_ciudad)

# Mostrar los resultados
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas diarias y promedios para {ciudad}:")
    for semana in range(semanas):
        print(f"\nSemana {semana + 1}:")
        for dia in range(len(dias)):
            print(f"{dias[dia]}: {temperaturas[i][semana][dia]}°C")
        print(f"Promedio de temperaturas en Semana {semana + 1}: {promedios[i][semana]:.2f}°C")

