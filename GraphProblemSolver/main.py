#   Hayden Yu, Sienna Ballot    #
#   EECS 118 Graph Term Project #
#   December 5, 2019            #
# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
# C = user input, t = number of edges that has the Color k

import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt
import function as fn

def main():
    graph_file = sys.argv[1]
    first_node = []
    second_node = []
    edge_weight = []
    edge_color = []

    print("Input A:")
    A = input()
    print("Input B:")
    B = input()
    print("Input C:")
    C = input()
    print("Input Color:")
    color_input = input()
    print(A, B, C, color_input)
    #reading csv file
    with open(graph_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
                first_node.append(row[0])
                second_node.append(row[1])
                edge_weight.append(row[2])
                edge_color.append(row[3])

    G = nx.Graph() #create a graph
    
    #adding edges & its colors
    for i in range(len(first_node)):
        G.add_edge(first_node[i], second_node[i], color=edge_color[i], weight=edge_weight[i])

    edges = G.edges()
    arr = []
    for i in edges:
        arr.append(i)
    l = []
    l.append(A)
    l_c = []
    fn.find_paths(G, A, B, l, l_c, color_input, int(C), 0, A)
    nx.draw_random(G)
    #plt.show() #showing the graph in a new window
    
if __name__ == '__main__':
    main()
