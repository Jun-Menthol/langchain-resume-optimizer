import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

load_dotenv()

# 1. 初始化大模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 2. 初始化搜索工具
search_tool = TavilySearchResults(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=3
)

tools = [search_tool]

# 3. 使用 langgraph 创建 Agent
agent = create_react_agent(llm, tools)

# 4. 运行 Agent
if __name__ == "__main__":
    query = input("请输入你想查询的内容：")
    result = agent.invoke({"messages": [("user", query)]})
    
    print("\n" + "="*60)
    print("📊 结果：")
    print("="*60)
    last_message = result["messages"][-1]
    print(last_message.content)