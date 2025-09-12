import networkx as nx
import matplotlib.pyplot as plt

warehouses = ['G1', 'G2', 'G3', 'G4']

G = nx.DiGraph()

G.add_nodes_from(warehouses)

shipments = [
    ('G1', 'G2'),
    ('G1', 'G3'),
    ('G2', 'G4'),
    ('G3', 'G4')
]
G.add_edges_from(shipments)

is_strongly_connected = nx.is_strongly_connected(G)

plt.figure(figsize=(10, 8))
pos = {'G1': (0, 0), 'G2': (1, 1), 'G3': (1, -1), 'G4': (2, 0)}

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=12, font_weight='bold', arrowsize=20)

print("analisis graf rantai pasokan:")
print("=============================")
print(f"Semua node (gudang): {G.nodes()}")
print(f"Alur pengiriman (edge): {G.edges()}")
print(f"Apakah graf ini 'strongly connected'? {is_strongly_connected}")

plt.show()