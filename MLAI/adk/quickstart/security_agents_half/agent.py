# import datetime
# from zoneinfo import ZoneInfo
# from google.adk.agents import Agent
# from google.adk.agents import LlmAgent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

def analysis_scan_report(report: str) -> dict:
  print("report -->>>", report)

  return {
    "code": 0,
    "message": "",
    "data": report
  }

root_agent = LlmAgent(
  name="security_agents",
  model=LiteLlm(model="deepseek/deepseek-chat"),
  description=(
    "Agent to answer questions about information security."
  ),
  instruction=(
    "You are a helpful agent who can answer user questions about anything of information security."
  ),
  tools=[analysis_scan_report],
)

if __name__ == "__main__":
  summary = root_agent.chat(
    f"""
    请帮我生成报告：
    主机 {host} 的扫描结果是 {status}。
    Critical 数量：{critical_count}，High 数量：{high_count}。
    请总结关键漏洞并给出修复建议。
    """
  )
  print(summary)


