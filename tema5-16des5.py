# Definición de la clase Nodo para el árbol binario de búsqueda
class Nodo:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izq = None
        self.der = None

# Función para insertar un nodo en el árbol
def insertar_en_arbol(raiz, nombre, promedio):
    if raiz is None:
        print(f"Insertando nodo raiz: {nombre} con promedio {promedio}")
        return Nodo(nombre, promedio)
    elif promedio < raiz.promedio:
        print(f"Insertando {nombre} a la izquierda de {raiz.nombre}")
        raiz.izq = insertar_en_arbol(raiz.izq, nombre, promedio)
    else:
        print(f"Insertando {nombre} a la derecha de {raiz.nombre}")
        raiz.der = insertar_en_arbol(raiz.der, nombre, promedio)
    return raiz

# Recorrido en inorden del árbol (muestra estudiantes en orden ascendente de promedio)
def recorrido_inorden(raiz):
    if raiz is not None:
        recorrido_inorden(raiz.izq)
        print(f"{raiz.nombre}: {raiz.promedio}")
        recorrido_inorden(raiz.der)

# Lista de estudiantes y sus promedios de calificaciones
estudiantes = [
    {"nombre": "Veronica", "promedio": 12},
    {"nombre": "Javier", "promedio": 8},
    {"nombre": "Diego", "promedio": 11},
    {"nombre": "Elena", "promedio": 8},
    {"nombre": "Milagros", "promedio": 10},
    {"nombre": "Gonzalo", "promedio": 9},
    {"nombre": "Pablo", "promedio": 7}
]

# Construir el árbol de clasificación de estudiantes por rendimiento
arbol = None
for estudiante in estudiantes:
    arbol = insertar_en_arbol(arbol, estudiante["nombre"], estudiante["promedio"])

# Mostrar los estudiantes en orden ascendente de promedio
print("Estudiantes en orden ascendente de promedio:")
recorrido_inorden(arbol)
