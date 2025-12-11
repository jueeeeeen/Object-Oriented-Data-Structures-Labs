class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left if left is not None else None
        self.right = right if right is not None else None
        self.height = 0
        
    def get_height(self, node):
        return -1 if node is None else node.height
        
    def set_height(self):
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
    
    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = BST._insert(self.root, data)
        
    def _insert(node, data):
        if node is None: return Node(data)
        if int(data) < int(node.data):
            node.left = BST._insert(node.left, data)
        else:
            node.right = BST._insert(node.right, data)
        return node
    
    def get_successor(node):
        cur = node.right
        while cur and cur.left:
            cur = cur.left
        return cur    
    
    def delete(self, data):
        self.root = BST._delete(self.root, data)
    
    def _delete(node, data):
        if node is None: return None
        if int(data) < int(node.data): node.left = BST._delete(node.left, data)
        elif int(data) > int(node.data): node.right = BST._delete(node.right, data)
        else:
            if node.left is None: return node.right
            elif node.right is None: return node.left
            new_root = BST.get_successor(node)
            node.data = new_root.data
            node.right = BST._delete(node.right, new_root.data)
        return node
    
    def print_tree(self):
        BST._print_tree(self.root)
        print()
        
    def _print_tree(node, level = 0):
        if node is not None:
            BST._print_tree(node.right, level+1)
            print('    '*level + node.data )
            BST._print_tree(node.left, level+1)

class AVL:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            self.size += 1
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)            
        node.set_height()        
        new_root = AVL.rebalance(node)
        
        return new_root if new_root else node
        
    def rebalance(node):
        balance = node.get_balance()
        if balance < -1:
            if node.right.get_balance() == 1:
                node.right = AVL.rotate_right(node.right)
            return AVL.rotate_left(node)
        elif balance > 1:
            if node.left.get_balance() == -1:
                node.left = AVL.rotate_left(node.left)
            return AVL.rotate_right(node)
        
    def rotate_left(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.set_height()
        new_root.set_height()
        return new_root
    
    def rotate_right(root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.set_height()
        new_root.set_height()
        return new_root
    
    def get_successor(root):
        if root and root.left:
            return AVL.get_successor(root.left)
        else:
            return root
        
    def get_successor_left(root):
        if root and root.right:
            return AVL.get_successor(root.right)
        else:
            return root
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
        
    def _delete(self, root, data):
        if root is None: 
            return None
        if data < root.data: root.left = self._delete(root.left, data)
        elif data > root.data: root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                self.size -= 1
                return root.right
            elif root.right is None:
                self.size -= 1
                return root.left
            new_root = AVL.get_successor(root.right)
            root.data = new_root.data
            root.right = self._delete(root.right, new_root.data)
        root.set_height()
        rebalanced_root = AVL.rebalance(root)
        return rebalanced_root if rebalanced_root else root
    
    def delete_left(self, data):
        self.root = self._delete_left(self.root, data)
    
    def _delete_left(self, root, data):
        if root is None: 
            return None
        if data < root.data: root.left = self._delete_left(root.left, data)
        elif data > root.data: root.right = self._delete_left(root.right, data)
        else:
            if root.left is None:
                self.size -= 1
                return root.right
            elif root.right is None:
                self.size -= 1
                return root.left
            new_root = AVL.get_successor_left(root.left)
            root.data = new_root.data
            root.left = self._delete_left(root.left, new_root.data)
        root.set_height()
        rebalanced_root = AVL.rebalance(root)
        return rebalanced_root if rebalanced_root else root
    
    def search(self, key):
        return AVL._search(self.root, key)
    
    def _search(root, key):
        if root is None: return f"Room {key} not found (empty)"
        if key == root.data: return root.show_room()
        if key < root.data: return AVL._search(root.left, key)
        return AVL._search(root.right, key)
        
    def print_tree(self):
        AVL._print_tree(self.root)
        
    def _print_tree(node, level = 0):
        if node is not None:
            AVL._print_tree(node.right, level+1)
            print('    '*level + str(node.data) )
            AVL._print_tree(node.left, level+1)

    def inorder_sort(node, f):
        if node is not None:
            AVL.inorder_sort(node.left, f)
            f.write(node.show_room() + "\n\n")
            AVL.inorder_sort(node.right, f)
            
    def level_order(self):
        q = []
        q.append(self.rppt)
        while not q.isEmpty():
            n = q.pop(0)
            print(n, end=" ")
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            
    def parent(self, key):
        return AVL._parent(self.root, key)
    
    def _parent(root, key):
        if root is None or root.data == key:
            return None
        if (root.left and root.left.data == key) or (root.right and root.right.data == key):
            return root
        if key < root.data: return AVL._parent(root.left, key)
        if key >= root.data: return AVL._parent(root.right, key)
        
    
        
Tree = AVL()
inp = (input()).split()
for i in inp:
    Tree.insert(int(i))
Tree.print_tree()

while 1:
    d = int(input())
    Tree.delete_left(d)
    Tree.print_tree()

print(Tree.parent(9).data)

print(Tree.parent(4).data)