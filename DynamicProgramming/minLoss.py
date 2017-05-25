

def calMinLoss(n, p):

    minLoss = 10**16

    for i in range(n):
        for j in range(i+1,n):
            if(p[i]>p[j]) and (p[i]-p[j])<minLoss:
                minLoss = p[i]-p[j]
                
    print(minLoss)
n = int(input())
p = [ int(x) for x in input().split()]
calMinLoss(n,p)
