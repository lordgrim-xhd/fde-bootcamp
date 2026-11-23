# FDE 训练仓库

从零基础转行 **FDE（Forward Deployed Engineer，前置交付工程师）** 的训练记录。

原则：**每天一个可运行的产出**，不写只读过但跑不起来的代码。

## 环境

- Python 3.12
- pytest（单元测试）

## 文件说明

| 文件 | 内容 | 用到的知识点 |
|---|---|---|
| `type_demo.py` | 类型与运算符 | `int` / `str` / `float`、类型转换 |
| `ex1.py` | 基础语法练习 | 变量、f-string、`for`、类型转换 |
| `ex2.py` | 列表与字典 | `list`、`dict`、`list` 套 `dict` |
| `ex3.py` | 成绩报表生成器 | 单次遍历、函数拆分、职责分离 |
| `ex4.py` | 函数练习 | `def` / `return`、打擂台找最值 |
| `ex5.py` | CSV 数据加载 | 文件读写、`csv.DictReader`、异常处理 |
| `ex6.py` | JSON 读写 | `json.dump/load`、类型保留 |
| `ex7.py` | while 循环 | `while` / `break`、猜数字游戏 |
| `ex8.py` | 带日志的数据加载 | `logging` 分级、双输出 |
| `ex9.py` | SQLite 入门 | 建表、参数化插入、`SELECT` / `WHERE` |
| `ex10.py` | SQL 进阶 | `ORDER BY`、聚合函数、`GROUP BY` / `HAVING` |
| `ex11.py` | 数据库 → 报表 | 分层设计、`row_factory`、幂等初始化 |
| `test_ex3.py` | 单元测试 | pytest、边界值、异常断言 |
| `demo_csv_reader.py` | CSV 读取方式对比 | `csv.reader` vs `DictReader` |
| `students.csv` | 示例数据 | CSV 格式 |
| `students.json` | 示例数据 | JSON 格式（同一份数据的另一种表示） |

## 运行

```bash
# 带日志的数据加载
python ex8.py

# 运行测试
python -m pytest test_ex3.py -v

# CSV 读取方式对比演示
python demo_csv_reader.py
```

## 代码特点

- **函数职责单一**：`analyze` 只负责计算，`print_report` 只负责显示，互不掺和
- **异常处理分策略**：`analyze` 对空输入抛 `ValueError`（拒绝服务），`load_students` 对缺失文件返回空列表（兜底），两种策略各有测试锁定
- **测试覆盖三条路径**：正常数据、边界情况（单学生）、异常情况（空列表）
- **日志分级**：`DEBUG` 记录每行原始数据，`INFO` 记录流程，`WARNING` 记录脏数据跳过，`ERROR` 记录文件缺失
- **编码显式声明**：所有文件读写都带 `encoding="utf-8"`，避免跨平台乱码

## 学习进度

| 日期 | 内容 |
|---|---|
| 11/09 | 环境搭建、第一个 Python 脚本 |
| 11/10 | Git 本地仓库与 GitHub 推送 |
| 11/12 | 成绩报表 v1（单次遍历、发现 `elif` 潜伏 bug） |
| 11/13 | 函数与模块化、第一道客户场景题 |
| 11/14 | 重构：把流水账拆成三个函数 |
| 11/15 | 文件读写、CSV 解析、类型转换陷阱 |
| 11/16 | 异常处理三层防护、边界测试 |
| 11/17 | JSON 序列化、编码问题排查 |
| 11/18 | `while` 循环、pytest 入门 |
| 11/22 | logging、仓库整理（`.gitignore`）、SQL 入门 |
| 11/23 | SQL 进阶（分组统计）、数据库接回报表程序 |

## 下一步

- 调用 LLM API，构建第一个 CLI 工具
- RAG 检索系统（主项目）
