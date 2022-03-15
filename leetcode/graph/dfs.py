from inspect import stack


marked = [False] * len(graph)
def dfs(graph, value):
    visit(value)
    marked[value] = True
    for i in graph.neighbours(value):
        if not marked[i]:
            dfs(graph, i)

def dfs_iter(graph, value):
    stack = [value]
    while len(stack) > 0:
        value = stack.pop()
        if not marked[value]:
            visit(value)
            marked[value] = True
            for i in graph.neighbours(value):
                if not marked[i]:
                    stack.append(i)

def dfs_stack(start):
    new_stack = stack()
    seen = set()

    new_stack.append(start)

    while len(new_stack) > 0:
        curr = new_stack.pop()

        if not seen.contains(curr):
            seen.add(curr)
            print(curr)
        
        