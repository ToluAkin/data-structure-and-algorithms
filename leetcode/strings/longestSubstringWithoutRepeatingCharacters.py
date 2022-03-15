def lengthOfLongestSubstring(s):
    lenString = len(s)
    if lenString <= 1:
        return lenString
    
    longest = 0
    counter = 0
    new_dict = {}
    
    for value in s:
        if value in new_dict:
            if counter > longest:
                longest = counter
            counter = 1
            new_dict = {}
            new_dict[value] = value
        else:
            counter += 1
            new_dict[value] = value
        print(new_dict, counter)
    if counter > longest:
        longest = counter
    return longest


print(lengthOfLongestSubstring("dvdf"))
