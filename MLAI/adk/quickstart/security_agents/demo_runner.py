# demo_runner.py
import asyncio
from typing import Dict

# ✅ 推荐用这些路径导入，1.8.0 版本通用
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types  # 提供 Content/Part

# === 你的工具（最小可跑 mock） ===
def report_scan_result_c2(host: str, status: str, detail: str) -> Dict:
  """
  将扫描结果上报到你的 C2 或回调逻辑。
  这里只做打印，方便你看到工具被调用。
  """
  print(f"[TOOL] report_scan_result_c2 called: host={host}, status={status}, detail={detail[:60]}...")
  return {"ok": True, "host": host, "status": status}

# === 定义 Agent ===
root_agent = LlmAgent(
  name="security_agents",
  model=LiteLlm(model="deepseek/deepseek-chat"),  # 通过 LiteLLM 调 DeepSeek
  description="Agent to answer questions about information security.",
  instruction="""
    你是一个安全分析助手。
    规则：
    1. 解析输入的 JSON（字段 hosts[].ip 与 hosts[].vulnerabilities[].severity）。
    2. 如果其中包含任意 "Critical" 或 "High" 漏洞，status=fail。
    3. 如果没有 Critical/High，status=pass。
    4. 总结关键漏洞并给出修复建议作为 detail。
    5. 请调用工具 report_scan_result_c2，始终传递 host=主机IP, status 和 detail。
    """,
  tools=[report_scan_result_c2],  # 直接传入函数，ADK 会自动生成 tool schema
)

# === 两份测试数据：fail / pass ===
SCAN_FAIL = {
  "hosts": [
    {
      "ip": "192.168.1.10",
      "vulnerabilities": [
        {"id": "VULN-001", "name": "OpenSSH 旧版本", "severity": "High"},
        {"id": "VULN-002", "name": "未授权访问风险", "severity": "Critical"},
      ]
    }
  ]
}

SCAN_PASS = {
  "hosts": [
    {
      "ip": "192.168.1.20",
      "vulnerabilities": [
        {"id": "VULN-010", "name": "TLS 配置可优化", "severity": "Medium"},
        {"id": "VULN-011", "name": "信息泄露风险较低", "severity": "Low"},
      ]
    }
  ]
}

async def run_once(runner: Runner, user_id: str, session_id: str, query_text: str) -> str:
  """
  用 Runner.run_async 发起一次对话，聚合最终回答文本。
  """
  content = genai_types.Content(role="user", parts=[genai_types.Part(text=query_text)])

  final_text = ""
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
    # 你也可以在这里观察工具调用事件、token 流等
    if getattr(event, "is_final_response", lambda: False)():
      # 取最终自然语言回答
      if event.content and getattr(event.content, "parts", None):
        part0 = event.content.parts[0]
        # 兼容 text / from_text
        text = getattr(part0, "text", None)
        if text:
          final_text = text
  return final_text

async def main():
  APP = "sec-app"
  USER = "u1"

  # 1) 建内存会话服务 + 创建会话
  session_service = InMemorySessionService()
  # 注意 1.8.0 的会话 API 是异步的
  await session_service.create_session(app_name=APP, user_id=USER, session_id="s-fail")
  await session_service.create_session(app_name=APP, user_id=USER, session_id="s-pass")

  # 2) 创建 Runner（不需要 api_server）
  runner = Runner(agent=root_agent, app_name=APP, session_service=session_service)

  # 3) 运行一次：FAIL 场景
  prompt_fail = f"请分析以下扫描结果 JSON：{SCAN_FAIL}"
  print("\n=== RUN FAIL CASE ===")
  final_fail = await run_once(runner, USER, "s-fail", prompt_fail)
  print("\n[FINAL FAIL RESPONSE]\n", final_fail)

  # 4) 运行一次：PASS 场景
  prompt_pass = f"请分析以下扫描结果 JSON：{SCAN_PASS}"
  print("\n=== RUN PASS CASE ===")
  final_pass = await run_once(runner, USER, "s-pass", prompt_pass)
  print("\n[FINAL PASS RESPONSE]\n", final_pass)

if __name__ == "__main__":
  asyncio.run(main())


