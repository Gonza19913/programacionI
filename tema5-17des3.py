import csv

def actualizar_cantidad_copias(titulo_libro, nuevas_copias):
    # Leer el archivo actual y almacenar los datos en una lista temporal
    inventario = []
    archivo_modificado = False

    # Leer el archivo CSV y actualizar la cantidad de copias si el título coincide
    with open("inventario.csv", "r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        for fila in lector_csv:
            if fila[0].strip() == "Título":  # Encabezado
                inventario.append(fila)
            elif fila[0].strip().lower() == titulo_libro.strip().lower():  # Ignorar mayúsculas y espacios
                inventario.append([fila[0].strip(), nuevas_copias])
                archivo_modificado = True
            else:
                inventario.append(fila)

    # Escribir los datos actualizados en el archivo CSV
    if archivo_modificado:
        with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv, delimiter=';')
            escritor_csv.writerows(inventario)
        print(f"La cantidad de copias de '{titulo_libro}' se ha actualizado a {nuevas_copias}.")
    else:
        print(f"No se encontró el libro '{titulo_libro}' en el inventario.")

# Solicitar al usuario el título del libro y la nueva cantidad de copias
titulo = input("Ingrese el título del libro a actualizar: ")
cantidad = input("Ingrese la nueva cantidad de copias: ")

# Convertir la cantidad de copias a entero y llamar a la función
try:
    cantidad = int(cantidad)
    actualizar_cantidad_copias(titulo, cantidad)
except ValueError:
    print("La cantidad de copias debe ser un número entero.")
