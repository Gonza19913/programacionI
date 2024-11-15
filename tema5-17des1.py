def registrar_prestamo():
    # Solicitar al usuario la información del préstamo
    nombre_libro = input("Ingrese el nombre del libro: ")
    nombre_prestatario = input("Ingrese el nombre del prestatario: ")
    fecha_prestamo = input("Ingrese la fecha del préstamo (dd-mm-aaaa): ")

    # Crear el archivo con encabezado si no existe, y añadir datos si ya existe
    try:
        with open("prestamos.txt", "x") as archivo:
            # Agregar encabezado
            archivo.write(f"{'Libro':<30} | {'Prestatario':<20} | {'Fecha'}\n")
            archivo.write("-" * 60 + "\n")
    except FileExistsError:
        pass  # Si el archivo ya existe, no hacer nada

    # Agregar la información de préstamo en formato de tabla
    with open("prestamos.txt", "a") as archivo:
        archivo.write(f"{nombre_libro:<30} | {nombre_prestatario:<20} | {fecha_prestamo}\n")
    
    print("Préstamo registrado con éxito.")

# Llamada a la función para registrar un préstamo
registrar_prestamo()
