# tools.py
import requests

def report_scan_result(host: str, status: str, details: dict = None):
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

