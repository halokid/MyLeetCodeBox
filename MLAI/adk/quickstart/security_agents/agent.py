# import datetime
# from zoneinfo import ZoneInfo
# from google.adk.agents import Agent
# from google.adk.agents import LlmAgent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

import json
import requests
import asyncio

# ------------------- tools start -------------------------
def analysis_scan_report(report: str) -> dict:
  print("report -->>>", report)

  return {
    "code": 0,
    "message": "",
    "data": report
  }

def report_scan_result_c1(host: str, status: str, details: dict = None):
  """
  host: 主机 IP
  status: pass/fail
  details: 扫描分析的详细结果（可选）
  """
  # 例子：调用你自己的API
  url = "http://your-api-server.local/scan_result"
  payload = {
    "host": host,
    "status": status,
    "details": details or {}
  }
  resp = requests.post(url, json=payload)
  return {"api_status": resp.status_code, "response": resp.text}

def report_scan_result_c2(host: str, status: str, details: str):
  payload = {
    "host": host,
    "status": status,
    "details": details,
  }
  print("payload -->>>", payload)


# ------------------- tools end -------------------------

root_agent = LlmAgent(
  name="security_agents",
  model=LiteLlm(model="deepseek/deepseek-chat"),
  description=(
    "Agent to answer questions about information security."
  ),
  instruction=(
    """
    你是一个安全分析助手。
    规则：
    1. 解析输入的 JSON。
    2. 如果其中包含任意 "Critical" 或 "High" 漏洞，status=fail。
    3. 如果没有 Critical/High，status=pass。
    4. 总结关键漏洞并给出修复建议输出为detail, 调用工具 detail=detail
    5. 请调用工具 report_scan_result, 始终传递 host=host IP, status 和 detail。
    """
  ),
  tools=[report_scan_result_c2],
)

def load_json_from_file(file_path: str) -> dict:
  """
  从指定文件中读取 JSON 数据并返回 Python 字典。

  :param file_path: JSON 文件路径
  :return: dict 对象
  """
  with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
  return data

def gen_summary(agent, prompt: str) -> str:
  async def _go():
    res = await agent.run_async(prompt)
    return getattr(res, "content", None) or getattr(res, "text", None) or str(res)
  return asyncio.run(_go())

if __name__ == "__main__":
  # sample_json = "read from sampe_scan.sjon"
  sample_json = load_json_from_file("./resource/sample_scan.json")
  prompt = f"""
    主机的扫描报告是 { sample_json }
    请帮我生成报告：
    主机 host 的扫描结果是 status。
    Critical 数量：critical_count，High 数量：high_count。
    请总结关键漏洞并给出修复建议。
    """
  # summary_result = await root_agent.run_async(prompt)
  # 兼容不同返回对象取文本：
  # summary = getattr(summary_result, "content", None) or getattr(summary_result, "text", None) or str(summary_result)
  # print(summary)

  summary = gen_summary(root_agent, prompt)
  print(summary)


