def isAlphabeticPalindrome(code):
# Write your code here
# Extract only letters
# Convert to lowercase
# Compare sequence forward and backward

# Extract only characters
    onlyLetters = ''.join(char for char in code if char.isalpha())

# Convert to lowercase
    lowercaseLetters = onlyLetters.lower()

# Compare sequence forward and backward
    isPalindrome = lowercaseLetters == lowercaseLetters[::-1]

# Print the result
    print(isPalindrome)
    return isPalindrome

# Example test cases
isAlphabeticPalindrome("abc123!@#XYZ")  # expected output: False
isAlphabeticPalindrome("A1b2B!a") # expected output: True