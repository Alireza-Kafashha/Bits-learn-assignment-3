import pydotplus
from IPython.display import Image, display
import matplotlib.pyplot as plt
def BFS(start,graph,goal):

    visited : []
    explored : [start]
    frontier: []

    for i in explored:

        for j in range(len(graph)):

            if graph[j][0] == i & graph[j][1] in visited == False :

                frontier.append(graph[j][1])

        explored.append(frontier[0])

        visited.append(explored[0])

        explored = explored[1:]

        frontier = frontier[1:]

        if visited[-1] == goal:
            return visited

def Adjacencyist(numberOfEdges):
    graph = []
    numberOfEdges = int(numberOfEdges)
    for i in range(numberOfEdges):
        n = input('Enter the first node : ')
        m = input('Enter the second node : ')
        graph.append((n,m))
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