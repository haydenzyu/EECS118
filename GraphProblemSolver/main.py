# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
#import function.py as f
import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt
import function as fn

def main():
    graph_file = sys.argv[1]
    first_node = []
    second_node = []
    weight = []
    edge_color = []
    function_is_path = False
    function_color = False

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
                weight.append(row[2])
                edge_color.append(row[3])

    G = nx.Graph() #create a graph
    
    #adding edges & its colors
    for i in range(len(first_node)):
        G.add_edge(first_node[i], second_node[i], color=edge_color[i])

    edges = G.edges()
    arr = []
    for i in edges:
        arr.append(i)
    l = []
    l.append(A)
    l_c = []
    fn.find_paths(G, A, B, l, l_c, color_input, int(C), 0, A)
    #function_color = fn.color(G, color_input, 1)
    #color_of=nx.get_edge_attributes(G,'color')
    #print(color_of)

    #function_is_path = fn.is_path(arr, A, B)
    #print(function_is_path)
    nx.draw_random(G)
    #plt.show()
    
if __name__ == '__main__':
    main()
