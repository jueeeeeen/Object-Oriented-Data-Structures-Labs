# Chapter : 9 - item : 1 - bubble sort [recursive]
# เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def bubble_recur(l,i):
    if i == 0 :
        return l
    l = _bubble(l,int(i-1),0)
    return bubble_recur(l,int(i-1))

def _bubble(l,end,i):
    if i == end or i == len(l):
        return l
    if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
    return _bubble(l,end,int(i+1))

inp = [int(a) for a in input("Enter Input : ").split()]
bubble_recur(inp,len(inp))
print(inp)