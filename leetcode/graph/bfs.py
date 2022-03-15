marked = [False] * len(graph)
def bfs(graph, vertex):
    queue = [vertex]
    while len(queue) > 0:
        vertex = queue.pop(0)
        if not marked[vertex]:
            visit(vertex)
            marked[vertex] = True
            for i in graph.neighbours(vertex):
                if not marked[i]:
                    queue.append(i)
