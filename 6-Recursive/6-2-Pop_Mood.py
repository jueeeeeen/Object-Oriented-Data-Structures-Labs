def print_bin(n, i = 0):
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
    elif i > (2**n)-1:
        return
    else:
        print(f"{bin(i)[2:]:0>{n}}")
        return print_bin(n, i+1)

n = int(input("Enter Number : "))
print_bin(n)