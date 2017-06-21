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

inp = [int(x) for x in input().split()]
minValue,item,initItem = inp[0],inp[1],inp[2]
print(transform(minValue,item,initItem))
