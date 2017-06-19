def rangeBitCount(a,b):

    count = 0
    for i in range(a,b+1):
        count = count + countOnes(i)
    return count

def countOnes(n):

    count =0
    while n>0:
        if n&1 == 1:
            count = count+1
        n = n>>1
        
    return count

inp = [int(i) for i in input().split()]
print(rangeBitCount(inp[0],inp[1]))
