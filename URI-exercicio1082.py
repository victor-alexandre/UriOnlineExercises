#Add the vertices in the graph(dictionary)
def add_to_graph(vertex1, vertex2, graph):
    if vertex1 in graph:            
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = [vertex2] 

    if vertex2 in graph:            
        graph[vertex2].append(vertex1)
    else:
        graph[vertex2] = [vertex1]      
           
#Depth search
def dfs(node, graph, component, visited_nodes):
    visited_nodes[node] =  True
    component.append(node)
    #Get all vertices connected with the given node
    for element in graph[node]:
        if not visited_nodes[element]:
            dfs(element, graph, component, visited_nodes)

#Return a list of connected components.
def connected_components(graph):
    components = []

    #Initializing the structure that will maintain visited and unvisited nodes
    visited_nodes = {}
    for vertex, edges in graph.items():
        visited_nodes[vertex] = False

    for vertex, visited in visited_nodes.items():
        component = []
        if not visited:
            dfs(vertex, graph, component, visited_nodes)

        #To avoid inserting empty lists in the components
        if len(component) != 0:
            components.append(component)

    return components

#Sort the list of lists in ascending order.
def sort_components(components):
    for component in components:
        component = component.sort()
    
    return sorted(components)


####Begin of execution###
test_cases = int(input())

for i in range(test_cases):
    line = input()
    line = [int(x) for x in line.split()]
    vertices = line[0]
    edges = line[1]

    #Create a list with all existing vertices(represented as letters of alphabet) in the graph 
    vertices = [(chr)(97 + i) for i in range(vertices)]

    graph = {}
    for j in range(edges):
        line = input()
        vertex1, vertex2 = line.split()
        add_to_graph(vertex1, vertex2, graph)

    #Add the vertices that was not mentioned in the edges 
    for vertex in vertices:
        if vertex not in graph:
            graph.update({vertex:[]})

    #Get the components and sort them.
    components = sort_components(connected_components(graph))

    print("Case #%d:" % (i+1))
    for component in components:
        print(*component, sep=',', end=',\n')
        
    print("%d connected components\n" %   len(components))      