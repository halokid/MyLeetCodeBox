from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from process import AgentRunner
from agent import jira_agent, confluence_agent, security_agent, requirements_agent, user_story_agent, root_agent, base_tools
from tools.tool import Tools
from pydantic import BaseModel
import inspect
import asyncio
import uvicorn
import json

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_state = {
    'WorkflowState': 'Init',
    'Nodes': {
        'JIRA': {},
        'CONFLUENCE': {},
        'SECURITY': {},
        'REQUIREMENTS': {},
        'USER STORY': {}
    },
    'Response': []
}

runner = AgentRunner(init_state)
asyncio.run(runner.init_session(init_state))

user_input = [
    "Hi!",
    "What's the markdown info from Jira?",
    "What's the weather today?"
]

class Query(BaseModel):
    message: str

@app.get("/health")
async def health_check():
    """基本的系统健康检查接口"""
    return {"status": "healthy", "message": "System is running"}

@app.get("/agents")
async def get_agents():
    """返回所有agent的详细信息"""
    agents = [
        {
            "name": jira_agent.name,
            "description": jira_agent.description,
            "instruction": jira_agent.instruction,
            "output_key": jira_agent.output_key
        },
        {
            "name": confluence_agent.name,
            "description": confluence_agent.description,
            "instruction": confluence_agent.instruction,
            "output_key": confluence_agent.output_key
        },
        {
            "name": security_agent.name,
            "description": security_agent.description,
            "instruction": security_agent.instruction,
            "output_key": security_agent.output_key
        },
        {
            "name": requirements_agent.name,
            "description": requirements_agent.description,
            "instruction": requirements_agent.instruction,
            "output_key": requirements_agent.output_key
        },
        {
            "name": user_story_agent.name,
            "description": user_story_agent.description,
            "instruction": user_story_agent.instruction,
            "output_key": user_story_agent.output_key
        },
        {
            "name": root_agent.name,
            "description": root_agent.description,
            "instruction": root_agent.instruction,
            "output_key": root_agent.output_key
        }
    ]
    return {"agents": agents}

@app.get("/state")
async def get_state():
    """返回runner.stored_session.state中的信息"""
    if hasattr(runner, 'stored_session') and runner.stored_session:
        return runner.stored_session.state
    else:
        return {"error": "Session not initialized"}

@app.get("/tools")
async def get_tools():
    """返回tools.py中Tools类下面所有的工具函数信息"""
    tools_instance = Tools()
    tools_info = []
    
    # 获取Tools类的所有方法
    methods = inspect.getmembers(tools_instance, predicate=inspect.ismethod)
    
    for method_name, method_obj in methods:
        # 跳过内置方法和私有方法
        if not method_name.startswith('_'):
            doc = method_obj.__doc__ or "No description available"
            tools_info.append({
                "name": method_name,
                "description": doc.strip()
            })
    
    return {"tools": tools_info}

@app.post("/chat")
async def chat(query: Query):
    ai_response = await runner.run_stateful_conversation(query.message)
    with open('history.json', 'w') as f:
        json.dump(base_tools.history_cache, f, indent=4)
    return {"message": ai_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

