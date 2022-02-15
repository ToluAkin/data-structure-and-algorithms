def solution(A):
    # A.sort()
    lengthOfA = len(A)

    # if lengthOfA:
    #     if not A[0] == 1:
    #         return 1
        
    #     if not A[-1] == lengthOfA + 1:
    #         return lengthOfA + 1

    #     if lengthOfA == 1:
    #         return lengthOfA + 1

    #     for i in range(len(A)):
    #         if not A[i] == i + 1:
    #             print(i + 1)
    # else:
    #     if lengthOfA == 0:
    #         return 1
    #     else:
    #         return 2

    originalSum = sum(list(range(1, lengthOfA + 2)))
    arraySum = sum(A)
    print(originalSum - arraySum)
solution([2, 6 , 3, 1, 4, 5, 8])