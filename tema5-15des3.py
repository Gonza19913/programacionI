# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor

# Creación de un árbol binario básico
raiz = Nodo(10)
raiz.izq = Nodo(5)
raiz.der = Nodo(15)
raiz.izq.izq = Nodo(3)
raiz.izq.der = Nodo(7)
raiz.der.izq = Nodo(12)
raiz.der.der = Nodo(20)

# Función para el recorrido en postorden y encontrar el valor máximo
def maximo_postorder(nodo):
    if nodo is None:
        return float('-inf')
    
    # Calcula el máximo en el subárbol izquierdo, el derecho y el nodo actual
    max_izq = maximo_postorder(nodo.izq)
    max_der = maximo_postorder(nodo.der)
    max_actual = max(nodo.val, max_izq, max_der)
    
    return max_actual

# Llamada a la función para encontrar el valor máximo en el árbol
maximo_valor = maximo_postorder(raiz)
print("El valor maximo en el arbol (recorrido postorden) es:", maximo_valor)
