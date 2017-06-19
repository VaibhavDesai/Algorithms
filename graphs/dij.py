
def dij(source):
    global n
    global visitedNodes
    visitedNodes.append(source)
    visitedCost = []
    visitedCost.append(0)
    travelCost = 0
    while(len(visitedNodes) != n+1):
        source, travelCost = nearestNeighbour(source,travelCost)
        visitedNodes.append(source)
        visitedCost.append(travelCost)

    return visitedNodes,visitedCost


def nearestNeighbour(source, travelCost):
    global costArray
    global n
    global distanceMatrix
    global visitedNodes
    nextNode = -1
    minCost = 999999
    for i in range(n):
        totalCost = distanceMatrix[source][i] + travelCost
        if totalCost < costArray[i]:
            costArray[i] = totalCost
    for i in range(n):

        if (costArray[i]+travelCost) < minCost and i not in visitedNodes:
            minCost = costArray[i]+travelCost
            nextNode = i
    return nextNode,minCost

t = int(input())
output = []
for i in range(t):
    inp = [int(x) for x in input().split()]
    n = inp[0]
    m = inp[1]
    visitedNodes =[]
    costArray = [999999]*n
    distanceMatrix = [[ 999999 for x in range(n)] for y in range(n)]
    for i in range(m):
        edge = [int(x) for x in input().split()]
        if distanceMatrix[edge[0]-1][edge[1]-1] > edge[2]:
            distanceMatrix[edge[0]-1][edge[1]-1] = edge[2]
            distanceMatrix[edge[1]-1][edge[0]-1] = edge[2]
    source = int(input())
    visitedNodes,visitedCost=dij(source-1)
    costArray.remove(costArray[source-1])
    output.append(costArray)


for j in range(t):
    for i in range(len(output[j])):
        print(output[j][i],end=' ')
    print()
