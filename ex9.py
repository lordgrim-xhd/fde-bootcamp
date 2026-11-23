import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT ONT NULL,
    score INTEGER
    )
""")
 
cur.executemany(
    "INSERT INTO students(name,score)VALUES(?,?)",
    [("张三", 88), ("李四", 92), ("王五", 75), ("赵六", 58)]
)
conn.commit() 
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)
cur.execute("SELECT name, score FROM students WHERE score >= 80")
for row in cur.fetchall():
    print(row)
conn.close()