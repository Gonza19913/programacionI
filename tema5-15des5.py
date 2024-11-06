# Definición de la clase Nodo para el árbol de expresiones
class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor

# Función para construir el árbol de expresiones a partir de una expresión en forma de lista
def construir_arbol(tokens):
    pila = []
    for token in tokens:
        if token.isdigit():  # Si es un número, crea un nodo y lo apila
            pila.append(Nodo(int(token)))
        else:  # Si es un operador, crea un nodo operador y asigna hijos
            nodo = Nodo(token)
            nodo.der = pila.pop()
            nodo.izq = pila.pop()
            pila.append(nodo)
    return pila[0]

# Función para evaluar el árbol de expresiones
def evaluar_arbol(nodo):
    if nodo.izq is None and nodo.der is None:  # Caso base: nodo hoja (número)
        return nodo.val
    # Evalúa el subárbol izquierdo y derecho recursivamente
    valor_izq = evaluar_arbol(nodo.izq)
    valor_der = evaluar_arbol(nodo.der)
    # Aplica el operador del nodo actual
    if nodo.val == '+':
        return valor_izq + valor_der
    elif nodo.val == '-':
        return valor_izq - valor_der
    elif nodo.val == '*':
        return valor_izq * valor_der
    elif nodo.val == '/':
        return valor_izq / valor_der

# Expresión de ejemplo: "5 + 3 * 4"
# Convertimos la expresión en notación postfija para simplificar la construcción del árbol
tokens = ["5", "3", "4", "*", "+"]

# Construcción del árbol de expresiones
raiz_expresion = construir_arbol(tokens)

# Evaluación del árbol de expresiones
resultado = evaluar_arbol(raiz_expresion)
print("El resultado de la expresion es:", resultado)
