def efficientRoadNetwork(n, roads):

    for i in range(n):
        for j in range(i+1,n):
            if not isTraversing(i,j,roads):
                return False
                
    return True

def isTraversing(source,destination,roads):
    pitStops = []
    result = False
    for road in roads:
        if road[0] == source:
            pitStops.append(road[1])
        elif road[1] == source:
            pitStops.append(road[0])

    for pitStop in pitStops:
        for road in roads:
            if road[0] == pitStop and road[1] == destination:
                return True
            elif road[1] == pitStop and road[0] == destination:
                return True
            else:
                result = False
    return result
