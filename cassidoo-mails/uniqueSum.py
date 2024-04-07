""" Given an array of numbers, add all of the values together but only if the number doesn't repeat a digit. """

def uniqueSum(arr):
    sum = 0
    for i in arr:
        if len(set(str(i))) == len(str(i)):
            sum += i
    return sum

# print(uniqueSum([1,2,3])) # 6
# print(uniqueSum([11,22,33])) # 0
# print(uniqueSum([101,2,3])) # 5
# print(uniqueSum([167,2,3])) # 172
