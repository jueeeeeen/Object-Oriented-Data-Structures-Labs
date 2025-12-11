# Chapter : 9 - item : 5 - Premier League Score
# สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# [ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

# ตัวอย่าง

# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68

def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        # print(array[j])
        if array[j][1]["points"] > pivot[1]['points']:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
        if array[j][1]["points"] == pivot[1]['points']:
            if array[j][2]["gd"] >= pivot[2]["gd"]:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

inp = input("Enter Input : ").split("/")
all_team = []
for team in inp:
    team = team.split(",")
    point = 3 * int(team[1]) + 0 * int(team[2]) + 1 * int(team[3])
    gd = int(team[4]) - int(team[5])
    point_dict ={'points': point}
    gd_dict = {'gd': gd}
    team_info = [team[0],point_dict,gd_dict]
    all_team.append(team_info)
    
print("== results ==")
quickSort(all_team,0,len(all_team)-1)
for team in all_team:
    print(team)