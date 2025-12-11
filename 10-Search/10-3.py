# Chapter : 10 - item : 3 - Fun with hashing
#  ส่งมาแล้ว 6 ครั้ง
# ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

# 1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
# 2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
# 3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
# 4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ



# class Data:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

#     def __str__(self):
#         return "({0}, {1})".format(self.key, self.value)

# class hash:

#     # Code Here

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
    
    def get_index(self):
        index = 0
        for c in self.key:
            index += ord(c)
        return index
    
class hash:
    def __init__(self, size, max_collision):
        self.table = [None] * size
        self.max_collision = max_collision
        self.data_size = 0
        
    def print_table(self):
        for i in range(len(self.table)):
            print(f"#{i+1}	{self.table[i]}")
            
    def is_full(self):
        if self.data_size == len(self.table):
            print("This table is full !!!!!!")
            return True

    def insert(self, key, value):
        new_data = Data(key, value)
        original_index = new_data.get_index()
        index = original_index % len(self.table)
        collision = 0
        
        while (index) < len(self.table) and self.table[index] is not None and collision < max_collision:
            collision += 1
            print(f"collision number {collision} at {index}")
            index = (original_index + (collision ** 2)) % len(self.table)
            

        if collision >= max_collision:
            print("Max of collisionChain")
        else:
            self.table[index] = new_data
            self.data_size += 1
            
print(" ***** Fun with hashing *****")
size, datas = input("Enter Input : ").split("/")
size, max_collision = map(int, size.split())
datas = datas.split(",")
hash_table = hash(size, max_collision)

for data in datas:
    if hash_table.is_full(): break
    key, value = data.split()
    hash_table.insert(key, value)
    hash_table.print_table()
    print("---------------------------")