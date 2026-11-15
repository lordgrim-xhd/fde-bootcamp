import csv
from ex3 import analyze, print_report     # ← 复用你昨天写的函数！

def load_students(filename):
    """从 CSV 读学生数据，返回 list of dict（score 要转成 int）"""
    result=[]
    with open(filename, "r", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            student = {
            "name": row["name"],
            "score": int(row["score"]),     # ← 别忘了转换
            }
            result.append(student)
    return result
            
students = load_students("students.csv")
stats = analyze(students)
print_report(students, stats)