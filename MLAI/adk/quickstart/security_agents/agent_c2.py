import asyncio
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# ==== Mock 工具函数 ====
def report_scan_result_c2(host: str, status: str, detail: str):
  print(f"[TOOL] report_scan_result_c2 被调用: host={host}, status={status}, detail={detail[:50]}...")
  return {"host": host, "status": status, "detail": detail}

# ==== 定义 Agent ====
root_agent = LlmAgent(
  name="security_agents",
  model=LiteLlm(model="deepseek/deepseek-chat"),
  description="Agent to answer questions about information security.",
  instruction="""
    你是一个安全分析助手。
    规则：
    1. 解析输入的 JSON。
    2. 如果其中包含任意 "Critical" 或 "High" 漏洞，status=fail。
    3. 如果没有 Critical/High，status=pass。
    4. 总结关键漏洞并给出修复建议输出为detail。
    5. 请调用工具 report_scan_result_c2，始终传递 host=host IP, status 和 detail。
    """,
  tools=[report_scan_result_c2],
)

# ==== 测试 JSON 输入 ====
scan_json = {
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

# ==== 封装一个调用函数 ====
async def agent_respond(agent, prompt: str) -> str:
  chunks = []
  async for ev in agent.run_async(prompt):   # 1.8.0 里可以直接传 str
    if hasattr(ev, "content") and ev.content:
      chunks.append(ev.content)
  return "".join(chunks)

# ==== 主入口 ====
async def main():
  prompt = f"请分析以下扫描结果 JSON：{scan_json}"
  summary = await agent_respond(root_agent, prompt)
  print("\n=== AI 总结 ===\n", summary)

if __name__ == "__main__":
  asyncio.run(main())


