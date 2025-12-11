# Chapter : 10 - item : 5 - Job
# คุณ CEO มีงานหลายชิ้นที่ต้องการแบ่งให้กับพนักงาน k คน หาระยะเวลาที่น้อยที่สุดที่สามารถแบ่งงานให้กับผู้ทำงาน k คนได้

# Input: 1 2 3 4/2
#     งานแต่ละชิ้นใช้เวลาต่างกัน = 1 2 3 4
#     คน = 2
# Output: 5

# แบ่งงานเป็นสองกลุ่มได้เป็น 1 4 ใช้เวลารวม 5 และ 2 3 ใช้เวลารวม 5 ดังนั้นระยะเวลาที่น้อยที่สุดคือ 5

# ยกตัวอย่างเพิ่ม testcase 8
# กลุ่ม 1: 29 + 11 = 40
# กลุ่ม 2: 31 + 7 = 38
# กลุ่ม 3: 19 + 19 = 38
# กลุ่ม 4: 17 + 13 + 5 + 3 = 38

# Hint: Binary Search & Backtracking / Dynamic Programming จะใช้อะไรก็ได้ 


def can_split(jobs, workers, maxTime, index=0, workload=None):
    if workload is None:
        workload = [0] * workers

    # base case
    if index == len(jobs):
        return True

    for i in range(workers):
        # print(workload,jobs[index])
        if workload[i] + jobs[index] <= maxTime:
            workload[i] += jobs[index]
            
            if can_split(jobs, workers, maxTime, index + 1, workload):
                return True
            else:
                workload[i] -= jobs[index]

        if workload[i] == 0:
            break
    # print()
    return False

def find_min_max_time(jobs, k):
    low = max(jobs) # 1 person - max time job
    high = sum(jobs) # 1 person - all job
    
    while low < high:
        mid = (low + high) // 2
        if can_split(jobs, k, mid):
            high = mid 
        else:
            low = mid + 1 
    return low

inp = input('Enter jobs and number of workers : ').split('/')
lst1 = [int(a) for a in inp[0].split()]
n = int(inp[1])
print(f"Minimum time to complete jobs with {inp[1]} workers is ",end="")
if min(lst1)==max(lst1):
    print((sum(lst1)+n-1)//n)
else:
    print(find_min_max_time(lst1,n))
