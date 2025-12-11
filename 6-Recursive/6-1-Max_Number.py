def find_max(list, max = None):
    if not list:
        return max
    n = list.pop()
    if max == None or n > max:
        max = n
    return find_max(list, max)

l = input("Enter Input : ").split()
print(f"Max : {find_max(l)}")