# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
# C = user input, t = number of edges that has the Color k

import networkx as nx

def is_path(s, a, b): #returns true if s is a path between node a and node b
    #putting edges in a graph into an array
    edges = s.edges()
    arr = []
    for i in edges:
        arr.append(i)
    
    for i in arr:
        if int(i[0])==a or int(i[0])==b: #s[0]=fist node of edge s, #s[1]=second node of edge s
            if int(i[1])==b or int(i[1])==a:
                return True
            else:
                continue
        else:
            continue

    return False #the set doesn't have an edge from nodes a to b
'''
def total_weight(s, n):
    for i in s:
        total_weight += i['weight']

    if total_weight == n:
        return True
    else:
        return False

def no_nodes(s, n):
    nodes = []
    for i in s: #finds unique nodes in set of edges, 's'
        if i[0] in nodes:
            continue
        else:
            nodes.append(i[0])

        if i[1] in nodes:
            continue
        else:
            nodes.append(i[1])

    if len(nodes) == n:
        return True
    else:
        return False

'''
def color(s, k, n): #returns true if number of nodes of color k in s is n
    cnt = 0
    #putting edges in a graph into an array
    edges = s.edges()
    arr = []
    for i in edges:
        arr.append(i)

    #count how many edges have the color k
    for i in arr:
        if s.edges[i[0],i[1]]['color'] == k:
            cnt+=1
        else:
            continue
    
    #result
    if cnt == n:
        return True
    else:
        return False