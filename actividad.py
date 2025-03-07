import heapq

class Nodo:
    def __init__(self, posicion, g=0, h=0, padre=None):
        self.posicion = posicion
        self.g = g
        self.h = h
        self.f = g + h
        self.padre = padre

    def __lt__(self, other):
        return self.f < other.f

def a_star(grafo, heuristicas, inicio, fin):
    abiertos = []
    heapq.heapify(abiertos)

    nodo_inicio = Nodo(inicio, g=0, h=heuristicas.get(inicio, 0))
    heapq.heappush(abiertos, (nodo_inicio.f, nodo_inicio))

    cerrados = set()

    while abiertos:
        _, nodo_actual = heapq.heappop(abiertos)

        if nodo_actual.posicion == fin:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.posicion)
                nodo_actual = nodo_actual.padre
            return camino [::-1]    

        cerrados.add(nodo_actual.posicion)

        for vecino, costo in grafo.get(nodo_actual.posicion, []):
            if vecino in cerrados:
                continue

            g_vecino = nodo_actual.g + costo 
            h_vecino = heuristicas.get(vecino, 0)
            nodo_vecino = Nodo(vecino, g=g_vecino, h=h_vecino, padre=nodo_actual)
            heapq.heappush(abiertos, (nodo_vecino.f, nodo_vecino))

    return None

# Ejemplo de uso:
grafo = {
    'A': [('B', 1), ('C', 2), ('D', 4), ('E', 7)],
    'B': [('A', 1), ('C', 2), ('F', 3)],
    'C': [('A', 2), ('B', 2), ('D', 3), ('F', 4)],
    'D': [('A', 4), ('C', 3), ('G', 6)],
    'E': [('A', 7), ('F', 2), ('H', 3)],
    'F': [('B', 3), ('C', 4), ('E', 2), ('G', 3)],
    'G': [('D', 6), ('F', 3), ('H', 1)],
    'H': [('E', 3), ('G', 1)]
}


# Diccionario con heurísticas predefinidas
heuristicas = {
    'A': 8,
    'B': 6,
    'C': 7,
    'D': 5,
    'E': 4,
    'F': 3,
    'G': 2,
    'H': 0
}

inicio = 'A'
fin = 'H'

camino = a_star(grafo, heuristicas, inicio , fin)

print(camino)

