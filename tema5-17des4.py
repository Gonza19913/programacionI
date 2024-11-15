def mostrar_prestamos():
    # Leer y mostrar los registros actuales
    prestamos = []
    with open("prestamos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            prestamos.append(linea.strip())
    
    # Mostrar los registros al usuario
    print("Registros de Prestamos:")
    for i, prestamo in enumerate(prestamos[2:], start=1):  # Omitimos el encabezado y la línea de separación
        print(f"{i}. {prestamo}")
    
    return prestamos

def eliminar_prestamo():
    # Mostrar los préstamos y obtener la lista de registros
    prestamos = mostrar_prestamos()
    
    # Solicitar al usuario que seleccione un registro para eliminar
    try:
        num_registro = int(input("Ingrese el numero del registro que desea eliminar: "))
        if 1 <= num_registro <= len(prestamos) - 2:  # Ajuste para omitir encabezado y línea de separación
            # Eliminar el registro seleccionado
            prestamos.pop(num_registro + 1)  # +1 para mantener la numeración con el encabezado en mente
            
            # Escribir los registros actualizados al archivo
            with open("prestamos.txt", "w", encoding="utf-8") as archivo:
                for prestamo in prestamos:
                    archivo.write(prestamo + "\n")
            print("Registro eliminado con éxito.")
        else:
            print("Numero de registro no valido.")
    except ValueError:
        print("Debe ingresar un numero valido.")

# Llamada a la función para eliminar un préstamo
eliminar_prestamo()
