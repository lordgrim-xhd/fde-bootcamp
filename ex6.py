import json

students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
    {"name": "赵六", "score": 58},
]
with open("students.json", "w", encoding="utf-8") as f:
     json.dump(students,f,ensure_ascii=False,indent=2)
with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))                    # 整体
print(type(data[0]))                 # 单个元素
print(type(data[0]["score"]))        # ← 重点
print(data[0]["score"] + 12)         # 能不能直接算
def load_students_json(filename):
    """从 JSON 读学生数据，返回 list of dict"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"找不到文件：{filename}")
        return []

    except json.JSONDecodeError:
        print(f"JSON 格式错误：{filename}")
        return []
students2 = load_students_json("students.json")
print(f"读到 {len(students2)} 个学生")
print(students2[0])
print(type(students2[0]["score"]))
# 测试 1：文件不存在
print(load_students_json("根本不存在的文件.json"))

# 测试 2：JSON 格式错误
with open("bad.json", "w", encoding="utf-8") as f:
    f.write('{"name": "张三",')     # 故意坏掉

print(load_students_json("bad.json"))
# 写到 students.json，要求：
# - 中文不转义
# - 缩进 2 格，方便人看
from ex5 import load_students

s1 = load_students("students.csv")          # CSV 路径
s2 = load_students_json("students.json")    # JSON 路径

print(s1 == s2)
print(len(s1), len(s2))