def percentageLetter(s, letter) -> int:
    countLetter = 0
    pos = 0
    lenString = len(s)
    
    while pos < lenString:
        if letter == s[pos]:
            countLetter += 1
        pos += 1
    
    if countLetter == 0:
        return countLetter
    
    percentageOfLetter = countLetter/lenString *100
    return int(percentageOfLetter // 1)

# print(percentageLetter("foobar", "o"))
# print(percentageLetter("jjjj", "k"))
# print(percentageLetter("sgawtb", "s"))
print(percentageLetter("kue", "e"))