from ex3 import get_level, analyze


def test_get_level_优秀():
    assert get_level(95) == "优秀"


def test_get_level_及格():
    assert get_level(75) == "及格"


def test_get_level_不及格():
    assert get_level(58) == "不及格"
def test_analyze_四个学生():
    students = [
        {"name": "张三", "score": 88},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 75},
        {"name": "赵六", "score": 58},
    ]
    stats = analyze(students)

    assert stats["total"] == 313
    assert stats["average"] == 78.25
    assert stats["max_name"] == "李四"
    assert stats["min_name"] == "赵六"
    assert stats["pass_count"] == 3
    assert stats["pass_rate"] == 75.0
def test_analyze_只有一个学生():
    students = [{"name": "张三", "score": 88}]
    stats = analyze(students)

    assert stats["total"] == 88
    assert stats["max_score"] == 88
    assert stats["min_score"] == 88     # ← 关键：最大最小必须是同一个人
    assert stats["average"] == 88.0
import pytest

def test_analyze_空列表():
    with pytest.raises(ValueError):
        analyze([])