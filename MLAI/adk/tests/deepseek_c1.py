import os
import asyncio
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import InMemoryRunner
from google.genai import types

# 设置 DeepSeek API Key
# os.environ["DEEPSEEK_API_KEY"] = "你的 DEEPSEEK_API_KEY"

# 初始化 LLM：DeepSeek 模型
llm = LiteLlm(
  model="deepseek/deepseek-chat",  # DeepSeek Chat 模型名称
  api_key=os.environ["DEEPSEEK_API_KEY"]
)

# 创建 Agent
agent = LlmAgent(
  name="deepseek_agent",
  model=llm,
  instruction="你是一个知识丰富的助手，简洁回答用户提问。",
  description="ADK + DeepSeek Chat 测试",
  tools=[]  # 无外部工具时可以留空
)

# 创建 session service 与 runner
session_service = InMemorySessionService()
# runner = InMemoryRunner(agent=agent, session_service=session_service, app_name="test_app")
#
runner = InMemoryRunner(agent=agent, app_name="test_app")


# 异步运行测试
async def run_agent():
  # 初始化 session
  user_id = "user1"
  # session_id = "sess1"
  session_service.create_session(app_name="test_app", user_id=user_id)

  content = types.Content(role="user", parts=[types.Part(text="你好，请介绍 AI agent。")])

  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
    if event.is_final_response():
      print("Agent 回答：", event.content.parts[0].text.strip())

if __name__ == "__main__":
  asyncio.run(run_agent())
