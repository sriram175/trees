class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def diameter(self,val,l):
        if val==None:
            return 0
        lh=self.diameter(val.left,l)
        rh=self.diameter(val.right,l)
        l[0]=max(l[0],(lh+rh))
        return 1+max(lh,rh)
    def diameter1(self,val,ans):
        l=[0]
        t.diameter(val,l)
        return l[0]
        
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.right.right=Node(5)
t.root.left.left.left=Node(6)
t.root.right.right.right=Node(7)
print(t.diameter1(t.root,0))
