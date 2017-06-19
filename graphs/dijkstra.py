
def nearestNeighbour(n,distanceMatrix,source,travelCost,visitedNodes):

    minCost = 999
    nextNode = -1
    for i in range(n):
        if i == source:
            continue
        cost = distanceMatrix[source][i]
        if cost+travelCost < minCost and not in visitedNodes:
            minCost = cost+travelCost
            nextNode = i
            
    return nextNode,travelCost

def recNN(source,distanceMatrix,des):

    if nextNode == -1:
        return -1
    if nextNode == des:
        

def dij(source,n,distanceMatrix):

    visitedNodes = []
    output = [999]*n
    while nextNode != -1:
        nextNode, travelCost = nearestNeighbour(n,distanceMatrix,source,travelCost,visitedNodes)
        if nextNode == -1:
            visitedNodes.append(source)
            nextNode, travelCost = nearestNeighbour(n,distanceMatrix,source,travelCost,visitedNodes)
        source = nextNode
        output[nextNode] = travelCost
    for i in range(len(output)):
        if i == source:
            continue
        if output[i] == 999:
            print(distanceMatrix[source][i])
        else:
            print(output[i])

inp = [ int(x) for x in input().split(" ")]
n = inp[0]
ne = inp[1]
distanceMatrix = [[ 999 for x in range(n)] for y in range(n)]
for i in range(n):
    distanceMatrix[i][i] = 0
print(distanceMatrix)    
for i in range(ne):
    edge = [ int(x) for x in input().split(" ") ]
    distanceMatrix[edge[0]-1][edge[1]-1] = edge[2]
    distanceMatrix[edge[1]-1][edge[0]-1] = edge[2]
    
print(dij(distanceMatrix,n,0))
    
