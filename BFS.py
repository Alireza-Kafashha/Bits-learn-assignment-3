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



