""" Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words 
with the same frequency by their lexicographical order.
"""

from collections import Counter
from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:
    countDict = Counter(words) 

    # sort words with same frequency alphabetically
    sortDictByFrequency = sorted(countDict.most_common(), key=lambda x: (-x[1], x[0]))
    res = []

    for tuple_i in sortDictByFrequency[:k]:
        res.append(tuple_i[0])
    return res

# print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))
# print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
print(topKFrequent(["i","love","leetcode","i","love","coding"], 3))