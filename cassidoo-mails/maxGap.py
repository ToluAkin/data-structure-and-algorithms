'''Given an integer array arr, return the maximum difference between two successive elements in arr's sorted form. 
Return 0 if there's 0 or 1 elements.'''

def maxGap(elements: list) -> int:
    len_elements = len(elements)

    if len_elements < 1:
        return 0
    
    index = 1
    max_diff = 0
    while index < len_elements:
        diff = elements[index] - elements[index-1]
        if diff > max_diff:
            max_diff = diff
        index += 1
    return max_diff

# print(maxGap([3,6,9,1,2]))
print(maxGap([3,6,6,9,15]))