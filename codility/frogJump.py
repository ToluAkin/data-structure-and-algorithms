import math
def solution(X, Y, D):
    # counter = 0
    # jumpTotal = 0

    # while jumpTotal < Y:
    #     if counter > 0:
    #         jumpTotal += D
    #     else:
    #         jumpTotal = X + D
    #     counter += 1

    # print(counter)
    baseValue = Y - X
    print(math.ceil(baseValue / D))
solution(10, 85, 30)