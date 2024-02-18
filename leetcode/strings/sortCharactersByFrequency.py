from collections import Counter, defaultdict


def frequency_sort(s: str) -> str:
    string_freq = {}
    sorted_string = ""

    for char in s:
        string_freq[char] = string_freq.get(char, 0) + 1

    # Sort the dictionary by frequency (ascending order) and then by character
    sorted_dict = dict(sorted(string_freq.items(), key=lambda x: (-x[1], x[0])))

    for letter in sorted_dict:
        sorted_string += (letter * sorted_dict[letter])

    return sorted_string


def frequencySort(s: str) -> str:
    count = Counter(s) # Creates a dictionary with the count of each string e.g ({a: 1, b: 2})
    buckets = defaultdict(list) # Creates a class list
    
    for char, cnt in count.items(): # Fills the bucket as a dictionary and the values as a list. It groups all the same values together e.g ({1: ["a", "c"], 2: ["b", "d"]})
        buckets[cnt].append(char)

    res = []
    for i in range(len(s), 0, -1):
        for c in buckets[i]: # Creates an empty array in for the index that does not exist in bucket
            res.append(c * i)
    return "".join(res)

# print(frequency_sort("cccaaa"))
# print(frequency_sort("Aabb"))
# print(frequency_sort("fast21st"))
# print(frequency_sort("tree"))
print(frequencySort("football"))