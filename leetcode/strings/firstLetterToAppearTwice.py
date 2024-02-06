def repeatedCharacter(s):
    characterDict = {}
    
    for i in range(len(s)):
        if s[i] in characterDict: # check if a key exist in a dictionary
            return s[i]
        else:
            characterDict[s[i]] = i

print(repeatedCharacter("abccbaacz"))
print(repeatedCharacter("abcdd"))