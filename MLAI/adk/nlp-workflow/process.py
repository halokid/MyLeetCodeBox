from google.genai import types
from agent import root_agent
from session import SessionController
from google.adk.memory import InMemoryMemoryService
from google.adk.runners import Runner
import json
import time

APP_NAME = "WORKFLOW_APP"
USER_ID = "USER001"
SESSION_ID = "SESSION001"

class AgentRunner:
    def __init__(self, init_state):
        self.init_session(init_state)
        self.memory_service = InMemoryMemoryService()

    async def call_agent_async(self, query: str, runner, user_id, session_id):
        content = types.Content(role='user', parts=[types.Part(text=query)])
        final_response = "Agent Response:\n"
        async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
            if event.is_final_response():
                final_response = event.content.parts[0].text
                self.stored_session.state['Response'].append(final_response)
        return final_response

    async def init_session(self, init_state):
        # Session Init
        session_controller = SessionController()
        await session_controller.create_session(APP_NAME, USER_ID, SESSION_ID, init_state)
        self.stored_session = session_controller.session_service_stateful.sessions[APP_NAME][USER_ID][SESSION_ID]

        # Runner Init
        self.runner_root_stateful = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=session_controller.session_service_stateful,
            memory_service=self.memory_service
        )

    async def call_agent_seq(self, query: str):
        return await self.call_agent_async(
            query= query,
            runner=self.runner_root_stateful,
            user_id=USER_ID,
            session_id=SESSION_ID
        )

    async def run_stateful_conversation(self, query: str):
        self.stored_session.state['WorkflowState'] = 'Init'
        time.sleep(3)
        self.stored_session.state['WorkflowState'] = 'Running'
        ai_response = await self.call_agent_seq(query)
        self.stored_session.state['WorkflowState'] = 'Finished'
        with open("data/result.json", "w") as f:
            json.dump(self.stored_session.state, f, indent=4)
        #print(f"State: {self.stored_session.state}")
        return ai_response