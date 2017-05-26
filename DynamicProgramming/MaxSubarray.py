
def maxContigous(n,array):

    pb = array[0]
    maxSum=array[0]
    for i in range(n):
        pb = max(pb+array[i],array[i])
        maxSum = max(maxSum,pb)
    return maxSum
                

def maxNonContigous(n,array):
    maxSum = 0
    for element in array:
        if element > 0:
            maxSum = maxSum +element
            
    return maxSum


t= int(input())
contigousList = []
nonContigousList = []
for test in range(t):
    n = int(input())
    array = [int(x) for x in input().split()]
    contigousList.append(maxContigous(n,array))
    nonContigousList.append(maxNonContigous(n,array))

for i in range(len(contigousList)):
    print(str(contigousList[i])+" "+str(nonContigousList[i]))
    
