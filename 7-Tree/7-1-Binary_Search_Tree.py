class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
            return self.root
        
        p = self.root
        while p != None:
            if int(data) < int(p.data):
                if p.left == None:
                    p.left = node
                    return self.root
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = node
                    return self.root
                else:
                    p = p.right

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)