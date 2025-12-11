class Room_Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left if left is not None else None
        self.right = right if right is not None else None
        self.height = 0
        
    def __str__(self):
        return str(self.data)
    
    def get_height(self, node):
        return -1 if node is None else node.height
        
    def set_height(self):
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
            
    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

class AVL:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, room_number, channel):
        self.root = self._insert(self.root, room_number, channel)
    
    def _insert(self, node, room_number, channel):
        if node is None:
            print(f"Added room {room_number}")
            self.size += 1
            return Room_Node(room_number, channel)
        if room_number < node.room_number:
            node.left = self._insert(node.left, room_number, channel)
        elif room_number > node.room_number:
            node.right = self._insert(node.right, room_number, channel)
        else:
            print(f"Can't add {room_number}")
            
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
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
        
    def _delete(self, root, room_number):
        if root is None: 
            print(f"Not found room", end=" ")
            return None
        if room_number < root.room_number: root.left = self._delete(root.left, room_number)
        elif room_number > root.room_number: root.right = self._delete(root.right, room_number)
        else:
            if root.left is None:
                self.size -= 1
                print(f"Deleted room", end = " ")
                return root.right
            elif root.right is None:
                self.size -= 1
                print(f"Deleted room", end = " ")
                return root.left
            new_root = AVL.get_successor(root.right)
            root.room_number = new_root.room_number
            root.right = self._delete(root.right, new_root.room_number)
        root.set_height()
        rebalanced_root = AVL.rebalance(root)
        return rebalanced_root if rebalanced_root else root
    
    def search(self, key):
        return AVL._search(self.root, key)
    
    def _search(root, key):
        if root is None: return f"Room {key} not found (empty)"
        if key == root.room_number: return root.show_room()
        if key < root.room_number: return AVL._search(root.left, key)
        return AVL._search(root.right, key)
        
    def print_tree(self):
        AVL._print_tree(self.root)
        
    def _print_tree(node, level = 0):
        if node is not None:
            AVL._print_tree(node.right, level+1)
            print('    '*level + str(node) )
            AVL._print_tree(node.left, level+1)

    def inorder_sort(node, f):
        if node is not None:
            AVL.inorder_sort(node.left, f)
            f.write(node.show_room() + "\n")
            print(node.show_room())
            AVL.inorder_sort(node.right, f)
    
    def get_last_room(self):
        return AVL._get_last_room(self.root)
    
    def _get_last_room(node):
        if node.right is None:
            return node
        else:
            return AVL._get_last_room(node.right)