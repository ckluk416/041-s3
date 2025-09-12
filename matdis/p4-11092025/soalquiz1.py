import networkx as nx
import matplotlib.pyplot as plt

terminals = ['T1', 'T2', 'T3', 'T4']
residential_areas = ['R1', 'R2', 'R3']

G = nx.Graph()

G.add_nodes_from(terminals, bipartite=0)
G.add_nodes_from(residential_areas, bipartite=1)

routes = [
    ('T1', 'R1'),
    ('T2', 'R1'),
    ('T2', 'R2'),
    ('T3', 'R2'),
    ('T4', 'R3')
]
G.add_edges_from(routes)

cut_vertices = list(nx.articulation_points(G))

terminal_cut_vertices = [node for node in cut_vertices if node in terminals]

plt.figure(figsize=(10, 8))
pos = nx.bipartite_layout(G, terminals)
node_colors = []
for node in G.nodes():
    if node in terminal_cut_vertices:
        node_colors.append('red') 
    elif node in terminals:
        node_colors.append('skyblue')
    else:
        node_colors.append('lightgreen')

nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=12, font_weight='bold')

legend_labels = {
    'skyblue': 'Terminal',
    'lightgreen': 'Area Perumahan',
    'red': 'Cut Vertex (Terminal)'
}
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=15) for color, label in legend_labels.items()]
plt.legend(handles=legend_elements, loc='best')

print("analisis graf jaringn transportasi:")
print("===================================")
print(f"Semua node: {G.nodes()}")
print(f"Semua rute (edge): {G.edges()}")
print(f"Cut vertices yang ditemukan di graf: {cut_vertices}")
print(f"Terminal yang merupakan cut vertex: {terminal_cut_vertices}")

plt.show()