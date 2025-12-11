# Chapter : 9 - item : 3 - Have fun with sorting card

# วันนี้เราจะมาทำการเรียงการ์ดกันโดยไพ่โดยพี่คิดว่าน้องๆ หน้าจะรู้จักกันแล้ว แต่พี่จะอธิบายให้ฟังอีกครั้ง โดยการ์ดนั้นแบ่งออกเป็น 2 ส่วน คือหน้าไพ่(symbol) มี 4 แบบ คือ

# ดอกจิก(Clover) ข้าวหลามตัด(Diamonds) โพแดง(Hearts) โพดำ(Spades) โดยตัวย่อ C, D, H, S ตามลำดับโดยเรียงค่าจากน้อยไปมาก

# และ อีกส่วนคือเลข (num) ประกอบด้วย เลข 2 - 9 แล้วต่อด้วย T(10) , J (jack) , Q (queen คนไทยนิยมเรียกว่า แหม่ม) , K (king) , A (ace) โดยเรียงค่าจากน้อยไปมาก

# ในเมื่อตอนนี้น้องๆรู้เกี่ยวกับการ์ดกันแล้ว การเรียงการ์ดที่จะใช้ในโจทย์ครั้งนี้นั้นมี 2 วิธี คือ

# เรียงโดย เรียงเลขก่อน (num) คือ เรียง 2 ดอกจิก 2 ข้าวหลามตัด 2 โพแดง 2 โพดำ แล้วไป 3 ดอกจิก … จนถึง A โพดำ

# เรียง ดอกก่อน(symbol) คือ 2 ดอกจิก 3 ดอกจิก … A ดอกจิก 2ข้าวหลามตัด … จนถึง A โพดำ


# Enter Input: C5,CK,H7,D2,DA,H3,S4/symbol

# โดย input จะประกอบโดยตัวอักษร 2 ตัว เช่น C5 โดยตัวแรกคือดอก แล้ว ตัวหลังคือเลข และขั้นด้วย , เป็นการ์ดใบต่อไป โดยด้านหลัง / คือรูปแบบการเรียง คือ  num หรือ symbol

# ถ้ามีการ์ดซ้ำกันให้ข้ามการ์ดใบนั้นทิ้งแล้วพิมพ์ “Error: Duplicate card found - H7”แล้วตามด้วยชื่อการ์ดใบนั้นในกรณีนี้คือ H7 

# ถ้ามีการใส่การ์ดที่ไม่มีอยู่จริง ก็ให้ข้ามการ์ดใบนั้นแล้วพิมพ์ “Error: X9 is an invalid card” พร้อมบอกชื่อการ์ดใบนั้นในกรณีนี้คือ X9 

# ถ้าไม่มีการ์ดให้เรียงไม่ว่าจะเกิดจากการที่มีแต่การ์ดแปลกๆหรือไม่มีการ์ดให้พิมพ์ ”No valid cards to sort.” ออกมา

# ***หมายเหตุ ห้ามใช้ทำสั่ง .sort() ข้อนี้อยากใช้อยากใช้วิธีใหนในการเรียงใช้ได้หมด แต่พี่แนะนำให้ลองใช้ insert sort***

# ***หมายเหตุ 2: หากอยากท้าทายโจทย์นี้ให้ยากขึ้นลองทำเป็น recursive ดู ไม่ได้บังคับไม่อยากทำก็ได้แล้วแต่น้อง***

def bubble_sort(cards, st_i, nd_i, first, second):
    for i in range(len(cards)):
        for j in range(0, len(cards) - i - 1):
            if (first.index(cards[j][st_i]) > first.index(cards[j+1][st_i])) or \
                (first.index(cards[j][st_i]) == first.index(cards[j+1][st_i]) and second.index(cards[j][nd_i]) > second.index(cards[j+1][nd_i])):
                cards[j], cards[j+1] = cards[j+1], cards[j]

print('Have fun with sort card')
inp, sort_type = input('Enter Input: ').split('/')
inp = inp.split(',')
symbols = ['C', 'D', 'H', 'S']
nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
sorted_cards = []

for i in inp:
    if i and (len(i) != 2 or i[0] not in symbols or i[1] not in nums):
        print(f'Error: {i} is an invalid card')
    elif i in sorted_cards:
        print(f'Error: Duplicate card found - {i}')
    elif i:
        sorted_cards.append(i)

if not sorted_cards:
    print('No valid cards to sort.')
else:
    if sort_type == 'num':
        bubble_sort(sorted_cards, 1, 0, nums, symbols)  
    elif sort_type == 'symbol':
        bubble_sort(sorted_cards, 0, 1, symbols, nums)  
    print(f'Sorted cards : {" ".join(sorted_cards)}', end = '')