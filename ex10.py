import sqlite3

conn = sqlite3.connect("school.db")
conn.row_factory = sqlite3.Row        # ← 先记下这行，第 5 节会讲
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS students")
cur.execute("""
    CREATE TABLE students (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        dept  TEXT,
        score INTEGER
    )
""")

cur.executemany(
    "INSERT INTO students (name, dept, score) VALUES (?, ?, ?)",
    [
        ("张三", "技术部", 88),
        ("李四", "技术部", 92),
        ("王五", "销售部", 75),
        ("赵六", "销售部", 58),
        ("钱七", "技术部", 65),
        ("孙八", "销售部", 90),
    ]
)
conn.commit()
cur.execute("SELECT name, score FROM students ORDER BY score DESC LIMIT 3")
for row in cur.fetchall():
    print(row["name"],row["score"])  
cur.execute("SELECT SUM(score) AS 总分, ROUND(AVG(score),2) AS 平均分, MAX(score) AS 最高, MIN(score) AS 最低 FROM students")
print(dict(cur.fetchone()))
cur.execute("SELECT dept AS 部门,count(*) AS 人数 FROM students group by dept")
for row in cur.fetchall():
    print(dict(row))
cur.execute("""
    SELECT dept AS 部门,ROUND(AVG(score),2) AS 平均分
    FROM students
    GROUP BY dept
    ORDER BY 平均分 DESC""")
for row in cur.fetchall():
    print(dict(row))
cur.execute("""
    SELECT dept AS 部门,ROUND(AVG(score),2) AS 平均分
    FROM students
    GROUP BY dept
    HAVING ROUND(AVG(score), 2) >= 75""")
for row in cur.fetchall():
    print(dict(row))