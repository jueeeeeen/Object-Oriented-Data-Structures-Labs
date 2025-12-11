# Unordered List
def search(l, key):
    for element in l:
        if key == element:
            return "Found"
    return "Not Found"

def search_index(l, key):
    for i in range(len(l)):
        if l[i] == key:
            return i
    return "Not Found"

#sentinal
def sentinal_search(l, key):
    l.append(key)
    i = 0
    while l[i] != key:
        i += 1
    
    if i < len(l)-1:
        return i
    else:
        return "Not Found"
    
# search = sentinal_search([19,56,2,7,25,18], 1)
# print(search)    
# move to front - move to front
# Transposition - move 1 index forward

#Binary search

def binary_search(l, key):
    low, high = 1, l(len)
    while low <= high:
        mid = (low+high)//2
        if l[mid] < key:
            low = mid + 1
        elif l[mid] > key:
            high = mid - 1
        else:
            low = high + 1
    if key == l[mid]:
        return mid
    else: return -1
    
def binary_search(l, key, low, high):
    mid = (low + high)//2
    if l[mid] == key: return mid
    if low < high:
        if l[mid] < key:
            return binary_search(l, key, mid+1, high)
        else:
            return binary_search(l, key, low, mid-1)
    
print(binary_search([1,3,5,6,6,7,9,13,17,19,20,21,25,30,41,45,47,49,55], 1, 0, 19))
    
    
    
def binary_search_tree(root, key):
    p = q = root
    while p is not None:
        if key < p.data:
            p = p.left
        elif key > p.data:
            p = p.right
        else:
            q = p
            p = None
    if key == q.data:
        return q
    else: return None