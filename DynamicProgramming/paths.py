def validCell(row,col):
	if row < maxRow and col < maxCol:
		return True
	else:
		return False
		
def isDestination(row,col):
	if row == (maxRow-1) and col == (maxCol-1):
		return True
	else:
		return False

def path(row, col):
	
	if(isDestination(row,col)):
		return 1
		
	elif(validCell(row,col)):
		rowSum  = path(row+1,col)
		colSum  = path(row,col+1)
	else:
		return 0
	
	return rowSum+colSum

def DPPath():

	for x in range(maxRow):
		matrix[x][0] = 1
	for y in range(maxCol):
		maxtrix[0][y] = 1

	for x in range(1,maxRow):
		for y in range(1,maxCol):
			matrix[x][y] = matrix[x-1][y]+matrix[x][y-1]

	return matrix[maxRow-1][maxCol-1]

elements = [ int(x) for x in input().split()]
maxRow = elements[0]
maxCol = elements[1]
maxtrix = [[ 0 for x in range(maxCol)] for y in range(maxRow)]

print(DPPath())
print(path(0,0))
