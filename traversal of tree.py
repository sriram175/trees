class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class tree:
    def __init__(self,root):
        self.root=Node(root)
    def print_tree(self,string):
        if string=="preorder":
            return self.preorder(t.root,"")
        elif string=="postorder":
            return self.postorder(t.root,"")
        elif string=="Inorder":
            return self.inorder(t.root,"")
    def preorder(self,start,traversal):
        if start:
            traversal+=str(start.val)+'-'
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    def postorder(self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=str(start.val)+"-"
        return traversal
    def inorder(self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=str(start.val)+'-'
            traversal=self.inorder(start.right,traversal)
        return traversal
t=tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
print(t.print_tree("preorder"))
print(t.print_tree("postorder"))
print(t.print_tree("Inorder"))
