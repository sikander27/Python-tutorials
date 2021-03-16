
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data,end=" ")
        if self.right:
            self.right.printTree()
            

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)
    
    
    def traverse(self, root):
        res = []
        if root:
            # In order left->root->right
            if root.left:
                res = self.traverse(root.left)
            res.append(root.data)
            if root.right:    
                res = res + self.traverse(root.right)
            return res

            
        
root = Node(10)
root.left = Node(8)
root.right = Node(27)
root.insert(12)
root.insert(7)
root.insert(14)
# root.printTree()
print(root.tra())
print(root.traverse(root)) 
