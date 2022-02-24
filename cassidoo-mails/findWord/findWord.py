def findWord(A, word):
    index = 0
    exist = 0

    for element in A:
        for i, letter in enumerate(element):
            if letter == word[index] and index < len(word) and not exist:
                element[i] = '*'
                exist += 1
        index += 1
        exist = 0
    return A
print(findWord([['a','a','q','t'], ['x','c','w','e'], ['r','l','e','p']], 'ace'))