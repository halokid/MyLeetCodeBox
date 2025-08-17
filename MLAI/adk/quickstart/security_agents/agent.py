import datetime
from zoneinfo import ZoneInfo
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


'''
def get_current_time(city: str) -> dict:
  if city.lower() == "new york":
    tz_identifier = "America/New_York"
  else:
    return {
      "status": "error",
      "error_message": (
        f"Sorry, I don't have timezone information for {city}."
      ),
    }

  tz = ZoneInfo(tz_identifier)
  now = datetime.datetime.now(tz)
  report = (
    f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
  )
  return {"status": "success", "report": report}
'''

'''
root_agent = Agent(
  name="weather_time_agent",
  # model="gemini-2.0-flash",
  # model="deepseek/deepseek-chat",
  model="deepseek-chat",
  description=(
    "Agent to answer questions about the time and weather in a city."
  ),
  instruction=(
    "You are a helpful agent who can answer user questions about the time and weather in a city."
  ),
  tools=[get_weather, get_current_time],
)
'''

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


