# Lista de estudiantes (asegúrate de que esté ordenada alfabéticamente)
estudiantes = ["Diego", "Elena", "Gonzalo", "Javier", "Milagros", "Pablo", "Veronica"]

# Implementación de búsqueda binaria insensible a mayúsculas y minúsculas
def busqueda_binaria(lista, nombre_objetivo):
    nombre_objetivo = nombre_objetivo.lower()  # Convertimos el nombre objetivo a minúsculas
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio].lower() == nombre_objetivo:  # Convertimos el nombre de la lista a minúsculas
            return f"Estudiante encontrado en la posicion: {medio + 1}"
        elif lista[medio].lower() < nombre_objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return "Estudiante no encontrado"

# Ejemplo de búsqueda de un estudiante específico
nombre_objetivo = "Alfredo"  # Cambia este valor para probar con otros nombres
resultado = busqueda_binaria(estudiantes, nombre_objetivo)
print(resultado)
