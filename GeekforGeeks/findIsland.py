#http://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1
'''Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

# your task is to complete this function
# Your function should return an integer
#Time complexity of this algoritm is n x m
#This problem is solved using the concept of DFS

def findIslands(arr, n, m):
    count = 0
    while(1):
        i,j = findStart(arr,n,m)
        if i == -1 or j == -1:
            break
        IsIsland(arr,i,j,n,m)
        count += 1
        
    return count
        
def IsIsland(mat,i,j,n,m):
    if i < 0 or i>n-1 or j<0 or j>m-1:
        return
    if mat[i][j] == 1:
        mat[i][j] = 0
        IsIsland(mat, i-1,j,n,m)
        IsIsland(mat, i+1,j,n,m)
        IsIsland(mat, i,j-1,n,m)
        IsIsland(mat, i,j+1,n,m)
        IsIsland(mat, i+1,j+1,n,m)
        IsIsland(mat, i-1,j-1,n,m)
        IsIsland(mat, i-1,j+1,n,m)
        IsIsland(mat, i+1,j-1,n,m)
    else:
        return
        
def findStart(mat,n,m):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                return i,j
    return -1,-1
