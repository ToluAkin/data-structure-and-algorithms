def guessNumber(n) -> int:
    left = 1
    right = n

    while True:
        num = (left + right) // 2

        if guess(num) == 0:
            return num
        elif guess(num) == -1:
            right = num - 1
        else:
            left = num + 1
