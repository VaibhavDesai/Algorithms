def newRoadSystem(roadRegister):
    inAndOut = [0]*(len(roadRegister))
    for i in range(len(roadRegister)):
        for j in range(len(roadRegister)):
            if(roadRegister[i][j] == True):
                inAndOut[i] = inAndOut[i] +1
                inAndOut[j] = inAndOut[j] -1

    result = True
    for i in range(len(inAndOut)):
        if inAndOut[i] !=0:
            result = False
        print i
    return result


