
def pairs(arr,k):
    l = 0
    r = 1
    count = 0
    arr.sort()
    while(l<=r and r < len(arr)):
        if(arr[r] - arr[l]) == k:
            count = count+1
            l = l+1
        elif(arr[r] - arr[l])< k:
            r = r+1
        else:
            l = l+1
    return count


inp = [int(x) for x in input().split()]
n, k = inp[0],inp[1]
arr = [int(x) for x in input().split()]
print(pairs(arr,k))
    
