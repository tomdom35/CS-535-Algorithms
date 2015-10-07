class node:
    def __init__(self,parent,leftChild,rightChild,name):
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.x = None
        self.y = None
        self.name = name

v1 = node(None,None,None,"v1")
v2 = node(None,None,None,"v2")
v3 = node(None,None,None,"v3")
v4 = node(None,None,None,"v4")
v5 = node(None,None,None,"v5")

v1.leftChild = v2
v1.rightChild = v3
v2.parent = v1
v2.leftChild = v4
v2.rightChild = v5
v3.parent = v1
v4.parent = v2
v5.parent = v2

#v1 = node(None,v2 = node(v1,v4 = node(v2,None,None),v5 = node(v2,None,None)),v3 = node(v1,None,None))
         


n = 5
h = 3

grid = []
for i in range(0,h):
    xVal = []
    for j in range(0,n):
        xVal.append(".")
    grid.append(xVal)
        
for i in grid:
    print("".join(i))
print()

def inOrder(v,x,y):
    if v.leftChild is not None:
        inOrder(v.leftChild,x,y+1)
    if v.leftChild is None:
        v.x = x
        v.y = y
        grid[y][x] = "O"
        for i in grid:
            print("".join(i))
        #print(v.name,v.x,v.y)
        print()
    else:
        v.x = v.leftChild.x+1
        v.y = y
        grid[y][v.leftChild.x+1] = "O"
        for i in grid:
            print("".join(i))
        #print(v.name,v.x,v.y)
        print()
    if v.rightChild is not None:
        inOrder(v.rightChild, v.x+1, y+1)

inOrder(v1,0,0)

for i in grid:
    print("".join(i))
print()
