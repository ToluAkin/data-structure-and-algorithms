def isNonTrivialRotation(s1, s2):
    # Write your code here
    len1 = len(s1)
    len2 = len(s2)

    if len1 != len2 or len1 == 0 or s1 == s2:
        print(0)
        return False
    
    start = 0
    while start < len1:
        rotated = s1[start:] + s1[:start]
        if rotated == s2:
            print(1)
            return True
        start += 1
    print(0)
    return False

# isNonTrivialRotation("abc", "bca")  # expected output: 1
# isNonTrivialRotation("abcde", "cdeab")  # expected output: 1
# isNonTrivialRotation("a", "a")  # expected output: 0
# isNonTrivialRotation("a", "b")  # expected output: 0
# isNonTrivialRotation("mnopqr", "pqrmno")  # expected output: 1
# isNonTrivialRotation("xyz", "zxy")  # expected output: 1
# isNonTrivialRotation("hello", "lloeh")  # expected output: 0