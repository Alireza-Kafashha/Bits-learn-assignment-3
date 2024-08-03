import pydotplus
from IPython.display import Image, display
import matplotlib.pyplot as plt
def DFS(start, graph, goal):
    visited = [] 
    frontier = [start]  
    while frontier:
        explored = frontier.pop()
        if explored == goal:
            visited.append(explored)
            return visited
        
        for edge in graph:
            if edge[0] == explored and edge[1] not in visited and edge[1] not in frontier:
                frontier.append(edge[1])
        visited.append(explored)

    return 'Search Failed' 


def Adjacencyist(numberOfEdges):
    graph = []
    numberOfEdges = int(numberOfEdges)
    for i in range(numberOfEdges):
        n = input('Enter the first node : ')
        m = input('Enter the second node : ')
        graph.append((n,m))
    return graph

def visualization(graph , dfs):
    plt.figure(figsize=(8,8))
    MyGraph = pydotplus.Dot(graph_type='digraph')  
    for edge in graph:
        MyGraph.add_edge(pydotplus.Edge(str(edge[0]), str(edge[1])))
    MyGraph.write_png('graph.png')
    img = plt.imread('graph.png')
    plt.imshow(img)
    plt.axis('off')  
    plt.title(f'DFS = {dfs}')
    plt.show()


number_of_edges = int(input('Enter number of edges : '))
starter = input('Enter the root : ')
target = input('Enter the goal : ')

graph = Adjacencyist(number_of_edges)
dfs = DFS(starter,graph,target)
print(dfs)
visualization(graph , dfs)
