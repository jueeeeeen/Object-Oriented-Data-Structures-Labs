class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def __str__(self):
        return str(self.val)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height

    def getHeight(self, node):
        return -1 if node == None else node.height

    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVL_Tree(object): 
    def __init__(self, root=None):
        self.root = None if root is None else root
        
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            AVL_Tree._insert(self.root, val)
            self.rebalance()
        

    def _insert(root, val):
        if root is None:
            return TreeNode(val)
        
        if int(val) < int(root.val):
            root.left = AVL_Tree._insert(root.left, val)
        else:
            root.right = AVL_Tree._insert(root.right, val)
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
        print("Not Balance, Rebalance!")
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
            if int(root.val) < int(parent.val):
                parent.left = root
            else:
                parent.right = root
        return root
        
    def getUnbalancedNode(self):
        return AVL_Tree._getUnbalancedNode(self.root)
    
    def _getUnbalancedNode(root):
        if root is None:
            return None, None
        
        if root.left:
            parent, unbalanced_node = AVL_Tree._getUnbalancedNode(root.left)
            if unbalanced_node:
                return parent if parent else root, unbalanced_node
            
        if root.right:
            parent, unbalanced_node = AVL_Tree._getUnbalancedNode(root.right)
            if unbalanced_node:
                return parent if parent else root, unbalanced_node
            
        if root.balanceValue() > 1 or root.balanceValue() < -1:
            # print("hi")
            return None, root
        
        return None, None
    
    def printTree(self):
        AVL_Tree._printTree(self.root)

    def _printTree(node , level=0):

        if not node is None:

            AVL_Tree._printTree(node.right, level + 1)

            print('     ' * level, node.val)

            AVL_Tree._printTree(node.left, level + 1)
    
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    myTree.insert(e)
    myTree.printTree()
    print("===============")