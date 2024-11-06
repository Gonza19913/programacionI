# Definición de la clase Nodo para el árbol de búsqueda binaria (ABB)
class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor

# Función para insertar un valor en el ABB
def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.val:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)
    return raiz

# Función para buscar un valor en el ABB
def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz.val == valor:
        return True
    elif valor < raiz.val:
        return buscar(raiz.izq, valor)
    else:
        return buscar(raiz.der, valor)

# Creación del ABB con un conjunto de valores únicos
valores = [10, 5, 15, 3, 7, 12, 20]
raiz = None
for val in valores:
    raiz = insertar(raiz, val)

# Prueba de búsqueda de un número en el ABB
numero_a_buscar = 12
existe = buscar(raiz, numero_a_buscar)
print(f"¿El numero {numero_a_buscar} existe en el arbol? {'Si' if existe else 'No'}")
