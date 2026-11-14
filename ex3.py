# 成绩报表生成器
# 知识点：单次遍历、if/elif 分支、打擂台找最值、字符串格式化
# 已验证：打乱数据顺序后，最高/最低分仍然正确
def analyze(students):
    """一次遍历，返回所有统计数字"""

    # ===== ① 初始化：全部 4 格缩进 =====
    total = 0
    max_score = students[0]["score"]
    max_name = students[0]["name"]
    min_score = students[0]["score"]
    min_name = students[0]["name"]
    count = 0

    # ===== ② 循环：4 格 =====
    for s in students:
        if s["score"] >= 60:
            count=count+1
          
        if s["score"] > max_score:
            max_score = s["score"]
            max_name = s["name"]
        if s["score"] < min_score:
            min_score=s["score"]
            min_name = s["name"]

        total = total + s["score"]

    # ===== ④ 循环之后：4 格 =====
    average = total / len(students)
    pass_rate = count / len(students) * 100

    # ===== ⑤ 返回：4 格 =====
    return {
        "total": total,
        "average": average,
        "max_name": max_name,
        "max_score": max_score,
        "min_name": min_name,
        "min_score": min_score,
        "pass_count": count,
        "pass_rate": pass_rate,
    }
def print_report(students, stats):
    """打印成绩报表"""
    print("=" * 36)
    print(f"{'姓名':<10}{'分数':>8}{'等级':>10}")
    print("-" * 36)

    
    def get_level(score):  
            if score >= 90:
                return"优秀"
            elif score>=60:
    
                return"及格"
            else:
                return"不及格"
    for s in students:
        level=get_level(s["score"])
        print(f"{s['name']:<10}{s['score']:>8}{level:>10}")
        

    print("=" * 36)
    
    print(f"总分：{stats['total']}    平均：{stats['average']:.2f}")
    print(f"最高：{stats['max_score']}（{stats['max_name']}）    最低：{stats['min_score']}（{stats['min_name']}）")
    print(f"及格人数：{stats['pass_count']}/{len(students)}    及格率：{stats['pass_rate']:.1f}%")

students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
    {"name": "赵六", "score": 58},
]

stats = analyze(students)
print_report(students, stats)


