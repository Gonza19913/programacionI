import sys

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.matriz_adyacencia = [[0] * num_nodos for _ in range(num_nodos)]
        self.nodos = {i: chr(65 + i) for i in range(num_nodos)}

    def agregar_arista(self, origen, destino, peso):
        if 0 <= origen < self.num_nodos and 0 <= destino < self.num_nodos:
            self.matriz_adyacencia[origen][destino] = peso

    def mostrar_matriz(self):
        print("Matriz de adyacencia:")
        for fila in self.matriz_adyacencia:
            print(fila)
        print()

    def dijkstra(self, inicio):
        distancias = [sys.maxsize] * self.num_nodos
        distancias[inicio] = 0
        visitados = [False] * self.num_nodos
        predecesores = [-1] * self.num_nodos

        for _ in range(self.num_nodos):
            nodo_actual = min((dist for dist in range(self.num_nodos) if not visitados[dist]), key=distancias.__getitem__)
            visitados[nodo_actual] = True

            for vecino, peso in enumerate(self.matriz_adyacencia[nodo_actual]):
                if peso > 0 and not visitados[vecino] and distancias[nodo_actual] + peso < distancias[vecino]:
                    distancias[vecino] = distancias[nodo_actual] + peso
                    predecesores[vecino] = nodo_actual

        self.mostrar_resultado(distancias, predecesores, inicio)

    def mostrar_resultado(self, distancias, predecesores, inicio):
        print(f"Desde el nodo {self.nodos[inicio]}:")
        for destino in range(self.num_nodos):
            if destino != inicio:
                camino = self.construir_camino(predecesores, destino)
                print(f"Hasta {self.nodos[destino]}: {' -> '.join(camino)}, Costo: {distancias[destino]}")

    def construir_camino(self, predecesores, destino):
        camino = []
        while destino != -1:
            camino.insert(0, self.nodos[destino])
            destino = predecesores[destino]
        return camino

# Ejemplo de uso
grafo = Grafo(5)
grafo.agregar_arista(0, 1, 10)
grafo.agregar_arista(0, 4, 3)
grafo.agregar_arista(1, 2, 2)
grafo.agregar_arista(2, 3, 9)
grafo.agregar_arista(4, 1, 4)
grafo.agregar_arista(4, 2, 8)
grafo.mostrar_matriz()
grafo.dijkstra(0)