'''
Imagine you have a collection of N wines placed next to each other on a shelf. For simplicity, let's number the wines from left to right as they are standing on the shelf with integers from 1 to N, respectively. The price of the ith wine is pi. (prices of different wines can be different).
Because the wines get better every year, supposing today is the year 1, on year y the price of the ith wine will be y*pi, i.e. y-times the value that current year.
You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this year. One more constraint - on each year you are allowed to sell only either the leftmost or the rightmost wine on the shelf and you are not allowed to reorder the wines on the shelf (i.e. they must stay in the same order as they are in the beginning).
You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order?
'''

import time

def calPrice(year, start, end):

    if(start > end):
        return 0

    price1 = calPrice(year+1,start+1,end) + year*P[start]

    price2 = calPrice(year+1,start,end-1) + year*P[end]
    
    return max(price1,price2)


def DPsolution(start,end):

    if(start > end):
        return 0

    if(ans[start][end]!=-1):
        return ans[start][end]

    year = len(P) - (end-start+1) + 1
    ans[start][end] = max(
        DPsolution(start+1,end) + year*P[start],
        DPsolution(start,end-1) + year*P[end])
    
    return ans[start][end]    
P = [int(x) for x in input().split()]

ans = [[ -1 for x in range(len(P))] for y in range(len(P))]
start  = time.time()
print(str(DPsolution(0,len(P)-1)))
print("time taken by DP is :"+str(time.time()-start))
start = time.time()
print(str(calPrice(1,0,len(P)-1)))
print("time taken by recurssion is :"+str(time.time()-start))
