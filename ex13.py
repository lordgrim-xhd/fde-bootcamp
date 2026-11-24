import os
import sys
import time

from dotenv import load_dotenv
from openai import (
    APIStatusError,
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
    timeout=30,          # 单次请求最多等 30 秒
    max_retries=0,       # 关掉 SDK 自带的重试，我们自己控制
)

DEFAULT_SYSTEM = "你是一个简洁的技术助理。回答控制在三句话以内，不要展开成文章。"


def ask(question, system=DEFAULT_SYSTEM, max_attempts=3):
    """问一个问题。成功返回 (回答, 用量)，失败返回 (None, None)。"""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": question},
    ]

    for attempt in range(1, max_attempts + 1):
        try:
            resp = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
            )
            return resp.choices[0].message.content, resp.usage

        except AuthenticationError:
            print("❌ API Key 无效或已过期，请检查 .env")
            return None, None

        except RateLimitError:
            wait = 2 ** attempt
            print(f"⚠️ 请求太频繁，{wait} 秒后重试（第 {attempt}/{max_attempts} 次）")
            time.sleep(wait)

        except (APIConnectionError, APITimeoutError):
            wait = 2 ** attempt
            print(f"⚠️ 网络问题，{wait} 秒后重试（第 {attempt}/{max_attempts} 次）")
            time.sleep(wait)

        except APIStatusError as e:
            if e.status_code >= 500:
                wait = 2 ** attempt
                print(f"⚠️ 服务端错误 {e.status_code}，{wait} 秒后重试")
                time.sleep(wait)
            else:
                print(f"❌ 请求被拒绝（{e.status_code}）：{e.message}")
                return None, None

    print(f"❌ 重试 {max_attempts} 次都失败，放弃")
    return None, None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('用法: python ex13.py "你的问题"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    answer, usage = ask(question)

    if answer is None:
        sys.exit(1)        # 失败退出码 1，方便脚本判断

    print(answer)
    print()
    print(f"[tokens] 输入 {usage.prompt_tokens} / 输出 {usage.completion_tokens}")