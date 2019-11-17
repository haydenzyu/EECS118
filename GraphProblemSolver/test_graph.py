import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)
G.add_edges_from(H.edges)

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*
nx.draw_random(G)
plt.show()
