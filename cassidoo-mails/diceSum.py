""" Imagine you have n dice, and each die has m faces on it (so the numbers are from 1 to m). 
Write a function where, given an integer target, it returns the number of possible ways to 
roll the dice to get the sum of target face up. You can safely assume m will never be 
larger than 20 (so you don't have to deal with mega huge numbers). """


def diceSum(n, m, target):
    if target <= 0:
        return 0
    if n == 1:
        return 1 if target <= m else 0
    return sum(diceSum(n - 1, m, target - i) for i in range(1, m + 1))

n = 1
m = 6
print(diceSum(n,m,3)) # 1 // there is only one die, and one way to get 3
print(diceSum(2,m,7)) # 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
print(diceSum(2, 6, 6)) # 1+5, 2+4, 3+3, 4+2, 5+1
print(diceSum(2, 6, 12)) # 6+6