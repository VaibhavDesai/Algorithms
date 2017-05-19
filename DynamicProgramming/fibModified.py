#https://www.hackerrank.com/challenges/fibonacci-modified

import time


def fib(n):
    if(n == 1):
        return t1
    if(n == 2):
        return t2
    
    return fib(n-2)+(fib(n-1)**2)

def DPfib(n):
    f = [0 for x in range(n+1)]
    f[1] = t1
    f[2] = t2
    for i in range(3,n+1):
        f[i] = f[i-2] + (f[i-1]**2)
    return f[n]

elements = [int(x) for x in input().split()]
t1 = elements[0]
t2 = elements[1]
n = elements[2]
start = time.time()
print(str(DPfib(n)))
print("Time taken by DP: "+str(start-time.time()))
start = time.time()
print(fib(n))
print("Time taken by recussion: "+str(start-time.time()))


