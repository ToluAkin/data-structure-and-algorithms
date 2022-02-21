def solution(A):
    # if len(A) <= 1:
    #     return len(A)
    # A.sort()
    # count = 1
    # for i in range(1, len(A)):
    #     if A[i-1] != A[i]:
    #         count += 1
    # print(count)
    # return count
    newA = set(A)
    print(len(newA))
    return len(newA)
solution([2, 1, 1, 2, 3, 1])