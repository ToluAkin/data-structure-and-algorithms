from collections import deque

def openLock(deadends, target):
    if "0000" in deadends:
        return -1
        
    q = deque()
    visited = set(deadends)
    q.append(["0000", 0])

    def children(lock):
        childLocks = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            childLocks.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            childLocks.append(lock[:i] + digit + lock[i+1:])
        return childLocks

    while q:
        lock, turns = q.popleft()
        if lock == target:
            return turns
        for child in children(lock):
            if child not in visited:
                q.append([child, turns + 1])
                visited.add(child)
    return -1
print(openLock(["0201","0101","0102","1212","2002"], "0202"))
print(openLock(["8888"], "0009"))
print(openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))
