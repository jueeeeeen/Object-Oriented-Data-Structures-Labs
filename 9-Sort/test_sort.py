def recursive_bubble_sort(l, last = None, i = 0):
    if last is None:
        last = len(l)-1
    if last == 0:
        return l
    if i < last:
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
        return recursive_bubble_sort(l, last, i+1)
    else:
        return recursive_bubble_sort(l, last-1, 0)

def positive_sort(l):
    for last in range(len(l)-1, 0, -1):
        swapped = False
        for i in range(last):
            if l[i] < 0:
                continue
            j = 1
            while i+j <= last and l[i+j] < 0:
                j += 1
            if i+j <= last and l[i] > l[i+j]:
                l[i], l[i+j] = l[i+j], l[i]
                swapped = True
            i += j - 1
        if swapped == False:
            break
    return l

def sort_by_mode(l):
    dupe = {}
    for num in l:
        if num not in dupe.keys():
            dupe[num] = 1
        else:
            dupe[num] += 1
    modes = list(dupe.items())
    for last in range(len(modes)-1, 0, -1):
        for j in range(last):
            if modes[j][1] < modes[j+1][1]:
                modes[j], modes[j+1] = modes[j+1], modes[j]
    for mode in modes:
        print(f"number {mode[0]}, total: {mode[1]}")

def recursive_insertion_sort(l, i = 1, j = None, insert_element = None):
    if i == len(l):
        return l
    if j == None:
        j = i
    if insert_element is None:
        insert_element = l[i]
    if l[j-1] > insert_element and j > 0:
        l[j] = l[j-1]
        return recursive_insertion_sort(l, i, j-1, insert_element)
    else:
        l[j] = insert_element
        return recursive_insertion_sort(l, i+1, i+1)

inp = input().split()
recursive_insertion_sort(inp)