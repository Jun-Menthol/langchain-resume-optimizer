import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

# 加载 .env 文件中的环境变量
load_dotenv()

# 初始化 DeepSeek 模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 调用模型
response = llm.invoke("请用一句话介绍你自己")
print(response.content)