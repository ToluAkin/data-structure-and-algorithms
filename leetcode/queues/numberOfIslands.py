import collections

def numsIsland(grid):
    rows, columns = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        q.append((r, c))
        
        while q:
            ros, cols = q.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for row, col in directions:
                r, c = ros + row, cols + col

                if (r in range(rows) and c in range(columns) and grid[r][c] == "1"):
                    grid[r][c] = 2
                    q.append((r, c))

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "1":
                bfs(r, c)
                grid[r][c] = 2
                islands += 1
    return islands

print(numsIsland([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
