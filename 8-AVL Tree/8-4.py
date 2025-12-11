class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVL_Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.root = self._insert(self.root, val, None)

    def _insert(self, node, val, parent):
        if not node:
            new_node = TreeNode(val)
            new_node.parent = parent
            return new_node

        if val < node.val:
            node.left = self._insert(node.left, val, node)
        else:
            node.right = self._insert(node.right, val, node)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and val < node.left.val: #new node less than y then rotate right first
            return self._rotate_right(node)
        if balance < -1 and val > node.right.val: #new node more than y then rotate right first
            return self._rotate_left(node)
        #after rotate the node is stil unbalanced(case 2, 4)
        if balance > 1 and val > node.left.val:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and val < node.right.val:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, x):
        y = x.right
        T1 = y.left

        y.left = x
        x.right = T1

        if T1:
            T1.parent = x
        y.parent = x.parent
        x.parent = y

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        if y.parent:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y

        return y

    def _rotate_right(self, x):
        y = x.left
        T2 = y.right

        y.right = x
        x.left = T2

        if T2:
            T2.parent = x
        y.parent = x.parent
        x.parent = y

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        if y.parent:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def burnTree(self, burn_node_val):
        if not self.root:
            return

        burn_node = self._find_node(self.root, burn_node_val)
        if not burn_node:
            print("There is no " + str(burn_node_val) + " in the tree.")
            return

        queue = [(burn_node, 0)]
        burned_nodes = {}
        visited = set()

        while queue:
            node, minute = queue.pop(0)

            if node in visited:
                continue

            if minute not in burned_nodes:
                burned_nodes[minute] = []
            burned_nodes[minute].append(node.val)
            visited.add(node)

            if node.left and node.left not in visited:
                queue.append((node.left, minute + 1))

            if node.right and node.right not in visited:
                queue.append((node.right, minute + 1))

            if node.parent and node.parent not in visited:
                queue.append((node.parent, minute + 1))

        for minute in sorted(burned_nodes.keys()):
            print(' '.join(map(str, burned_nodes[minute])))

    def _find_node(self, node, val):
        if not node or node.val == val:
            return node
        elif val < node.val:
            return self._find_node(node.left, val)
        else:
            return self._find_node(node.right, val)

    def print_tree_level(self, nodes, level, max_level):
        if not any(nodes):
            return
        current_indent = int(2 ** (max_level - level + 1) - 1)
        between_spaces = int(2 ** (max_level - level + 2) - 1)

        line = " " * (current_indent - 1)
        new_nodes = []
        for node in nodes:
            if node is None:
                line += " " * (between_spaces + 1)
                new_nodes.extend([None, None])
            else:
                line += f"{node.val}"
                new_nodes.extend([node.left, node.right])
                line += " " * between_spaces
        print(line.rstrip())
        self.print_tree_level(new_nodes, level + 1, max_level)

    def print_tree(self):
        height = self._get_height(self.root)
        self.print_tree_level([self.root], 1, height)



user_input = input("Enter node and burn node : ")
if '/' in user_input:
    nodes_input, burn_node_str = user_input.split('/')
    burn_node_val = int(burn_node_str)
else:
    nodes_input = user_input
    burn_node_val = None

nodes = list(map(int, nodes_input.split()))

bt = AVL_Tree()
for node in nodes:
    bt.insert(node)
2
bt.print_tree()
if burn_node_val is not None:
    bt.burnTree(burn_node_val)