import requests

params = {"query": "Hi!\nWhat's the markdown info from Jira?\nWhat's the weather today?"}
url = "http://127.0.0.1:8000/chat"

resp = requests.post(url, params=params)
print(resp.json())