# Chapter : 9 - item : 4 - Sort by alphabet
#  ส่งมาแล้ว 1 ครั้ง
# ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def Quicksort(a):
    if len(a) < 2:
        return a
    
    pivot = a[0]
    left = [i for i in a[1:] if i < pivot]
    right = [i for i in a[1:] if i >= pivot]
    return Quicksort(left) + [pivot] + Quicksort(right)

inp = [i for i in input('Enter Input : ').split()]

# สร้างลิสต์เก็บตัวอักษรจาก string แต่ละตัว
char_list = []
for i in inp:
    for j in i:
        if j.isalpha():
            char_list.append(j)

# แปลงตัวอักษรเป็นลำดับ ASCII แล้วทำการเรียงโดยวิธี Quicksort
ascii_values = [ord(char) for char in char_list]
sorted_ascii_values = Quicksort(ascii_values)

sorted_chars = [chr(i) for i in sorted_ascii_values] # แปลงค่า ASCII กลับมาเป็นตัวอักษร

# จับคู่ string เดิมกับตัวอักษรที่ถูกเรียงแล้ว
sorted_inp = []
for sorted_char in sorted_chars:
    for i in inp:
        if sorted_char in i and i not in sorted_inp: 
            sorted_inp.append(i)
            break

print(' '.join(sorted_inp))
