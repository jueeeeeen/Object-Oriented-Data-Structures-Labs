class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert(self, data):
        if self is None:
            return Node(data)
        if int(data) < int(self.data):
            self.left = Node.insert(self.left, data)
        else:
            self.right = Node.insert(self.right, data)
        return self
    
    def display(self):
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        """Returns list of strings, width, height"""
        
        # No child.
        if self.right is None and self.left is None:
            line = str(self.data)
            width = len(line)
            height = 1
            return [line], width, height

        # Only left child.
        if self.right is None:
            lines, width, height  = Node.display_aux(self.left)
            if self.left.right == None:
                width_right_of_left = 0
            else:
                width_right_of_left = Node.display_aux(self.left.right)[1] + 1
            data = str(self.data)
            length = len(data)
            first_line = f"{' ' * (width +1)}{data}"
            second_line = f"{' ' * (width-width_right_of_left)}{'_' * (width_right_of_left)}/{' ' * (length)}"
            shifted_lines = [f"{line}{' ' * (length + 1)}"for line in lines]
            return [first_line, second_line] + shifted_lines, width + length + 1, height + 2

        # Only right child.
        if self.left is None:
            lines, width, height  = Node.display_aux(self.right)
            if self.right.left == None:
                width_left_of_right = 0
            else:
                width_left_of_right = Node.display_aux(self.right.left)[1] + 1
            data = str(self.data)
            length = len(data)
            first_line = f"{data}{' ' * (width + 1)}"
            second_line = f"{' ' * (length)}\{'_' * (width_left_of_right)}{' ' * (width - width_left_of_right)}"
            shifted_lines = [f"{' ' * (length + 1)}{line}" for line in lines]
            return [first_line, second_line] + shifted_lines, width + length + 1, height + 2

        # Two children.
        left, width_left, height_left = Node.display_aux(self.left)
        right, width_right, height_right = Node.display_aux(self.right)
        if self.right.left == None:
            width_left_of_right = 0
        else:
            width_left_of_right = Node.display_aux(self.right.left)[1] + 1
            
        if self.left.right == None:
            width_right_of_left = 0
        else:
            width_right_of_left = Node.display_aux(self.left.right)[1] + 1
        data = str(self.data)
        length = len(data)
        first_line = f"{' ' * (width_left + 1)}{data}{' ' * (width_right + 1)}"
        second_line = f"{' ' * (width_left - width_right_of_left)}{'_' * (width_right_of_left)}/{' ' * (length)}\{'_' * (width_left_of_right)}{' ' * (width_right - width_left_of_right)}"
        if height_left < height_right:
            left += [width_left * ' '] * (height_right - height_left)
        elif height_right < height_left:
            right += [width_right * ' '] * (height_left - height_right)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [f"{a}{(length + 2) * ' '}{b}" for a, b in zipped_lines]
        return lines, width_left + width_right + length + 2, max(height_left, height_right) + 2


inp = input('Enter input: ').split()
root = None
for i in inp:
    root = Node.insert(root, i)
Node.display(root)
