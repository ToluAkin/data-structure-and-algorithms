def coinChange(coins, amount):
    purse = [amount + 1] * (amount + 1)
    purse[0] = 0

    for money in range(1, amount + 1):
        for coin in coins:
            if money - coin >= 0:
                # print(purse[money], purse[money - coin], money - coin, money, coin)
                purse[money] = min(purse[money], 1 + purse[money - coin])
    return purse[amount] if not purse[amount] == amount + 1 else -1


print(coinChange([1,2,5], 11))