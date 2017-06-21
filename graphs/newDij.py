def dij(source, distanceMatrix, n):

    visitedVertex = [False]*n
    distanceVertex = [999999]*n
    distanceVertex[source] = 0
    
    for k in range(n):
        visitedVertex[source] = True
        source = getSource(visitedVertex,distanceVertex)
        for i in range(n):
            if (distanceMatrix[source][i] != 999999) and visitedVertex[i] == False and (distanceVertex[source]+distanceMatrix[source][i] < distanceVertex[i]):
                distanceVertex[i] = distanceVertex[source]+distanceMatrix[source][i]
    return distanceVertex

def getSource(visitedVertex,distanceVertex):
    minDistance = 999999
    source = 0
    for i in range(len(distanceVertex)):
        if distanceVertex[i] < minDistance and visitedVertex[i] == False:
            minDistance = distanceVertex[i]
            source = i
    return source
        

t = int(input())
results = []
for i in range(t):

    inp = [int(x) for x in input().split()]
    n = inp[0]
    m = inp[1]
    distanceMatrix = [[999999 for i in range(n)] for j in range(n)]
    for j in range(m):
        edge = [int(x) for x in input().split()]
        if distanceMatrix[edge[0]-1][edge[1]-1] > edge[2]:
            distanceMatrix[edge[0]-1][edge[1]-1] = edge[2]
            distanceMatrix[edge[1]-1][edge[0]-1] = edge[2]

    source = int(input())
    distanceVertex = dij(source-1,distanceMatrix,n)
    del distanceVertex[source-1]
    results.append(distanceVertex)
    
for result in results:
    for r in result:
        if r == 999999:
            r = -1
        print(r, end=" ")
    print()
