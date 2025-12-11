# Chapter : 10 - item : 1 - จดโพย
# Unordered Search: Transposition Heuristic (พื้นฐาน)

# กล่าวคือ:

# แต่ละครั้งที่ search พบ ให้สลับ record ที่ search พบขึ้นมาข้างหน้า 1 ตำแหน่ง

# แนวคิด: การใช้ครั้งเดียวไม่ได้แปลว่าจะใช้อีกครั้งหนึ่งเสมอไป(ต่างจาก Move to Front Heuristic ที่แต่ละครั้งที่ search พบ ให้เลื่อน record นั้นขึ้นไปอยู่หน้าสุดของ list) แต่การสลับแบบนี้ หากค้นหามากๆ ก็จะเลื่อนขึ้นมาอยู่ข้างหน้าเอง


# เนื้อหา:

# 	นักศึกษาจะได้รับบทเป็น นักศึกษาที่กำลังจะสอบ English Vocabulary ในอีก 1 วัน แต่เนื่องจากวิชาเรียนให้โครงงานจำนวนมาก ทำให้ไม่มีเวลาเตรียมตัวท่องศัพท์มากพอ นักศึกษาจึงคิดแผนการเด็ดๆ นั้นคือการจดโพย แต่การสอบห้ามนำเอกสารใดๆเข้า นักศึกษาจึงหมดหนทาง เลยต้องไปดีลกับพระอินทร์ไว้ว่า ตอนที่ถึงเวลาสอบนักศึกษาจะทำการนั่งทางใน ไปขอดูโพยที่ฝากไว้กับพระอินทร์นั้นเอง แต่การสอบครั้งนี้ ดันไปติดกับการส่ง  Project: OOD พอดี เช่นเดียวกัน นักศึกษาก็ยังทำ  project นั้นไม่เสร็จ จึงต้องรีบสอบ English Vocabulary ในครั้งนี้ให้เสร็จไวๆ ด้วยความโชคดีพระอินทร์ทรงคิดเมตตาได้ช่วยนักศึกษา โดยหากคำใดๆที่นักศึกษาจะมาหาคำนั้นๆอีก พระอินทร์จะทำการเลื่อนคำศัพท์นั้นขึ้นไปข้างหน้า 1 ตำแหน่ง (Transposition Heuristic) เพื่อลดเวลาการที่นักศึกษาจะต้องไล่ดูแต่ละคำใหม่ตั้งแต่ต้น แต่หากคำศัพท์ที่นักศึกษาจะหาไม่อยู่ในโพยที่มอบไว้ให้กับพระอินทร์ ถือว่านักศึกษาจดโพยมาไม่ดีพอ พระอินทร์จะทำการจดศัพท์นี้ต่อท้ายศัพท์คำสุดท้าย เพื่อให้นักศึกษาไปหาความหมาย และเตรียมตัวให้ดีใหม่ในครั้งถัดๆไป


# รายละเอียด:

# Output ที่ต้องแสดง:

# ความหมายของคำศัพท์นั้นๆ

# เวลาที่เจอคำนั้น โดยกำหนดให้:

# เวลาที่เลื่อนคำศัพท์ใดๆ = 1 วินาที ต่อ 1 คำ (ถ้าเจอคำศัพท์นั้นจะหยุดเลื่อน)

# เวลาที่ Return ความหมายนั้นๆ = 1 วินาที

# เวลาที่เพิ่มคำศัพท์นั้นเข้าโพย = 1 วินาที


# โพยคำศัพท์ที่จะมอบให้พระอินทร์:

# unordered_words_and_meanings = {

#     'watermelon': 'A Large fruit',

#     'nectarine': 'Similar to a peach.',

#     'mango': 'Tropical fruit.',

#     'kiwi': 'Small fruit.',

#     'vanilla': 'Used in baking.',

#     'fig': 'Chewy skin.',

#     'pear': 'Sweet fruit.',

#     'cherry': 'Red fruit.',

#     'strawberry': 'Tiny seeds.',

#     'quince': 'Tart flavor.',

#     'ugli fruit': 'Hybrid citrus.'

# }

# *นำ unordered_words_and_meanings ไปวางใน code


# หากคำศัพท์นั้นไม่อยู่ในโพยให้ meaning เหล่านั้นเป็น:

# defalut_meaning = '(Default) A fruit.'


# ตัวอย่าง

# Input :

# Enter a word to search for: kiwi,lion

# อธิบาย input:

# kiwi,lion : คำศัพท์ kiwi และ lion ที่จะค้นหาในโพย		

