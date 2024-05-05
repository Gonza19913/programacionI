# Definimos las variables numéricas para el ancho y largo del rectángulo
ancho = 5
largo = 8

# Calculamos el área del rectángulo
area = ancho * largo

# Definimos variables de texto explicativo y 
# convertimos "ancho", "largo" y "area" a tipo string para poder realizar concatenaciones.
txt_ancho = "El ancho del rectangulo es: " + str(ancho) + " cm." 
txt_largo = "El largo del rectangulo es: " + str(largo) + " cm."
txt_area = "El area del rectangulo es: " + str(area) + " cm2."

# Presentamos los resultados, imprimiendo en pantalla
print(txt_ancho)
print(txt_largo)
print(txt_area)
