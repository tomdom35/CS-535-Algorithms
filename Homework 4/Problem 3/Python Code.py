#Node object that makes up tree
class node:
    def __init__(self,parent,leftChild,rightChild,name):
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.x = None
        self.y = None
        self.name = name

#Create nodes
v1 = node(None,None,None,"v1")
v2 = node(None,None,None,"v2")
v3 = node(None,None,None,"v3")
v4 = node(None,None,None,"v4")
v5 = node(None,None,None,"v5")
v6 = node(None,None,None,"v1")
v7 = node(None,None,None,"v2")
v8 = node(None,None,None,"v3")
v9 = node(None,None,None,"v4")
v10 = node(None,None,None,"v5")
v11 = node(None,None,None,"v1")
v12 = node(None,None,None,"v2")
v13 = node(None,None,None,"v3")
v14 = node(None,None,None,"v4")
v15 = node(None,None,None,"v5")

#Create tree
v1.leftChild = v2
v1.rightChild = v3
v2.parent = v1
v2.leftChild = v4
v2.rightChild = v5
v3.parent = v1
v3.leftChild = v6
v3.rightChild = v7
v4.parent = v2
v5.parent = v2
v5.leftChild = v8
v5.rightChild = v9
v6.parent = v3
v7.parent = v3
v7.leftChild = v10
v7.rightChild = v11
v8.parent = v5
v9.parent = v5
v9.leftChild = v12
v9.rightChild = v13
v10.parent = v7
v11.parent = v7
v12.parent = v9
v12.leftChild = v14
v12.rightChild = v15
v13.parent = v9
v14.parent = v12
v15.parent = v12


#Set number of nodes and height   
n = 15
h = 6

#Create empty grid
grid = []
for i in range(0,h):
    xVal = []
    for j in range(0,n):
        xVal.append(".")
    grid.append(xVal)

#Algorithm
def findRightMost(v):
    if v.rightChild is None:
        return v
    else:
        return findRightMost(v.rightChild)

def inOrderPlot(v,x,y):
    if v.leftChild is not None:
        inOrderPlot(v.leftChild,x,y+1)
        v.x = findRightMost(v.leftChild).x+1
        v.y = y
        grid[v.y][v.x] = "O"
    else:
        v.x = x
        v.y = y
        grid[v.y][v.x] = "O"
    if v.rightChild is not None:
        inOrderPlot(v.rightChild, v.x+1, y+1)

inOrderPlot(v1,0,0)

#Print Grid
for i in grid:
    print("".join(i))
print()
