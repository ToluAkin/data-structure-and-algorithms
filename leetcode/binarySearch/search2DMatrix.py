def searchMatrix(matrix, target):
    matrixRows = len(matrix)
    matrixCols = len(matrix[0])

    topMatrix = 0
    bottomMatrix = matrixRows - 1

    while topMatrix <= bottomMatrix:
        matchedRow = (topMatrix + bottomMatrix) // 2

        if target > matrix[matchedRow][-1]:
            topMatrix = matchedRow + 1
        elif target < matrix[matchedRow][0]:
            bottomMatrix = matchedRow - 1
        else:
            break

    if not topMatrix <= bottomMatrix:
        return False

    left = 0
    right = matrixCols - 1

    while left <= right:
        mid = (left + right) // 2

        if matrix[matchedRow][mid] == target:
            return True
        elif matrix[matchedRow][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
