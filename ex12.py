# ex12.py —— 第一次调用大模型 API
#
# 前置条件：
#   1. 同目录下有 .env，里面有一行 DEEPSEEK_API_KEY=sk-xxx
#   2. 已安装 openai 和 python-dotenv
#
# 运行方式（必须在 w1 目录下，否则读不到 .env）：
#   cd D:\deepseek\bootcamp\w1
#   python ex12.py

import os

from dotenv import load_dotenv
from openai import OpenAI

# ① 读取 .env，把里面的 KEY=VALUE 变成环境变量
load_dotenv()

# ② 创建客户端
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# ③ 发请求
resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "用三句话解释什么是 RAG"}
    ],
)

# ④ 取回答
print("=== 模型回答 ===")
print(resp.choices[0].message.content)

# ⑤ 看看这次调用花了多少 token
print()
print("=== 用量 ===")
print(f"输入 token: {resp.usage.prompt_tokens}")
print(f"输出 token: {resp.usage.completion_tokens}")
print(f"合计:       {resp.usage.total_tokens}")
