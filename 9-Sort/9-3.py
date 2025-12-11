# Chapter : 9 - item : 3 - somethingDROME
# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง


def somethingDROME(numbers):
    increase = False
    decrease = False
    same = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            decrease = True
        elif numbers[i] < numbers[i+1]:
            increase = True
        else:
            same = True
    if increase and not decrease:
        if same:
            return "Plaindrome"
        else:
            return "Metadrome"
    elif not increase and decrease:
        if same:
            return "Nialpdrome"
        else:
            return "Katadrome"
    elif not increase and not decrease and same:
        return "Repdrome"
    else:
        return "Nondrome"

inp = [int(i) for i in input("Enter Input : ")]
print(somethingDROME(inp))