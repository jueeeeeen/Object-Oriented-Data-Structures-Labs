# Chapter : 9 - item : 5 - Sort Subset
#  ส่งมาแล้ว 1 ครั้ง
# ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

# 1. ด้านซ้าย เป็นผลลัพธ์
# 2. ด้านขวา เป็น list ของจำนวนเต็ม

# โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

# 1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
# 2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

# ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset



# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

# อธิบาย Test Case 1:

# [2]
# [-1, 3]
# [0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
# [-3, 2, 3]
# [-2, 1, 3]
# [-1, 0, 3]
# [-1, 1, 2]
# [-3, 0, 2, 3]
# [-2, -1, 2, 3]
# [-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
# [-1, 0, 1, 2]
# [-3, -1, 1, 2, 3]
# [-2, -1, 0, 2, 3]
# [-3, -1, 0, 1, 2, 3]

def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        swapped = False
        for i in range(i):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
    return numbers

def subset_sort(subset):
    for i in range(len(subset) - 1, 0, -1):
        swapped = False
        for i in range(i):
            if len(subset[i]) > len(subset[i+1]):
                subset[i], subset[i+1] = subset[i+1], subset[i]
                swapped = True
        if swapped is False:
            break
    return subset

def find_subset(target, numbers, index = 0, result = None, current_subset = None):  
    if result is None:  
        result = []
    if current_subset is None:
        current_subset = []
    if index >= len(numbers):    
        return result
    current_subset.append(numbers[index])
    if sum(current_subset) == target:  
        result.append(current_subset.copy())

    result = find_subset(target, numbers, index + 1, result, current_subset) 
    current_subset.pop()
    result = find_subset(target, numbers, index + 1, result, current_subset)
    return result

inp_target, inp_number = input("Enter Input : ").split("/")
target = int(inp_target)
number_list = [int(i) for i in inp_number.split(" ")]

result = find_subset(target, bubble_sort(number_list))

if result:
    for subset in subset_sort(result):
        print(subset)
else:
    print("No Subset")