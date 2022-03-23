import math
# def numSquares(n):
#     pos = [n] * (n + 1)
#     pos[0] = 0

#     for target in range(1, n + 1):
#         for value in range(1, target + 1):
#             # print(target, value)
#             square = value * value
#             if target - square < 0:
#                 break
#             pos[target] = min(pos[target],  1 + pos[target - square])
#     print(pos)
#     return pos[n]
# print(numSquares(20))

def numSquares(n):
    rangeVal = math.isqrt(n)
    squares = [val * val for val in range(1, rangeVal + 1)]
    values = [n + 1] * (n + 1)
    values[0] = 0

    for i in range(1, n + 1):
        for square in squares:
            if i - square >= 0:
                values[i] = min(values[i], 1 + values[i - square])
    return values[n]

print(numSquares(24))
