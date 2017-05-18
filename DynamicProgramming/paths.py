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
	
grid = [ int(x) for x in input().split()]
maxRow = grid[0]
maxCol = grid[1]

print(path(0,0))
