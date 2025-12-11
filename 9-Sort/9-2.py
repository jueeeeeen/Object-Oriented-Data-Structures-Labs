# Chapter : 9 - item : 2 - Straight Selection Sort [recursive]
# เขียน function Straight Selection Sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# และแสดงขั้นตอนของ Straight Selection Sort ตามตัวอย่าง

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def straight_selection_sort(num_list, length = None, max_i = 0, i = 0):
    if length is None: length = len(num_list)
    if length == 0:
        return num_list
    if i == length:
        if num_list[max_i] != num_list[length-1]:
            max = num_list[max_i]
            num_list[max_i] = num_list[length-1]
            num_list[length-1] = max
            print(f"swap {num_list[max_i]} <-> {num_list[length-1]} : {num_list}")
        return straight_selection_sort(num_list, length-1)
    else:
        if num_list[max_i] < num_list[i]:
            return straight_selection_sort(num_list, length, i, i+1)
        else:
            return straight_selection_sort(num_list, length, max_i, i+1)
            
inp = [int(i) for i in input("Enter Input : ").split()]
print(straight_selection_sort(inp))