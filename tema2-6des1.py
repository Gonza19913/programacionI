# Solicitar al usuario que ingrese la calificación necesaria para aprobar
calificacion_aprobacion = int(input("Ingrese la calificacion necesaria para aprobar el curso: "))

# Solicitar al usuario que ingrese las calificaciones
calificaciones = []
while True: 
    calificacion = input("Ingrese una calificacion (o 'z' para terminar): ")
    
    if calificacion.lower() == 'z':
        break
    calificaciones.append(int(calificacion))

# Contar cuántos estudiantes aprobaron y reprobaron
aprobados = 0
reprobados = 0
for calificacion in calificaciones:
    if calificacion >= calificacion_aprobacion:
        aprobados += 1
    else:
        reprobados += 1

# Mostrar los resultados
print("Numero de estudiantes aprobados: " + str(aprobados))
print("Numero de estudiantes reprobados: " + str(reprobados))
