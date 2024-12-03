from openai import OpenAI
import os

os.environ["http_proxy"] = "socks5://10.176.24.76:10802"
os.environ["https_proxy"] = "socks5://10.176.24.76:10802"


def test_openai_api_key(api_key):
    """
    测试 OpenAI API 密钥是否可用
    :param api_key: str, 要测试的 OpenAI API 密钥
    :return: bool, True 表示可用，False 表示不可用
    """
    try:
        # 设置 API 密钥
        # openai.api_key = api_key
        client = OpenAI(api_key=api_key)

        # 尝试一个简单的 API 请求
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"},
            ],
        )

        # 检查返回结果=
        print("API Key is valid. Response:")
        print(response.choices[0].message)
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# 替换为你的 OpenAI API 密钥
OPENAI_API_KEY = ""

# 测试密钥
if test_openai_api_key(OPENAI_API_KEY):
    print("The OpenAI API key is valid!")
else:
    print("The OpenAI API key is invalid or an error occurred.")
