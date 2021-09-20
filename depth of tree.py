class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def depth(self,val):
        if val==None:
            return 0
        lh=self.depth(val.left)
        rh=self.depth(val.right)
        return 1+max(lh,rh)
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
print(t.depth(t.root))
