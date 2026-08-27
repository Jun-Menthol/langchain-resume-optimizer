import os
import sys
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate

# ============================================================
# 步骤 1：加载环境变量
# ============================================================
print("正在加载环境变量...")
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("❌ 错误：未找到 DEEPSEEK_API_KEY，请检查 .env 文件。")
    sys.exit(1)
else:
    print(f"✅ API Key 已加载（前8位：{api_key[:8]}...）")

# ============================================================
# 步骤 2：初始化模型
# ============================================================
print("正在初始化 DeepSeek 模型...")
try:
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.3,
        api_key=api_key
    )
    print("✅ 模型初始化成功")
except Exception as e:
    print(f"❌ 模型初始化失败：{e}")
    sys.exit(1)

# ============================================================
# 步骤 3：创建提示词模板
# ============================================================
print("正在创建提示词模板...")
prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一位资深HR和职业规划师，擅长从招聘者的视角优化简历。
    请分析用户提供的简历，并从以下方面给出具体、可量化的优化建议：
    1. 整体评价
    2. 核心优化建议（至少3条，每条包含问题定位、优化方案、量化指标）
    3. 需要补充的关键信息
    4. 格式与排版建议"""),
    ("user", "请分析这份简历：\n{resume_text}")
])

chain = prompt | llm

# ============================================================
# 步骤 4：准备示例简历
# ============================================================
sample_resume = """
姓名：张三
教育背景：大专，软件技术专业
项目经验：开发过学生管理系统
技能：熟悉Java
"""

print("\n" + "="*60)
print("📄 输入的简历：")
print("="*60)
print(sample_resume)
print("="*60)

# ============================================================
# 步骤 5：调用模型生成优化建议
# ============================================================
print("\n🤖 正在生成优化建议，请稍候...\n")

try:
    response = chain.invoke({"resume_text": sample_resume})
    print("="*60)
    print("📊 优化建议：")
    print("="*60)
    print(response.content)
    print("="*60)
    print("✅ 运行完成！")
except Exception as e:
    print(f"❌ 调用模型时出错：{e}")
    sys.exit(1)