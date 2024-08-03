import pydotplus
from IPython.display import Image, display
import matplotlib.pyplot as plt
def BFS(start, graph, goal):
    visited = [] 
    explored = [start] 
    frontier = []  

    while explored:
        i = explored.pop(0) 

        if i == goal:
            visited.append(i)
            return visited
        
        for edge in graph:
            if edge[0] == i and edge[1] not in visited and edge[1] not in frontier:
                frontier.append(edge[1])
        
        if frontier:
            explored.append(frontier.pop(0))
            visited.append(i)
        else:
            visited.append(i)

    return 'Search Failed' 


def Adjacencyist(numberOfEdges):
    graph = []
    numberOfEdges = int(numberOfEdges)
    for i in range(numberOfEdges):
        n = input('Enter the two nodes connected : ').split()
        graph.append((n[0],n[1]))
    return graph

def visualization(graph):
    plt.figure(figsize=(8,8))
    MyGraph = pydotplus.Dot(graph_type='digraph')  
    for edge in graph:
        MyGraph.add_edge(pydotplus.Edge(str(edge[0]), str(edge[1])))
    MyGraph.write_png('graph.png')
    img = plt.imread('graph.png')
    plt.imshow(img)
    plt.axis('off')  
    plt.show()


number_of_edges = int(input('Enter number of edges : '))
starter = input('Enter the root : ')
target = input('Enter the goal : ')

graph = Adjacencyist(number_of_edges)
visualization(graph)
print(BFS(starter,graph,target))