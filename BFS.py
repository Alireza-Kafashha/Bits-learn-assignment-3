import pydotplus
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

def AdjacencyList(numberOfEdges):
    graph = []
    for i in range(numberOfEdges):
        n = input('Enter the first node :')
        m = input('Enter the second node :')
        graph.append((n,m))
    plt.figure(figsize=(8,8))
    MyGraph = pydotplus.Dot(graph_type='digraph')  
    for edge in adjacency_list:
        MyGraph.add_edge(pydotplus.Edge(str(edge[0]), str(edge[1])))
    img = Image(graph.create_png())
    display(img)
        