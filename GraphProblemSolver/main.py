# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
#import function.py as f
import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt

def main():
    #graph_file = sys.argv[1]
    graph_file = "C:\\Users\\hayde\\Documents\\GitHub\\EECS118\\GraphProblemSolver\\graph.csv"
    first_node = []
    second_node = []
    weight = []
    color = []
    with open(graph_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
                first_node.append(row[0])
                second_node.append(row[1])
                weight.append(row[2])
                color.append(row[3])

    G = nx.Graph()
    cnt = 0
    for i in first_node:
        G.add_node(i) 
    for i in second_node:
        if i in first_node:
            continue
        else:
            G.add_node(i)
    for i in range(len(first_node)):
        G.add_edge(first_node[i], second_node[i])
        G.edges[first_node[i], second_node[i]]['color']=color[i]
        
                
    #print(first_node, second_node, weight, color)
    color_of=nx.get_edge_attributes(G,'color')
    print(color_of)
    nx.draw_random(G)
    plt.show()
    
if __name__ == '__main__':
    main()
