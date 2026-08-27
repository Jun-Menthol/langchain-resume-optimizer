import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 定义带变量的提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一位{role}，请用{style}的语气回答问题。"),
    ("user", "{input}")
])

# 构建链
chain = prompt | llm

# 调用链
response = chain.invoke({
    "role": "简历优化顾问",
    "style": "专业且具体",
    "input": "如何让项目经验更有说服力？"
})

print(response.content)