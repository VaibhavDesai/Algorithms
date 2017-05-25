
def calMaxSum(n,a):

    m = [0]*n
    m[0] = a[0]

    for i in range(1,n):
        if(i-2 == -1):
            m[i] = max(m[i-1],0+a[i])
        else:
            m[i] = max(m[i-1],m[i-2]+a[i])
        
    return m[n-1]
        
n = int(input())
a = [int(x) for x in input().split()]

print(calMaxSum(n,a))
