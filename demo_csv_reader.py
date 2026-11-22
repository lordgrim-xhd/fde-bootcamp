import csv

print("=" * 60)
print("原始文件长什么样（前 2 行，repr 显示隐藏字符）")
print("=" * 60)
with open("students.csv", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= 2:
            break
        print(f"  第{i+1}行: {repr(line)}")

print()
print("=" * 60)
print("方式 A：csv.reader —— 每行是一个【列表】，靠下标取")
print("=" * 60)
with open("students.csv", "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(f"  {row}   类型={type(row).__name__}")

print()
print("=" * 60)
print("方式 B：csv.DictReader —— 每行是一个【字典】，靠列名取")
print("=" * 60)
with open("students.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"  {row}")
        print(f"     取名字：row['name'] = {row['name']!r}")

print()
print("=" * 60)
print("关键对比：如果 CSV 把两列顺序换了会怎样")
print("=" * 60)

# 造一个列顺序反过来的文件
with open("_swapped.csv", "w", encoding="utf-8") as f:
    f.write("score,name\n")
    f.write("88,张三\n")

print("  _swapped.csv 的内容：score,name / 88,张三")
print()

with open("_swapped.csv", "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(f"  csv.reader   : row[0]={row[0]!r}  row[1]={row[1]!r}")
        print(f"                 → 如果你按下标取 row[0] 当名字，就拿到 '88' 了 ❌")

with open("_swapped.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"  DictReader   : row['name']={row['name']!r}  row['score']={row['score']!r}")
        print(f"                 → 不管列在第几，取名字永远拿到 '张三' ✅")

import os
os.remove("_swapped.csv")
