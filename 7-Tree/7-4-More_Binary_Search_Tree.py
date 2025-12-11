class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
                
    def append(self, data, node):
        if node == None:
            if self.root == None:
                self.root = Node(data)
            return Node(data)
            
        if data < node.data:
            node.left = self.append(data, node.left)
        else:
            node.right = self.append(data, node.right)
        return node
    
    def cut(self, data, node = None):
        if node == None:
            node = self.root
            
        if node.data == data:
            if node.right != None:
                node.right = None
            elif node.left != None:
                node.left = None
            else:
                print("Not thing change")
            return
            
        else:
            if data < node.data:
                self.cut(data, node.left)
            else:
                self.cut(data, node.right)
        
    def preorder(self, node,stop):
        if node != None:
            self.printNode(node.data, stop)
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node,stop):
        if node != None:
            self.inorder(node.left, stop)
            self.printNode(node.data, stop)
            self.inorder(node.right, stop)
            

    def postorder(self, node,stop):
        if node != None:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            self.printNode(node.data, stop)
            
    def printNode(self, data, stop):
        if stop >= data:
                ascii = ""
                for c in data:
                    ascii += str(ord(c))
                print(ascii, end = " ")
        else:
            print(data, end = " ")
            
    def printMirrorTree(self, node, level=0):
        if node != None:
            self.printMirrorTree(node.left, level + 1)
            print('     ' * level, node)
            self.printMirrorTree(node.right, level + 1)
            

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        

T = BST()
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
first = first.split()
for i in first:
    T.append(i, T.root)
print("FIrst look of this plum tree")
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:], T.root)
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)