def solution(A):
    newA = set(A)
    lenA = len(A)

    if len(newA) < lenA:
        print(0)

    if max(A) == lenA:
        print(1)
    else:
        print(0)
solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8])