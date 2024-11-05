def leer_archivo(nombre_archivo):
    try:
        # Intentamos abrir el archivo en modo de lectura
        archivo = open(nombre_archivo, 'r')
        
        # Leemos y mostramos el contenido del archivo
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    
    except IOError:
        print("Error: Hubo un problema al leer el archivo.")
    
    finally:
        # Aseguramos que el archivo se cierre, si fue abierto
        try:
            archivo.close()
            print("El archivo se ha cerrado correctamente.")
        except NameError:
            # Si el archivo no fue abierto, se captura el NameError
            print("No hay archivo abierto que cerrar.")

# Llamada a la función con un ejemplo de nombre de archivo
nombre_archivo = "archivo_prueba.txt"
leer_archivo(nombre_archivo)
