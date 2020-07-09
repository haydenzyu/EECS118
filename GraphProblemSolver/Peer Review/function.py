from collections import defaultdict

#Determines if the provided set of edges (s) is a simple path or not
def is_path(s):
    for x in range(0, len(s)-1):
        if s[x][1] != s[x+1][0]:
            return False
    temp_list = []
    temp_list.append(s[0][0])
    for t in s:
        if t[1] not in temp_list:
            temp_list.append(t[1])
        else:
            return False
    return True

#Determines if the max degree of the nodes in the path is equal to n
def max_degree(s, n, G):

    node = s[0][0]
    degree_node = 0
    for x in G['Node1']:
        if x == node:
            degree_node += 1
    for x in G['Node2']:
        if x == node:
            degree_node += 1

    max_deg = degree_node


    for x in range(0, len(s)):
        node = s[x][1]
        degree_node = 0
        for x in G['Node1']:
            if x == node:
                degree_node += 1
        for x in G['Node2']:
            if x == node:
                degree_node += 1

        if degree_node > max_deg:
            max_deg = degree_node
    

    if max_deg == n:
        return True
    else:
        return False
    
#Determines if the number of edges in the path with color k is equal to n
def color(s, k, n, G):
    num_color = 0
    for i in range(0, len(s)):
        for x in range(0, len(G)):
            if s[i] == (G['Node1'][x],G['Node2'][x]) or s[i] == (G['Node2'][x],G['Node1'][x]):
                if G['Color'][x] == k:
                    num_color += 1

    if num_color == n:
        return True
    else:
        return False

#Takes a path in node form [1,2,3] and returns the path in edge form [(1,2),(2,3)]
def node_to_edge(nodelist):
    edgelist = []
    for x in range(0, len(nodelist)-1):
        edgelist.append((nodelist[x],nodelist[x+1]))
    return edgelist



# Find all paths from a source to destination.  
class Paths: 
   
    def __init__(self,max_vert): 
        #Set number of max value node
        self.V= max_vert

        #Save all paths
        self.listOfpaths = []
          
        #Dictionary to store graph 
        self.graph = defaultdict(list)
   
    #Add an edge to the graph 
    def edgeAdd(self,u,v): 
        self.graph[u].append(v)
        self.graph[v].append(u)
   
    #Finds all paths from 'u' to 'd'
    def findAllPathsfromto(self, s_node, d_node, visited, path): 
  
        #Mark the current node as visited and store in path 
        visited[s_node]= True
        path.append(s_node) 
  
        #If current vertex is same as destination then save path
        if s_node == d_node: 
            self.listOfpaths.append(node_to_edge(path))
        else:#Current vertex is not equal to destination, go through vertices adjacent to the current vertex 
            for new_node in self.graph[s_node]: 
                if visited[new_node] == False: 
                    self.findAllPathsfromto(new_node, d_node, visited, path) 
                      
        #Remove the current vertex from path list and mark the vertex as unvisited 
        path.pop() 
        visited[s_node]= False


    def findAllPaths(self, nodes):
        #Set all vertices as unvisited, used in called function
        visited =[False]*(self.V) 
        #List to store path, used in called function 
        path = [] 
        for s_node in nodes:
            for d_node in nodes:
                if s_node != d_node:
                    #Calling the function to find all paths from s to d
                    #This function is being called for all possible combinations of nodes
                    self.findAllPathsfromto(s_node, d_node, visited, path)
