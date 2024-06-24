#Desafío 2: Ordenar el Inventario de Libros
#Como encargado de la biblioteca, necesitas organizar los libros de acuerdo
#con sus códigos de identificación en orden decreciente, sin modificar la lista original. 
#Se recomienda usar la función sorted().

class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
    def __repr__(self):
        return repr((self.codigo, self.titulo, self.autor))

lista_libros = [
    Libro("B10", "La tregua", "Mario Benedetti"),
    Libro("A01", "Don Juan", "Juan Carlos Onetti"),
    Libro("C07", "Cuentos completos", "Horacio Quiroga"),
    Libro("F03", "El pozo", "Juan Carlos Onetti"),
    Libro("D08", "Gracias por el fuego", "Mario Benedetti"),
    Libro("E05", "Tierra de nadie", "Juan José Morosoli"),
    Libro("H02", "Las cenizas del cóndor", "Fernando Butazzoni"),
    Libro("G09" , "La balada del álamo Carolina", "Felipe Polleri"),
    Libro("I04", "La otra aventura", "Eduardo Galeano"),
    Libro("J06" , "El hombre de la máscara de cuero", "Hugo Burel")
]

lista_ordenada = sorted(lista_libros, key=lambda libro: libro.codigo, reverse= True)
print(lista_ordenada)



