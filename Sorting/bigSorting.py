import sys

def sortArray(unsorted):
    return unsorted.sort()

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

unsorted.sort()
for i in unsorted:
    print(i)
    
