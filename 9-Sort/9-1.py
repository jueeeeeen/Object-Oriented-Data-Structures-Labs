# Chapter : 9 - item : 1 - หัดใช้ Sort
# ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

inp = [int(i) for i in input("Enter Input : ").split(" ")]
check = True
for i in range(len(inp) - 1):
    if not inp[i] < inp[i+1]:
        print("No")
        check = False
        break

if check:
    print("Yes")