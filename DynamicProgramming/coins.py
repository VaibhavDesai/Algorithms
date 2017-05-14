import time

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


def DpChange(money, coins):
    minChange = [999]*1000
    minChange[0] = 0

    for i in range(1,money+1):

        minValue = 999

        for coin in coins:
            if( i >= coin):
                value = minChange[i-coin] + 1
                if(value < minValue):
                    minValue = value
                    minChange[i] = minValue

    return minChange[money]



money =int(input("Enter money \n"))

coins = [int(x) for x in input().split()]

start = time.time()
print("MinChange using Dynamic Programming:"+str(DpChange(money,coins)))
print("Time taken :" +str(time.time() - start))

start = time.time()
print("Min Chnage using recersion:"+str(minChange(money,coins)))
print("Time taken :"+str(time.time()-start))
