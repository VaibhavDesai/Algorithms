# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    n = 0
    currNode = l
    while currNode != None:
        n += 1
        currNode = currNode.next

    midElement = n//2
    currentNode = l
    previousNode = None
    i=0
    while i != n:
        if i > midElement:
           tempNode = currentNode.next
           currentNode.next = previousNode
           previousNode = currentNode
           currentNode = tempNode
        else:
           previousNode = currentNode
           currentNode = currentNode.next
        i = i+1
    lastNode = previousNode
    currentNode = l
    i = 0
    while i != n//2:
        if currentNode.value != lastNode.value:
            return False
        currentNode = currentNode.next
        lastNode = lastNode.next
        i += 1
    
    return True
