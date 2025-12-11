# Chapter : 9 - item : 4 - Find the Running Median
#  ส่งมาแล้ว 1 ครั้ง
# เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# l = [e for e in input("Enter Input : ").split()]
# if l[0] == 'EX':
#     Ans = "xxx"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
#     l=list(map(int, l))
#     #code here


# ***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

# พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

# - bubble sort

# - straight selection sort

# - insertion sort

# - shell sort

# - merge sort

# - quick sort

# - minHeap and maxHeap

# พิมพ์คำตอบลงในช่อง Ans = "xxx"

# ***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***

def bubble_sort(numbers):
    for last in range(len(numbers) - 1, 0, -1):
        swapped = False
        for i in range(last):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
    return numbers

def median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n//2]
    else:
        return (numbers[(n//2)-1] + numbers[n//2])/2

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "quick sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    number_list = []
    for i in l:
        number_list.append(i)
        median_index = (len(number_list)+1)/2
        print(f"list = {number_list} : median = {median(bubble_sort(number_list.copy())):.1f}")