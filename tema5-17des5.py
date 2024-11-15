from collections import Counter
import re

def contar_palabras_mas_comunes(nombre_archivo, top_n=5):
    # Leer el archivo y contar las palabras en los títulos
    try:
        with open(nombre_archivo, "r", encoding="latin-1") as archivo:
            lineas = archivo.readlines()
        
        # Ignorar el encabezado y la línea de separación
        texto_titulos = ""
        for linea in lineas[2:]:  # Saltamos las dos primeras líneas
            titulo = linea.split("|")[0].strip()  # Tomamos solo el título
            texto_titulos += titulo + " "
        
        # Convertimos el texto a minúsculas y usamos expresiones regulares para obtener solo palabras
        palabras = re.findall(r'\b\w+\b', texto_titulos.lower())
        
        # Contar las palabras
        contador_palabras = Counter(palabras)
        
        # Obtener las top_n palabras más comunes
        palabras_comunes = contador_palabras.most_common(top_n)
        
        # Mostrar las palabras más comunes
        print(f"Las {top_n} palabras mas comunes en los titulos de '{nombre_archivo}' son:")
        for palabra, frecuencia in palabras_comunes:
            print(f"{palabra}: {frecuencia} veces")
    
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")

# Llamada a la función para contar palabras
contar_palabras_mas_comunes("libros.txt")
