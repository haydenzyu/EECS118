import sys
import pandas
import function
import csv

#Import Graph CSV
sheet_name = sys.argv[1]
graph = pandas.read_csv(sheet_name, names=['Node1','Node2','Weight','Color'])

#Get the needed inputs from the user
max_deg = int(input('Enter the the max degree value (max degree < value): '))
color = input('Enter the color: ')
max_color = int(input('Enter the the maximum '+color+' edges value (max color < value): '))

#Create a list of all nodes in the graph
node_list = []
for node in graph['Node1']:
    if node not in node_list:
        node_list.append(node)
for node in graph['Node2']:
    if node not in node_list:
        node_list.append(node)

#Find all paths in the Graph
max_vert = max(node_list)+1
p = function.Paths(max_vert)
for x in range(0, len(graph)):
    p.edgeAdd(graph['Node1'][x], graph['Node2'][x]) 
p.findAllPaths(node_list)

#Check each path found and see if it meets the predicate conditions
path_name = []
path_number = 1
myFile = open('results.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    for s in p.listOfpaths:
        if function.is_path(s):
            for md in range(1, max_deg):
                if function.max_degree(s,md,graph):
                    for mc in range(0, max_color):
                        if function.color(s,color,mc,graph):
                            path_name = ['Path '+str(path_number)+':']
                            writer.writerow(path_name)
                            writer.writerows(s)
                            path_number += 1


