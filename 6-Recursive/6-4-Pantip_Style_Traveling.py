def pantip(i, n, l, path):
    possible = 0
    if l == []:
        return
    if n+l[0] > i:
        pan = pantip(i,n,l[1:],path)
        if pan is not None:
            possible += pan
    elif n+l[0] < i:
        path.append(l[0])
        pan = pantip(i,n+l[0],l[1:],path)
        if pan is not None:
            possible += pan
        path.pop()
        pan = pantip(i,n,l[1:],path)
        if pan is not None:
            possible += pan
    elif n+l[0] == i:
        path.append(l[0])
        possible += 1
        print(str(path).replace('[','').replace(']','').replace(',',''))
        path.pop()
        pan = pantip(i,n,l[1:],path)
        if pan is not None:
            possible += pan
        return possible
    return possible

inp = input('Enter Input (Money, Product) : ').split('/')
l = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, l, [])
print(f"Krisada can purchase Product: {l} with: {inp[0]} Baht | {pattern} Pattern")