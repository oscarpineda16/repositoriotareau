import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo Dirigido
G = nx.DiGraph()

# Agregar las aristas
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (5, 1), (5, 2), (6, 3), (6, 4), (2, 5), (6, 1)])

# Dibujar
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color="lightgreen", node_size=1000)
plt.title("Grafo Dirigido", fontsize=16)  # Título corregido
plt.show()
