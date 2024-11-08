# Definir una matriz fija de calificaciones
calificaciones = [
    [8, 7, 10, 9],  # Estudiante 1
    [10, 3, 12, 4],  # Estudiante 2
    [12, 10, 9, 11],  # Estudiante 3
]

# Lista de materias
materias = ["Programacion", "Matematica", "Logica", "Didactica"]

# Función para buscar todas las ocurrencias de una calificación específica
def buscar_calificacion(matriz, calificacion_objetivo, materias):
    resultados = []
    for estudiante_idx, calificaciones in enumerate(matriz):
        for materia_idx, calificacion in enumerate(calificaciones):
            if calificacion == calificacion_objetivo:
                estudiante = f"Estudiante {estudiante_idx + 1}"
                materia = materias[materia_idx]
                resultados.append(f"{estudiante}, Materia: {materia}")
    if resultados:
        return "Calificacion encontrada en:\n" + "\n".join(resultados)
    else:
        return "Calificacion no encontrada"

# Búsqueda de una calificación específica
calificacion_objetivo = 5  # Cambia este valor para buscar otra calificación
resultado = buscar_calificacion(calificaciones, calificacion_objetivo, materias)
print(resultado)
