import heapq

class Nodo:
    def __init__(self, posicion, g, h):
        self.posicion = posicion
        self.g = g
        self.h = h
        self.f = g + h

    def __Lt__(self, other):
        return self.f < other.f


def a_star(grado, heuriticas, inicio, fin):
    abiertos = []
    heapq.heapify(abiertos)

    nodo_inicio = Nodo(inicio, g=0, h=heuriticas.get(inicio, 0))
    heapq.heappush(abiertos,(nodo_inicio.f, nodo_inicio))

    cerrados = set()

    while abiertos:
        _, nodo_actual = heapq.heappop(abiertos)

        
        if nodo_actual.posicion == fin:
            camino = []  
            while nodo_actual:
                camino.append(nodo_actual.posicion)
                nodo_actual = nodo_actual.padre
            return camino[::-1] 

        cerrados.add(nodo_actual.posicion)

        for vecino, costo in grafo.get(nodo_actual.posicion, []):
            if vecino in cerrados:
                continue

            g_vecino = nodo_actual.g + costo
            h_vecino = heuriticas.get(vecino, 0)
            nodo_vecino = Nodo(vecino, g=g_vecino, padre=nodo_actual)
            heapq.heapush(abiertos, (nodo_vecino.f, nodo_vecino)) 

            return None
        



