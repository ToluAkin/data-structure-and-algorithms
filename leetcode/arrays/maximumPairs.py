
""" You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
- Remove both integers from nums, forming a pair.
- The operation is done on nums as many times as possible.

Return a 0-indexed integer array 
answer of size 2 where answer[0] is the number of pairs that are formed and
answer[1] is the number of leftover integers in nums after doing the 
operation as many times as possible.

Hint
What do we need to know to find how many pairs we can make? We need to know the frequency of each integer.
When will there be a leftover number? When the frequency of an integer is an odd number.
 """

from collections import Counter
from typing import List


def numberOfPairs(nums: List[int]) -> List[int]:
    count = Counter(nums)
    leftover = 0
    pairs = 0

    for key, val in count.items():
        remainder = val % 2

        if remainder == 0:
            pairs += val // 2

        if val >= 1 and remainder != 0:
            pairs += (val - 1) // 2
            leftover += 1
    
    return [pairs, leftover]


print(numberOfPairs([1,3,2,1,3,2,2]))
print(numberOfPairs([1, 1, 1, 1]))
print(numberOfPairs([1, 1]))
print(numberOfPairs([0]))
print(numberOfPairs([1, 2 , 3, 4, 5]))