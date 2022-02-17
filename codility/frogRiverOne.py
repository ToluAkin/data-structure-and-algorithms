def solution(X, A):
    position = {}

    for i in range(len(A)):
        position[A[i]] = i

        if len(position) == X:
            return i

    return -1
solution(5, [1, 3, 1, 4, 2, 3, 5, 4])