# Lista de estudiantes y sus promedios de calificaciones
estudiantes = [
    {"nombre": "Veronica", "promedio": 12},
    {"nombre": "Javier", "promedio": 8},
    {"nombre": "Diego", "promedio": 11},
    {"nombre": "Elena", "promedio": 8},
    {"nombre": "Milagros", "promedio": 10},
    {"nombre": "Gonzalo", "promedio": 9},
    {"nombre": "Pablo", "promedio": 7}
]

# Implementación del ordenamiento por selección para ordenar por promedio
def ordenar_por_promedio(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if estudiantes[j]["promedio"] > estudiantes[max_idx]["promedio"]:
                max_idx = j
        # Intercambiar al estudiante con el promedio más alto encontrado
        estudiantes[i], estudiantes[max_idx] = estudiantes[max_idx], estudiantes[i]

# Ordenar la lista de estudiantes por promedio
ordenar_por_promedio(estudiantes)

# Mostrar los estudiantes ordenados
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")
