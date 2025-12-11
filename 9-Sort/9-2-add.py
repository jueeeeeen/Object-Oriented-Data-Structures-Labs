# Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ
# ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def bubble_positive(numbers):
    for last in range(len(numbers) - 1, 0, -1):
        swaped = False
        for i in range(last):
            count = 1
            if not numbers[i] < 0:
                while i+count < last and numbers[i+count] < 0:
                    count += 1
                if numbers[i] > numbers[i+count] and numbers[i+count] >= 0:
                    numbers[i], numbers[i+count] = numbers[i+count], numbers[i]
                    swaped = True
        if not swaped:
            break
    return numbers

inp = [int(i) for i in input("Enter Input : ").split(" ")]
for i in bubble_positive(inp):
    print(i, end=" ")