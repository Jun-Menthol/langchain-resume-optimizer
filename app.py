import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --------------------------------------
# 1. 加载环境变量 & 初始化模型
# --------------------------------------
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("未找到 DEEPSEEK_API_KEY，请检查 .env 文件")

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.3,
    api_key=api_key
)

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

# --------------------------------------
# 2. 创建 FastAPI 应用
# --------------------------------------
app = FastAPI(title="简历优化助手API")

# 定义请求体结构
class ResumeRequest(BaseModel):
    resume_text: str

# 定义响应体结构
class ResumeResponse(BaseModel):
    optimized_text: str
    status: str

# --------------------------------------
# 3. 创建 API 端点
# --------------------------------------
@app.get("/")
def read_root():
    return {"message": "简历优化助手API已启动"}

@app.post("/optimize", response_model=ResumeResponse)
async def optimize_resume(request: ResumeRequest):
    try:
        # 调用优化链，并传入请求中的简历文本
        response = chain.invoke({"resume_text": request.resume_text})
        return ResumeResponse(
            optimized_text=response.content,
            status="success"
        )
    except Exception as e:
        # 如果出错，返回 500 错误
        raise HTTPException(status_code=500, detail=str(e))