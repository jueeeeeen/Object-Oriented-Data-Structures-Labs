# Chapter : 9 - item : 2 - มากไปน้อยที่ไม่ใช่ค่ามากไปน้อย
# ให้เรียงลำดับ input จากเลขที่มีค่าซ้ำกันมากที่สุด ไป ซ้ำน้อยที่สุด
# มีเงื่อนไขว่า หากเลขที่มีจำนวนซ้ำเท่ากันให้แสดงจากเลขที่มาก่อนไปหลังเสมอ 

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def duplicate_sorted(lst):
    new_lst, count = [], 1
    curr_value = lst[0]
    
    for i in range(1, len(lst)):
        # print(curr_value, lst[i])
        if curr_value == lst[i]:
            count += 1
        else:
            new_lst.append([curr_value, count])
            curr_value = lst[i]
            count = 1  
    new_lst.append([curr_value, count])          
    
    # print(new_lst)   
    for i in range(1, len(new_lst)):
        curr = new_lst[i]
        for j in range(i, -1, -1):
            if j > 0 and new_lst[j - 1][1] < curr[1]:
                new_lst[j] = new_lst[j - 1]       
            else:   
                new_lst[j] = curr
                break
    return new_lst

inp = [int(i) for i in input("Enter list  of numbers: ").split()]
sorted_list = duplicate_sorted(inp)

for i in sorted_list:
    print(f"number {i[0]}, total: {i[1]}")
