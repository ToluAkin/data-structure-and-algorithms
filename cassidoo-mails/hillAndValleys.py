# Given an integer array, 
# write a function hills(arr) and a function valleys(arr) 
# that return the number of hills and valleys, respectively, in the array. The integers represent heights!

def hills(arr: list) -> int:
    pos = 1
    hill = 0
    left = 0

    while pos < len(arr) - 1:
        if arr[pos] == arr[pos + 1] and left != arr[pos]:
            left = arr[pos - 1]
        elif arr[pos] != arr[pos + 1]:
            left = 0

        if arr[pos - 1] < arr[pos] > arr[pos + 1] or left < arr[pos - 1] == arr[pos] > arr[pos + 1]:
            hill += 1
        
        pos += 1

    return hill

def valleys(arr: list) -> int:
    pos = 1
    valley = 0
    left = 0

    while pos < len(arr) - 1:
        if arr[pos] == arr[pos + 1] and left != arr[pos]:
            left = arr[pos - 1]

        elif arr[pos] != arr[pos + 1]:
            left = 0

        if arr[pos - 1] > arr[pos] < arr[pos + 1] or left > arr[pos - 1] == arr[pos] < arr[pos + 1]:
            valley += 1    
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