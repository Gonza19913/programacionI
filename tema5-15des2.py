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

# Función para el recorrido en inorden y la suma de los valores de los nodos
def suma_inorder(nodo):
    if nodo is None:
        return 0
    # Suma los valores de los nodos en inorden: izquierda, raíz, derecha
    return suma_inorder(nodo.izq) + nodo.val + suma_inorder(nodo.der)

# Llamada a la función para calcular y mostrar la suma
suma_total = suma_inorder(raiz)
print("La suma de todos los valores en el arbol (recorrido inorden) es:", suma_total)
