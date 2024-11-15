def inicializar_archivo_libros():
    """Crea el archivo 'libros.txt' con formato de tabla si no existe."""
    try:
        with open("libros.txt", "x") as archivo:
            archivo.write(f"{'Título':<30} | {'Autor'}\n")
            archivo.write("-" * 50 + "\n")
    except FileExistsError:
        pass  # Si el archivo ya existe, no hacer nada

def buscar_libros_por_autor(nombre_autor):
    # Inicializar el archivo en formato de tabla si no existe
    inicializar_archivo_libros()

    # Leer el archivo y buscar coincidencias parciales con el nombre del autor
    with open("libros.txt", "r") as archivo:
        libros_encontrados = []
        for linea in archivo:
            # Ignorar las líneas de encabezado y separación
            if linea.startswith("-") or "Título" in linea:
                continue
            
            # Separar título y autor basándose en el carácter delimitador "|"
            partes = linea.split(" | ")
            if len(partes) == 2:
                titulo, autor = partes[0].strip(), partes[1].strip()
                # Convertir ambos a minúsculas para una comparación sin distinción de mayúsculas/minúsculas
                if nombre_autor.lower() in autor.lower():
                    libros_encontrados.append(titulo)
        
        # Mostrar los resultados de la búsqueda
        if libros_encontrados:
            print(f"Libros de autores que contienen '{nombre_autor}':")
            for libro in libros_encontrados:
                print(f"- {libro}")
        else:
            print(f"No se encontraron libros de autores que contengan '{nombre_autor}'.")

# Solicitar al usuario el nombre o parte del nombre del autor
autor = input("Ingrese el nombre o apellido del autor que desea buscar: ")
buscar_libros_por_autor(autor)
