# 11. find s where is_path(s, A, B) and color(s, Color, t) and t>C
# C = user input, t = number of nodes that has the Color k

import networkx as nx

def is_path(s, a, b): #returns true if s is a path between node a and node b
    for i in s:
        if i[0]==a or i[0]==b: #s[0]=fist node of edge s, #s[1]=second node of edge s
            if i[1]==b or i[1]==a:
                continue
            else:
                return False
        else:
            return False

    return True #all edges have nodes a and b
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
    nodes = []
    for i in s: #edges in set 's'
        if i[0] in nodes: #if first node of edge is unique
            continue
        else: #if not add node to the list
            nodes.append(i[0])
            if i[0]['color'] == k: #increase counter if color of the node is k
                cnt++
            else:
                continue
        
        if i[1] in nodes: #check second node of the edge in set 's'
            continue
        else:
            nodes.append(i[1])
            if i[0]['color'] == k: 
                cnt++
            else:
                continue

    if cnt == n:
        return True
    else:
        return False
    
        
