class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
            
    def __str__(self):
        return str(self.data)
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        if self.head == None:
            return "empty"
        if self.head != None:
            current_node = self.head.next
            s = str(self.head)
            while current_node != None:
                s += "->" + str(current_node)
                current_node = current_node.next
            return s
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1
        
    def pop(self):
        if self.head == None: return
        if self.head.next == None:
            data = self.head.data
            self.head = None
        else:
            current_node = self.head
            while current_node and current_node.next.next:
                current_node = current_node.next
            data = current_node.next.data
            current_node.next = current_node.next.next
        return data
        
ll1 = LinkedList()
ll2 = LinkedList()

l1, l2 = [x.split("->") for x in input("Enter Input (L1,L2) : ").split(" ")]

for i in l1:
    ll1.append(i)

for i in l2:
    ll2.append(i)
    
for i in l2:
    ll1.append(ll2.pop())
print(ll1)