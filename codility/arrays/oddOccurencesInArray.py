def solution(A):
    # numDict = {}
    # for i in range(len(A)):
    #     if A[i] in numDict:
    #         numDict[A[i]] += 1
    #     else:
    #         numDict[A[i]] = 0
    # for key, value in numDict.items():
    #     if not value % 2 or value == 0:
    #         return key
    answer = 0
    for value in A:
        answer = answer ^ value
    print(answer)
solution([9, 3, 9, 3, 9, 7, 9])