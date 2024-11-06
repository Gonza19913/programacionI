# Definición de la clase Nodo para representar cada nodo en el árbol
class Nodo:
    def __init__(self, valor):
        self.izq = None   # Hijo izquierdo
        self.der = None   # Hijo derecho
        self.val = valor  # Valor del nodo

# Creación del árbol binario con 3 niveles de profundidad
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)
raiz.izq.izq.izq = Nodo(8)
raiz.izq.izq.der = Nodo(9)

# Función para el recorrido en preorden
def print_preorder(nodo):
    if nodo:
        print(nodo.val, end=" ")
        print_preorder(nodo.izq)
        print_preorder(nodo.der)

# Llamada a la función para mostrar los valores en preorden
print("Recorrido en preorden del arbol:")
print_preorder(raiz)
