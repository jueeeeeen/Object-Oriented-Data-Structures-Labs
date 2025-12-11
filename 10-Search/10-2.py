def search_first_greater(l, val):
    first = None
    for num in l:
        if (num > val) and ((first is None or num < first)):
            first = num
    return "No First Greater Value" if first is None else first

nums, vals = input("Enter Input : ").split("/")
nums = list(map(int, nums.split(" ")))
vals = list(map(int, vals.split(" ")))

for val in vals:
    print(search_first_greater(nums, val))