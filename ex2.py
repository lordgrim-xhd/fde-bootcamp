scores = [88, 92, 75, 60, 95]
total=0
for i in scores:
    total=total+i
avg=total/len(scores)
m1=max(scores)
m2=min(scores)
print(f"总分:{total},平均分:{avg},最高:{m1},最低:{m2}")
ages = {"张三": 25, "李四": 30, "王五": 28}
tt=0
for i,n in ages.items():
    print(f"{i}今年{n}岁")
    tt=tt+n
avg1=tt/len(ages)
print(f"平均年龄：{avg1:.2f}")
students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
]
for s in students:
    print(f"{s['name']} 考了 {s['score']}分")

