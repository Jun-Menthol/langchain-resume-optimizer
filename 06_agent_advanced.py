import os
import math
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool

load_dotenv()

# ============================================================
# 1. 初始化大模型
# ============================================================
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# ============================================================
# 2. 定义工具
# ============================================================

# 2.1 搜索工具
search_tool = TavilySearchResults(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=3
)

# 2.2 计算器工具
@tool
def calculator(expression: str) -> str:
    """
    计算数学表达式的结果。
    输入：一个数学表达式，如 "2 + 3 * 4" 或 "sqrt(16)"。
    返回：计算结果。
    """
    try:
        # 安全计算，只允许基本数学运算
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("_")
        }
        allowed_names.update({"abs": abs, "round": round})
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"计算结果：{result}"
    except Exception as e:
        return f"计算错误：{e}"

# 2.3 获取当前时间工具
@tool
def get_current_time() -> str:
    """获取当前的日期和时间。"""
    from datetime import datetime
    now = datetime.now()
    return f"当前时间：{now.strftime('%Y年%m月%d日 %H:%M:%S')}"

# 2.4 获取用户信息（模拟记忆）
@tool
def get_user_info(key: str) -> str:
    """
    获取已存储的用户信息。
    输入：信息名称，如 "name"。
    返回：对应的信息值。
    """
    # 这里可以扩展为从数据库或文件中读取
    user_data = {
        "name": "用户",
        "learning_goal": "AI开发"
    }
    return user_data.get(key, f"未找到 '{key}' 的相关信息")

# 收集所有工具
tools = [search_tool, calculator, get_current_time, get_user_info]

# ============================================================
# 3. 创建带记忆的 Agent
# ============================================================

# 创建记忆存储（用于多轮对话）
memory = MemorySaver()

# 创建 Agent
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory  # 启用对话记忆
)

# ============================================================
# 4. 运行 Agent（支持多轮对话）
# ============================================================

print("="*60)
print("🤖 智能助手已启动（按 Ctrl+C 退出）")
print("="*60)
print("我可以帮你：")
print("  🔍 搜索实时信息（如天气、新闻）")
print("  🧮 计算数学表达式（如 2+3*4）")
print("  ⏰ 获取当前时间")
print("  💬 记住你在对话中的信息")
print("="*60)

# 对话线程 ID（用于区分不同会话）
thread_id = "user_session_001"

while True:
    try:
        query = input("\n👤 你：")
        if query.lower() in ["exit", "quit", "退出"]:
            print("👋 再见！")
            break
        
        # 调用 Agent
        result = agent.invoke(
            {"messages": [("user", query)]},
            config={"configurable": {"thread_id": thread_id}}
        )
        
        # 输出最终回答
        last_message = result["messages"][-1]
        print(f"\n🤖 助手：{last_message.content}")
        
    except KeyboardInterrupt:
        print("\n👋 再见！")
        break
    except Exception as e:
        print(f"\n❌ 出错了：{e}")
        print("请再试一次。")