import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt

graph_file = sys.argv[1]
first_node = []
second_node = []
weight = []
edge_color = []
function_is_path = False
function_color = False

with open(graph_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
            first_node.append(int(row[0]))
            second_node.append(int(row[1]))
            weight.append(row[2])
            edge_color.append(row[3])

G = nx.Graph() #create a graph

#adding edges & its colors
for i in range(len(first_node)):
    G.add_edge(first_node[i], second_node[i], color=edge_color[i])

nx.draw_random(G)
#plt.show()

x = list(G.neighbors(1))
print(x[1])
