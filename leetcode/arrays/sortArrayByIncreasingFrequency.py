from typing import Counter, List

def frequencySort(nums: List[int]) -> List[int]:
    count = Counter(nums)
    res = []
    sorted_dict = dict(sorted(count.items(), key=lambda x: (-x[1], x[0]), reverse=True))

    for cnt, val in sorted_dict.items():
        res.extend([cnt] * val)
    return res

# def frequencySort(nums: List[int]) -> List[int]:
#     count = Counter(nums)
#     res = []
#     reverseFreq = {k: v for k, v in reversed(dict(count))}
#     for cnt, val in reverseFreq.items():
#         res.extend([cnt] * val)
#     return res

print(frequencySort([1,1,2,2,2,3]))
print(frequencySort([2,3,1,3,2]))
print(frequencySort([-1,1,-6,4,5,-6,1,4,1]))