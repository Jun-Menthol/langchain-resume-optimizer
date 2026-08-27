import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 创建记忆
memory = ConversationBufferMemory()

# 创建对话链
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print("第一轮对话：")
print(conversation.predict(input="我叫小张，正在学习AI开发"))

print("\n第二轮对话（测试记忆）：")
print(conversation.predict(input="我刚才说我叫什么名字？"))