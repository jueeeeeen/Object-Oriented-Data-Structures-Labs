def bubble_sort(l):
    for last in range(len(l)-1, 0, -1):
        swapped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
                print(str(last) +":"+ str(l))
        if not swapped:
            break
    return l
# bubble_sort([5,3,4,1,2])

def straight_selection_sort(l):
    for last in range(len(l), 0, -1):
        max_index = 0
        for i in range(1, last):
            if l[i] > l[max_index]:
                max_index = i
        l[last-1], l[max_index] = l[max_index], l[last-1]
    return l

def insertion_sort(l):
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if l[j-1] > iEle and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break

def shell_sort(l, dIncrements):
    for inc in dIncrements:
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if l[j-inc] > iEle and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
                
# Heap sort

from math import log2
from math import floor

def print90(h, i, max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('    ' * indent, h[i])
        print90(h, (i*2)+1, max_i)
        
def insertMinHeap(h, i):
    print('insert', h[i], 'at index', i, end = '    ')
    print(h)
    insertEle = h[i]
    fi = (i-1)//2
    while i > 0 and insertEle < h[fi]:
        h[i] = h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle
    
def insertMinHeap1(h):
    for i in range(1, len(h)):
        insertEle = h[i]
        fi = (i-1)//2
        while i > 0 and insertEle < h[fi]:
            h[i] = h[fi]
            i = fi
            fi = (i-1)//2
        h[i] = insertEle
    
# Ex
# h = [200, 100, 97, 85, 30]
# insertMinHeap1(h)
# print(h)
# for i in range(1, len(h)):
#     insertMinHeap(h, i)
#     print(h)
#     print90(h, 0, i)
#     print("---------------------------\n")
    
def delMin(h, last):
    print('delMin', h[0], 'last index = ', last, end='  ')
    print(h)
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2+1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h[ls] < h[rs] else rs
        if h[min] < insertEle:
            h[hole] = h[min]
            hole = min
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle
    
# Ex
# h = [13, 14, 16, 24,21, 19, 68, 65, 26, 32, 31]
# for last in range(len(h)-1, -1, -1):
#     delMin(h, last)
#     print(h)
#     print90(h, 0, last)
#     print("---------------------------\n")

# Merge Sort

def merge_sort(l, left, right):
    center = (left+right)//2
    if left < right:
        merge_sort(l, left, center)
        merge_sort(l, center+1, right)
        merge(l, left, center+1, right)
        
def merge(l, left, right, right_end):
    start = left
    left_end = right-1
    result = []
    
    while left <= left_end and right <= right_end:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= left_end:
        result.append(l[left])
        left += 1
    while right <= right_end:
        result.append(l[right])
        right += 1
    
    print(result)
    
    for ele in result:
        l[start] = ele
        start += 1
        if start > right_end:
            break

list = [5, 3, 6, 1, 2, 7, 8, 4]
print(merge_sort(list, 0, len(list)-1))

# Quick Sort

def quick_sort(l):
    q_sort(l, 0, len(l)-1)
    
def q_sort(l, left, right):
    if left < right+1:
        p = partition(l, left, right)
        q_sort(l, left, p-1)
        q_sort(l, p+1, right)
        
def partition(l, left, right):
    if left == right-1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return left
    
    pivot = l[left]
    i, j = left+1, right
    while i < j:
        while i < right and l[i] <= pivot:
            i += 1
        while j > left and l[j] >= pivot:
            j -= 1
        if i<j:
            l[i], l[j] = l[j], l[i]
    if left is not j:
        l[left], l[j] = l[j], pivot
    return j

# Ex
# l = [5, 1, 4, 9, 6, 3, 8, 2, 7, 0]
# quick_sort(l)

def partition_median_of_3(l, left, right):
    if left == right-1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return
    
    c = (left + right)//2
    if l[left] < l[c]:
        l[left], l[c] = l[c], l[left]
    if l[right] < l[c]:
        l[c], l[right] = l[right], l[c]
    if l[right] < l[left]:
        l[left], l[right] = l[right], l[left]
    
    pivot = l[left]
    i, j = left + 1, right
    while i < j:
        while i < right and l[i] <= pivot:
            i += 1
        while j > left and l[j] >= pivot:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    if left is not j:
        l[left], l[j] = l[j], pivot