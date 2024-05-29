# Solicitar al usuario que ingrese las calificaciones separadas por comas
calificaciones_entrada = input("Ingrese las calificaciones separadas por comas: ")

# Convertir la entrada a una lista de calificaciones
lista_calificaciones = [int(cal) for cal in calificaciones_entrada.split(",")]

# Calcular el promedio
# (Aquí el método len() devuelve la longitud de un objeto, en este caso la "lista de calificaciones")
promedio = sum(lista_calificaciones) / len(lista_calificaciones)

# Mostrar el resultado
print("El promedio de las calificaciones es: " + str(promedio))
