def get_level(score):
    if score>=90:
        return "优秀"
    elif score>=60:
        return "及格"
    else:
        return "不及格"
print(get_level(95))   # 应该输出 优秀
print(get_level(75))   # 应该输出 及格
print(get_level(58))   # 应该输出 不及格

students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
]



def find_max(students):
    # 返回分数最高的那个学生（返回整个 dict）
    max_student=students[0]
    for i in students:
        if i["score"]>max_student["score"]:
            max_student=i
            
    return max_student

best = find_max(students)
print(best["name"], best["score"])   # 李四 92
students2 = [
    {"name": "赵六", "score": 60},
    {"name": "钱七", "score": 70},
]
best2 = find_max(students2)
print(best2["name"], best2["score"])   # 应该是 钱七 70