class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def balanced(self,val):
        if val==None:
            return 0
        lh=self.balanced(val.left)
        rh=self.balanced(val.right)
        if abs(lh-rh)>1:
            return -1
        if lh==-1 or rh==-1:
            return -1
        return 1+max(lh,rh)
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.left.left.left=Node(6)
t.root.left.left.right=Node(7)
if t.balanced(t.root)!=-1:
    print("Balanced")
else:
    print("Not Balanced")
