# LangChain 简历优化助手

> 基于 LangChain 和 DeepSeek 的智能 Agent 工具集，已封装为可调用的 API 服务。

一个使用 LangChain 框架和 DeepSeek 大模型构建的 AI 工具集，包含简历优化助手、多功能 Agent 和 FastAPI 服务接口。

---

## 🎯 项目包含

| 文件 | 功能 | 状态 |
| :--- | :--- | :--- |
| `04_resume_optimizer.py` | 简历优化助手：分析简历并生成优化建议 | ✅ 完成 |
| `05_agent_with_search.py` | 带搜索功能的 Agent | ✅ 完成 |
| `06_agent_advanced.py` | 多功能 Agent：搜索 + 计算 + 时间 + 记忆 | ✅ 完成 |
| `app.py` | FastAPI 接口：将简历优化封装为可调用的 API 服务 | ✅ 完成 |

---

## 📚 学习进度与规划

### 已完成
- [x] 搭建 LangChain 开发环境
- [x] 实现简历优化助手核心流程（`04_resume_optimizer.py`）
- [x] 集成 DeepSeek API 实现 LLM 调用
- [x] 基于 LangGraph 构建带搜索功能的 Agent（`05_agent_with_search.py`）
- [x] 扩展多功能 Agent（搜索 + 计算 + 时间 + 记忆，`06_agent_advanced.py`）
- [x] 编写项目 README 文档
- [x] 用 FastAPI 封装简历优化接口，提供 Web 访问

### 进行中 / 计划中
- [ ] 对接本地 Ollama 模型，实现离线推理
- [ ] 优化提示词，提升简历优化建议的质量
- [ ] 添加前端界面，降低使用门槛

---

## 💡 学习收获

通过本项目，我掌握了：

- LangChain 基础用法（Chain、Prompt Template、Output Parser）
- LangGraph 构建 Agent 工作流的方法
- 大模型 API 的调用与异常处理
- 将 AI 能力组合成实际工具的开发思路
- FastAPI 封装 AI 服务为可调用 API 的工程化方法

---

## 🔄 最新进展（2026.08.31）

- ✅ 用 FastAPI 封装简历优化接口，提供 `/optimize` 端点和 Swagger 文档
- ✅ 在本地成功部署 Dify，作为 AI 应用开发平台
- ✅ 将本地 Ollama 模型（Qwen2.5:3b）接入 Dify
- ✅ 验证了从模型到应用的完整调用链路
- 下一步：搭建基于个人文档的 RAG 知识库

---

## 🛠️ 技术栈

| 工具 | 用途 |
| :--- | :--- |
| **Python 3.14** | 开发语言 |
| **LangChain** | AI 应用开发框架 |
| **LangGraph** | Agent 编排框架 |
| **FastAPI** | Web API 框架 |
| **DeepSeek API** | 大语言模型 |
| **Tavily API** | AI 搜索引擎 |

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Jun-Menthol/langchain-resume-optimizer.git
cd langchain-resume-optimizer
