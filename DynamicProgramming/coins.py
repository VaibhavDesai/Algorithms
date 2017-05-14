def minChange(money,coins):
    
    if(money == 0):
        return 0

    minCoins = 999
    for coin in coins:
        if(money >= coin):
            change = minChange(money-coin,coins)+1

            if(change < minCoins):
                minCoins = change

    return minCoins


money =int(input("Enter money"))

coins = [int(x) for x in input().split()]

print("Min Chnage:"+str(minChange(money,coins)))
