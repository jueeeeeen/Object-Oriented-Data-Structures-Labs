# Chapter : 10 - item : 4 - Rehashing
# ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
# 1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
# 2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

# หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

# การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
class hash:
    def __init__(self, size, max_collision, treshold):
        self.table = [None] * size
        self.max_collision = max_collision
        self.treshold = treshold
        self.size = size
        self.data_size = 0
        
    def print_table(self):
        for i in range(len(self.table)):
            print(f"#{i+1}	{self.table[i]}")
            
    def new_size(self):
        size = self.size * 2
        while not hash.is_prime(size):
            size += 1
        return size
    
    def treshold_exceeded(self):
        return self.data_size >= (self.size * self.treshold) / 100
    
    def is_prime(num, comp = 2):
        if comp == num: return True
        if num < comp or num % comp == 0:return False
        return hash.is_prime(num, comp+1)
        
    def insert(self, data):
        index = data % self.size
        collision = 0
        
        while self.table[index] is not None:
            collision += 1
            print(f"collision number {collision} at {index}")
            if collision >= max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash(data)
                return
            index = (data + (collision ** 2)) % self.size
        
        self.data_size += 1
        if self.treshold_exceeded():
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(data)
            return
        self.table[index] = data
                
    def rehash(self, data = None):
        new_hash = hash(self.new_size(), max_collision, treshold)
        for val in datas:
            new_hash.insert(val)
            if data == val:
                break
        self.table = new_hash.table
        self.size = new_hash.size
                    
print(" ***** Rehashing *****")
size, datas = input("Enter Input : ").split("/")
size, max_collision ,treshold= map(int, size.split())
datas = list(map(int, datas.split()))
hash_table = hash(size, max_collision, treshold)

print("Initial Table :")
hash_table.print_table()
print("----------------------------------------")

for data in datas:
    print("Add : " + str(data))
    hash_table.insert(data)
    hash_table.print_table()
    print("----------------------------------------")

