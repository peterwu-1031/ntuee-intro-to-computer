import sys
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key
    
    def Insert(self, key):
        if key < self.value:
            if(self.left == None):
                self.left = Node(key)
            else:
                self.left.Insert(key)
        elif key > self.value:
            if(self.right == None):
                self.right = Node(key)
            else:
                self.right.Insert(key)

def GetLevel(node, key, level):
    if (node == None):
        return 0
  
    if (node.value == key):
        return level
  
    downlevel = GetLevel(node.left, key, level + 1)
    if (downlevel != 0):
        return downlevel
  
    downlevel = GetLevel(node.right, key, level + 1)
    return downlevel

root = Node(6)
root.left = Node(2)
root.left.right = Node(4)
root.right = Node(16)
root.right.left = Node(11)
root.right.left.right = Node(13)
root.right.right = Node(19)

for i in range(1, 4):
    x = ord(sys.argv[i][0])-64
    if (GetLevel(root, x, 1)):
        print(GetLevel(root, x, 1))
    else:
        root.Insert(x)
        print(GetLevel(root, x, 1))

