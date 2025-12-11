class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left if left is not None else None
        self.right = right if right is not None else None
        self.height = 0
        
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self, root = None):
        self.root = root
        
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
            
    def search(self, key):
        return BST._search(self.root, key)
    
    def _search(root, key):
        if root is None: return f"Room {key} not found (empty)"
        if key == root.data: return root.show_room()
        if key < root.data: return BST._search(root.left, key)
        return BST._search(root.right, key)
        
    def print_tree(self):
        BST._print_tree(self.root)
        
    def _print_tree(node, level = 0):
        if node is not None:
            BST._print_tree(node.right, level+1)
            print('    '*level + str(node.data) )
            BST._print_tree(node.left, level+1)

    def inorder_sort(node, f):
        if node is not None:
            BST.inorder_sort(node.left, f)
            f.write(node.show_room() + "\n\n")
            BST.inorder_sort(node.right, f)
            
    def level_order(self):
        q = []
        q.append(self.rppt)
        while not q.isEmpty():
            n = q.pop(0)
            print(n, end=" ")
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            
    def parent(self, key):
        return BST._parent(self.root, key)
    
    def _parent(root, key):
        if root is None or root.data == key:
            return None
        if root.left.data == key or root.right.data == key:
            return root
        if key < root.data: return BST._parent(root.left, key)
        if key >= root.data: return BST._parent(root.right, key)

def postfix_to_BST(postfix):
    stack = []
    for s in postfix:
        op = Node(s)
        if s in '+-*/':
            op.right = stack.pop()
            op.left = stack.pop()
        stack.append(op)
    return BST(stack.pop())

tree = postfix_to_BST("ab+cde+**")
tree.print_tree()

# Tree = AVL()

# for i in [1, 2, 4, 9, 10, 6, 7]:
#     Tree.insert(i)

# Tree.print_tree()

# print(Tree.parent(9).data)

# print(Tree.parent(4).data)