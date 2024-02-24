""" You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false. """

from collections import Counter
from typing import List


def divideArray(nums: List[int]) -> bool:
    count = Counter(nums)

    for val in count.values():
        if val % 2 != 0:
            return False
    return True

print(divideArray([3,2,3,2,2,2]))
print(divideArray([1,2,3,4]))