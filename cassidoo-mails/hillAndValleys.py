# Given an integer array, 
# write a function hills(arr) and a function valleys(arr) 
# that return the number of hills and valleys, respectively, in the array. The integers represent heights!

def isValid(arr: list) -> bool:
    if len(arr) < 3: return False

def hills(arr: list) -> int:
    isValid(arr)

    pos = 1
    hill = 0
    start = False
    while pos < len(arr) - 1:
        if arr[pos - 1] < arr[pos]:
            start = True

        if start and arr[pos] > arr[pos + 1]:
            hill += 1
            if start: 
                start = False
        pos += 1

    return hill

def valleys(arr: list) -> int:
    isValid(arr)

    pos = 1
    valley = 0
    start = False
    while pos < len(arr) - 1:
        if arr[pos - 1] > arr[pos]:
            start = True

        if start and arr[pos] < arr[pos + 1]:
            valley += 1 
            if start:
                start = False   
        pos += 1

    return valley


# arr = [1,2,1]
# print(hills(arr)) # returns 1
# print(valleys(arr)) # returns 0

# arr = [1,0,1]
# print(hills(arr)) # returns 0
# print(valleys(arr)) # returns 1

# arr = [7,6,5,5,4,1]
# print(hills(arr)) # returns 0
# print(valleys(arr)) # returns 0

# arr = [3,4,1,1,6,5]
# print(hills(arr)) # returns 2
# print(valleys(arr)) # returns 1

arr = [1,4,5,5,4,6,7]
print(hills(arr)) # returns 1
print(valleys(arr)) # returns 1