# Output :

# (1) Word 'mango' found (4 seconds): Tropical fruit.

# >> เวลาที่หาคำ 'mango' คือ 4 seconds: กล่าวคือ 

# 	วินาทีที่ 1 : เลื่อนเจอ watermelon ;ไม่ใช่ศัพท์ที่ต้องการหาเลื่อนต่อ

# 	วินาทีที่ 2 : เลื่อนเจอ nectarine ;ไม่ใช่ศัพท์ที่ต้องการหาเลื่อนต่อ

# 	วินาทีที่ 3 : เลื่อนเจอ mango ;ศัพท์ที่ต้องการหา หยุดเลื่อนต่อ

# 	วินาทีที่ 4 : Return คำอธิบาย mango (Tropical fruit.)

# (2) Word 'lion' added (13 seconds): (Default) A fruit.

# >> เวลาที่หาคำ 'lion' คือ 13 seconds: กล่าวคือ 

# 	วินาทีที่ 1 : เลื่อนเจอ watermelon ;ไม่ใช่ศัพท์ที่ต้องการหาเลื่อนต่อ

# 	….

# 	วินาทีที่ 11 : เลื่อนเจอ ugli fruit ;ไม่ใช่ศัพท์ที่ต้องการ หมดโพย ต้องทำการเพิ่มศัพท์	

# 	วินาทีที่ 12 : เพิ่ม lion เข้าโพย

# 	วินาทีที่ 13 : Return คำอธิบาย lion ซึ่งเป็น default_meaning ((Default) A fruit.)

# (END) Updated dictionary:

# 0: watermelon, 1: mango, 2: nectarine, 3: kiwi, 4: vanilla, 5: fig, 6: pear, 7: cherry, 8: strawberry, 9: quince, 10: ugli fruit, 11: lion

# >> โพยที่ถูกปรับเปลี่ยนโดยพระอินทร์ โดยระบุคำศัพท์คู่กับลำดับของมัน(เริ่มจาก 0)

# (SUMMARY OF INDEX CHANGES):

# mango: 2 -> 1

# lion: None -> 11

# >> กล่าวคือ mango เลื่อน index มาข้างหน้า 1 ตำแหน่ง จาก index 2 เป็น 1 และ lion ไม่เคยมีศัพท์นี้ (None) จนเพิ่มเข้ามาที่ตำแหน่งที่ 11 นั้นเอง

unordered_words_and_meanings = {

    'watermelon': 'A Large fruit',

    'nectarine': 'Similar to a peach.',

    'mango': 'Tropical fruit.',

    'kiwi': 'Small fruit.',

    'vanilla': 'Used in baking.',

    'fig': 'Chewy skin.',

    'pear': 'Sweet fruit.',

    'cherry': 'Red fruit.',

    'strawberry': 'Tiny seeds.',

    'quince': 'Tart flavor.',

    'ugli fruit': 'Hybrid citrus.'
}

defalut_meaning = '(Default) A fruit.'

def print_updated_dict(updated_dict):
    print("(END) Updated dictionary:")
    for i in range(len(updated_dict)):
        if i != 0:
            print(", ", end="")
        print(f"{i}: {updated_dict[i]}", end = "")
    print()

def transposition_search(keys):
    updated_dict = [key for key in unordered_words_and_meanings.keys()]
    summary = {}
    for i in range(len(keys)):
        time = 1
        for word in updated_dict:
            if keys[i] == word:
                print(f"({i+1}) Word '{word}' found ({time+1} seconds): {unordered_words_and_meanings[word]}")
                if time-1 > 0:
                    updated_dict[time-2], updated_dict[time-1] = updated_dict[time-1], updated_dict[time-2]
                if word not in summary.keys():
                        summary[word] = time-1
                break
            time += 1
        else:
            unordered_words_and_meanings[keys[i]] = defalut_meaning
            print(f"({i+1}) Word '{keys[i]}' added ({time+1} seconds): {unordered_words_and_meanings[keys[i]]}")
            updated_dict.append(keys[i])
            summary[keys[i]] = None
    print_updated_dict(updated_dict)
    index_summary(summary, updated_dict)

def index_summary(summary, dictionary):
    print("(SUMMARY OF INDEX CHANGES):")
    for key in summary.keys():
        for i in range(len(dictionary)):
            if dictionary[i] == key:
                print(f"{key}: {summary[key]} -> {i}")
                break

words = [word.strip().lower() for word in input("Enter a word to search for: ").split(",")]
transposition_search(words)