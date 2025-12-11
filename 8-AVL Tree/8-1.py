class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        def __str__(self):

            return str(self.data)

        def setHeight(self):

                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a, b)

                return self.height

        def getHeight(self, node):

            return -1 if node == None else node.height

        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root=None):

        self.root = None if root is None else root

    def add(self, data):
        if self.root is None:
            self.root = AVLTree.AVLNode(data)
        else:
            AVLTree._add(self.root, data)
        self.rebalance()

    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        
        if int(data) < int(root.data):
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root.setHeight()
        return root
        
        
    def rotateLeftChild(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setHeight()
        new_root.setHeight()
        if root == self.root:
            self.root = new_root
        return new_root
    
    def rotateRightChild(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setHeight()
        new_root.setHeight()
        if root == self.root:
            self.root = new_root
        return new_root
    
    def rebalance(self):
        parent, root = self.getUnbalancedNode()
        if root is None:
            return None
        balance = root.balanceValue()
        if balance == -2:
            if root.right.balanceValue() == 1:
                root.right = self.rotateLeftChild(root.right)
            root = self.rotateRightChild(root)
        elif balance == 2:
            if root.left.balanceValue() == -1:
                root.left = self.rotateRightChild(root.left)
            root = self.rotateLeftChild(root)
            
        if parent is not None:
            if int(root.data) < int(parent.data):
                parent.left = root
            else:
                parent.right = root
        return root
    
    def getUnbalancedNode(self):
        return AVLTree._getUnbalancedNode(self.root)
    
    def _getUnbalancedNode(root):
        if root is None:
            return None, None
        
        if root.left:
            parent, unbalanced_node = AVLTree._getUnbalancedNode(root.left)
            if unbalanced_node:
                return parent if parent else root, unbalanced_node
            
        if root.right:
            parent, unbalanced_node = AVLTree._getUnbalancedNode(root.right)
            if unbalanced_node:
                return parent if parent else root, unbalanced_node
            
        if root.balanceValue() > 1 or root.balanceValue() < -1:
            return None, root
        
        return None, None
    
    def postOrder(self):
        print("AVLTree post-order : ", end="")
        AVLTree._postOrder(self.root)
        print()
        
    def _postOrder(root):
        if root is not None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end = " ")
            
    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":

        avl1.add(i[3:])

    elif i[:2] == "PR":

        avl1.printTree()

    elif i[:2] == "PO":
        avl1.postOrder()