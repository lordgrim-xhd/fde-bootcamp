# ex8.py —— 带日志的数据加载器
# 知识点：logging 的级别、配置、双输出（文件 + 屏幕）
import csv
import logging
# ============================================================
# 第 1 块：配置日志系统（整个程序只做一次，放在最前面）
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
# ============================================================
# 第 2 块：带日志的加载函数
# ============================================================
def load_students(filename):
    """从 CSV 读学生数据，全程记录日志"""
    result = []
    logging.info(f"开始读取文件：{filename}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                logging.debug(f"第 {i} 行原始数据：{row}")
                try:
                    student = {
                        "name": row["name"],
                        "score": int(row["score"]),
                    }
                    result.append(student)
                except ValueError:
                    logging.warning(f"第 {i} 行数据有误，已跳过：{row}")
    except FileNotFoundError:
        logging.error(f"找不到文件：{filename}")
    logging.info(f"读取结束，成功 {len(result)} 条")
    return result
# ============================================================
# 第 3 块：主程序（只有直接运行这个文件时才执行）
# ============================================================
if __name__ == "__main__":
    students = load_students("students.csv")
    print(f"最终读到 {len(students)} 条")