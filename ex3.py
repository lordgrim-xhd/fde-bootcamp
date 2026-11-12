students = [
    {"name": "张三", "score": 58},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
    {"name": "赵六", "score": 88},
]
total = 0
max_score = 0
max_name = ""
min_score = 100
min_name = ""
count=0

for s in students:
    if s["score"] >= 90:
        level = "优秀"
        count=count+1
    elif s["score"] >= 60:
        count=count+1
        level = "及格"
    else:
        level = "不及格"
    
    if s["score"] > max_score:
        max_score = s["score"]
        max_name = s["name"]
    if s["score"] < min_score:
        min_score=s["score"]
        min_name = s["name"]
    print(s["name"], s["score"], level)
    

    total = total + s["score"]

average = total / len(students)
rate=count / len(students)*100

print(f"总分：{total}    平均：{average}")   
print(f"最高:{max_score}({max_name})  最低:{min_score}({min_name})")
print(f"及格人数：{count}/{len(students)}    及格率：{rate:.1f}%")