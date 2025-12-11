# Chapter : 9 - item : 3 - insertion sort [recursive]
#  ส่งมาแล้ว 2 ครั้ง
# เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def find_index(l: list, i: int, end: int): # ใช้เพื่อหาตำแหน่งที่เหมาะสมในการแทรกค่า โดยการเลื่อนค่าที่มากกว่าไปทางขวา
    if i < 0 or l[i] < end: 
        return i
    l[i + 1] = l[i] # เลื่อนไปทางขวา
    return find_index(l, i - 1, end)

def insertion(l: list, n: int):
    if n <= 1:
        return
    insertion(l, n - 1)
    end = l[n - 1]
    i = find_index(l, n - 2, end)
    l[i + 1] = end
    print(f'insert {end} at index {i + 1} : ', end='')
    print(f'{l[:n]} {l[n:]}' if len(l) > n else f'{l}')


inp = [int(i) for i in input('Enter Input : ').split()]
insertion(inp, len(inp))
print('sorted')
print(inp)
