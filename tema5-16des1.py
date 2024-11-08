from collections import deque

class Nodo:
    def __init__(self, grado, estudiantes=None):
        self.grado = grado
        self.estudiantes = estudiantes if estudiantes is not None else []
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

def recorrido_por_niveles(raiz):
    if not raiz:
        return

    cola = deque([raiz])

    while cola:
        nodo_actual = cola.popleft()
        print(f"Grado {nodo_actual.grado}: Estudiantes {nodo_actual.estudiantes}")

        for hijo in nodo_actual.hijos:
            cola.append(hijo)

# Ejemplo de uso:
# Creación de un árbol de ejemplo
grado_12 = Nodo("12", ["Estudiante A", "Estudiante B"])
grado_11 = Nodo("11", ["Estudiante C", "Estudiante D"])
grado_10 = Nodo("10", ["Estudiante E"])
grado_12.agregar_hijo(grado_11)
grado_11.agregar_hijo(grado_10)

# Llamada al recorrido por niveles
recorrido_por_niveles(grado_12)
