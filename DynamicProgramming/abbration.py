def subStringMatch(stringA, stringB):

    rowN = len(stringB)
    colN = len(stringA)

    subString = [[ 0 for x in range(colN+1)] for y in range(rowN+1)]
    for i in range(rowN+1):
        subString[i][0] = 0
    for i in range(colN+1):
        subString[0][i] = 0

    for i in range(1,rowN+1):
    	for j in range(1,colN+1):
            if(stringB[i-1].lower() == stringA[j-1].lower()):
	           	subString[i][j] = subString[i-1][j-1] + 1
            else:
                subString[i][j] = max(subString[i-1][j],subString[i][j-1])

    if(len(stringB) == subString[rowN][colN]):
        return "YES"
    else:
        return "NO"

number = int(input())
output = []
for i in range(number):
    stringA = input()
    stringB = input()
    output.append(subStringMatch(stringA,stringB))

for ele in output:
    print(ele)
