# ex13.py —— hello-llm：命令行问答工具
#
# 用法：
#   python ex13.py "你的问题"
#
# 注意：必须在 w1 目录下运行，否则读不到 .env

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)


DEFAULT_SYSTEM = "你是一个简洁的技术助理。回答控制在三句话以内，不要展开成文章。"

def ask(question, system=DEFAULT_SYSTEM):
    """问一个问题，返回模型回答和用量"""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": question},
    ]

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )
    return resp.choices[0].message.content, resp.usage


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('用法: python ex13.py "你的问题"')
        print('例如: python ex13.py "什么是向量数据库"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    answer, usage = ask(question)

    print(answer)
    print()
    print(f"[tokens] 输入 {usage.prompt_tokens} / 输出 {usage.completion_tokens}")