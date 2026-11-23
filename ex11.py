# ex11.py —— 从数据库取数，复用已有的分析与报表函数
#
# 分层结构：
#   ① init_db                → 数据层：准备数据（幂等，只在第一次真正建表）
#   ② load_students_from_db  → 数据层：读取数据
#   ③ analyze                → 业务层：计算统计
#   ④ print_report           → 显示层：输出报表

import sqlite3

from ex3 import analyze, print_report


def init_db(db_path):
    """初始化数据库：建表 + 插入示例数据。

    幂等设计：如果 students 表已经存在，就什么都不做。
    所以这个脚本可以反复运行，不会重复插入、不会清掉已有数据。
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # sqlite_master 是 SQLite 的系统表，记录库里所有表 / 索引 / 视图
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'students'"
    )
    if cur.fetchone() is not None:
        print("[init_db] students 表已存在，跳过初始化")
        conn.close()
        return

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
        ],
    )

    conn.commit()
    conn.close()
    print("[init_db] 初始化完成，已插入 6 条示例数据")


def load_students_from_db(db_path):
    """只读：从数据库取学生数据，返回 list of dict。

    返回的形状和 CSV / JSON 版本完全一致：
        [{"name": "张三", "score": 88}, ...]
    所以 analyze 和 print_report 不需要任何修改。
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT name, score FROM students")
    rows = cur.fetchall()

    # Row 对象不是 dict，用列表推导式逐个转换
    students = [dict(r) for r in rows]

    conn.close()
    return students


if __name__ == "__main__":
    DB = "school.db"

    init_db(DB)                                    # ① 准备数据（幂等）
    students = load_students_from_db(DB)           # ② 读取
    stats = analyze(students)                       # ③ 计算
    print_report(students, stats)                   # ④ 显示
