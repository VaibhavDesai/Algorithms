class graphs:
    left = None
    right = None
    value = 0
    nodeValue = 0

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addNodes(child, parent):

    if parent == None:
        return child

    if child.value < parent.value:
        parent.left = child
    else:
        parent.right = child

    return parent

queue = []
def BFSTraversal(node, previousNodeValue):

    if node.left != None:
        node.left.nodeValue = node.nodeValue -1
        queue.append(node.left)

    if node.right != None:
        node.right.nodeValue = node.nodeValue +1
        queue.append(node.right)


hashMap = {}

def takeInput():
    n = raw_input("Enter number of elements")
    m = raw_input("Enter elements")
    ele = [int(x) for x in m.split()]
    parent = None
    for e in ele:
        node  = graphs(e)
        parent = addNodes(node, parent)
        if node.value in hashMap:
            hashMap[node.nodeValue] = hashMap[node.nodeValue]+ node.value


