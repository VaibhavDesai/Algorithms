
def equal(arr):

    minValue = min(arr)

    noOfOps = 0
#    for item in arr:
#        if item != minValue:
#            noOfOp = noOfOp+ transform(minValue,item,item)
    delta1 = [x-minValue for x in arr]
    noOfOps1 = getOps(delta1)
    delta2 = [x-minValue-1 for x in arr if(x-minValue-1)>0]
    delta3 = [x-minValue-2 for x in arr if(x-minValue-2)>0]
    noOfOps2 = getOps(delta2)
    noOfOps3 = getOps(delta3)
    b = [noOfOps1,noOfOps2,noOfOps3]
    return min(i for i in b if i >0)

def getOps(delta):

    ops = 0
    for ele in delta:
        e = ele//5
        f = (ele%5)//2
        g = ((ele%5)%2)//1
        ops = ops+e+f+g
    return ops
def transform(minValue,item,initItem):

    if(item < minValue):
        return 0
    if(item == minValue):
        return 1

    n1 = transform(minValue,item-5,initItem)
    n2 = transform(minValue,item-2,initItem)
    n3 = transform(minValue,item-1,initItem)
    if(item == initItem):
        a = [n1,n2,n3]
        return min(i for i in a if i>0)
    else:
        return n1+n2+n3
    
t = int(input())
ans = []

for i in range(t):
    size = int(input())
    inp = [int(x) for x in input().split()]
    ans.append(equal(inp))


for a in ans:
    print (a)
