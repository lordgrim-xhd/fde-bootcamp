"""手写一个最小检索器：不依赖任何框架，只靠 math 和 collections。"""

import math
from collections import Counter

# ========== ① 语料：模拟公司的制度文档 ==========
DOCS = [
    "员工报销需要提交发票原件，审批流程为：直属主管、财务、财务总监。一般 5 个工作日到账。",
    "年假天数按工龄计算：满 1 年 5 天，满 5 年 10 天，满 10 年 15 天。",
    "产假为 158 天，难产增加 15 天。男方陪产假 15 天。",
    "差旅住宿标准：一线城市每晚 500 元，二线城市每晚 350 元。",
]


# ========== ② 切词：把文本变成词条列表 ==========
def tokenize(text):
    """中文没有空格，用「字符二元组」当词条。

    "报销流程" → ["报销", "销流", "流程"]
    好处：不依赖分词库，且能保留词序信息。
    """
    clean = "".join(ch for ch in text if ch.strip())
    return [clean[i:i + 2] for i in range(len(clean) - 1)]


# ========== ③ 向量化：词条列表 → 词频向量 ==========
def to_vector(text):
    """统计每个词条出现的次数，得到一个 {词条: 次数} 的字典。"""
    return Counter(tokenize(text))


# ========== ④ 余弦相似度：手写，不调库 ==========
def cosine(v1, v2):
    """两个向量的夹角余弦。1 表示方向完全一致，0 表示无关。"""
    common = set(v1) & set(v2)
    dot = sum(v1[k] * v2[k] for k in common)

    norm1 = math.sqrt(sum(x * x for x in v1.values()))
    norm2 = math.sqrt(sum(x * x for x in v2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


# ========== ⑤ 检索：返回最相似的 k 条 ==========
def search(query, docs, k=2):
    q_vec = to_vector(query)

    scored = []
    for doc in docs:
        score = cosine(q_vec, to_vector(doc))
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:k]


# ========== ⑥ 试一下 ==========
if __name__ == "__main__":
    queries = [
        "报销要几天到账",          # 应该命中第 1 条
        "年假有几天",               # 应该命中第 2 条
        "出差住宿能报销多少",       # 应该命中第 4 条
        "费用核销要多久",           # ← 语义和第 1 条一样，但用词不同
    ]

    for q in queries:
        print(f"\n问题：{q}")
        for score, doc in search(q, DOCS, k=2):
            print(f"  {score:.3f}  {doc[:30]}...")