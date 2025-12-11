def print_alphabet(alphabet, curr = None, n = 0):
    if n == 2*(ord(alphabet) - ord("A") + 1)-1:
        return
    
    if curr == None:
        curr = "A"
    
    if n >= (ord(alphabet) - ord("A") + 1):
        print(curr[:-1])
        print_alphabet(alphabet, curr[:-1], n+1)
    else:
        print(curr)
        if n == (ord(alphabet) - ord("A") + 1) - 1:
            print_alphabet(alphabet, curr, n+1)
        else:
            print_alphabet(alphabet, curr + chr(ord(curr[-1]) + 1), n+1)
    
print_alphabet('D')