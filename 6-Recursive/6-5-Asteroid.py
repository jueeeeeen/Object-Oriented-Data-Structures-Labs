def asteroid_collision(asts, i = 1):
    if i == len(asts):
        return asts
    else:
        prev = asts[i-1]
        curr = asts[i]
        if prev > 0 and curr < 0:
            curr *= -1
            if prev >= curr:
                asts.pop(i)
            if prev <= curr:
                asts.pop(i-1)
            return asteroid_collision(asts, i-1)
        else:
            return asteroid_collision(asts, i+1)
                

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))