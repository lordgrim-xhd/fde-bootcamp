import csv
from ex3 import analyze, print_report     # ← 复用你昨天写的函数！

def load_students(filename):
    """从 CSV 读学生数据，返回 list of dict（score 要转成 int）"""
    result=[]
    try:   
        with open(filename, "r", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            for row in reader:
                try:
                    student = {
                    "name": row["name"],
                    "score": int(row["score"]),     # ← 别忘了转换
                    }
                    result.append(student)
                except ValueError:
                    print(f"跳过脏数据：{row}")
    except FileNotFoundError:
        print(f"找不到文件：{filename}")
        print("请确认文件在当前目录，并且名字拼写正确")
                 
    return result
            
students = load_students("students.csv")
if not students:
    print("没有可处理的数据，程序结束")
else:
    stats = analyze(students)
    print_report(students, stats)