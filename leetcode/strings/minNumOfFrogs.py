""" You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs,
that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
Return the minimum number of different frogs to finish all the croaks in the given string.
A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. 
The frogs have to print all five letters to finish a croak. 
If the given string is not a combination of a valid "croak" return -1. """

from collections import Counter

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    dictCroak = Counter(croakOfFrogs)
    
    if croakOfFrogs[0] != "c" or croakOfFrogs[-1] != "k" or len(set(dictCroak.values())) != 1:
        return -1
     
    active_frogs = 0  # Count of active frogs

    # Initialize counters for each letter
    c_count, r_count, o_count, a_count, k_count = 0, 0, 0, 0, 0

    # Iterate through the input string
    for key in range(len(croakOfFrogs)):
        char = croakOfFrogs[key]

        if char == 'c':
            c_count += 1
            if active_frogs > 0:
                active_frogs -= 1
        elif char == 'r':
            r_count += 1

            if r_count > c_count:
                return -1
        elif char == 'o':
            o_count += 1

            if o_count > r_count:
                return -1
        elif char == 'a':
            a_count += 1

            if a_count > r_count or a_count > o_count:
                return -1
        elif char == 'k':
            k_count += 1
            active_frogs += 1

            if k_count > r_count or k_count > o_count or k_count > a_count:
                return -1
        else:
            # Invalid character found
            return -1

    return active_frogs
  
print(minNumberOfFrogs("croakcroak")) # 1
print(minNumberOfFrogs("coark")) # -1
print(minNumberOfFrogs("crcoakroak")) # 2
print(minNumberOfFrogs("aoocrrackk")) # -1
print(minNumberOfFrogs("croakcrook")) # -1
print(minNumberOfFrogs("cccrorakrcoakorakoak")) # 3
print(minNumberOfFrogs("croacroacrckckoakroakroak")) # 4
print(minNumberOfFrogs("crroakcoak")) # -1