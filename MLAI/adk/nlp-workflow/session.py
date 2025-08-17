from google.adk.sessions import InMemorySessionService

class SessionController:
    def __init__(self):
        self.session_service_stateful = InMemorySessionService()

    async def create_session(self, app_name, user_id, session_id, init_state):
        self.session_stateful = await self.session_service_stateful.create_session(
            app_name = app_name,
            user_id = user_id,
            session_id = session_id,
            state = init_state
        )

    async def get_session(self, app_name, user_id, session_id):
        session_state = await self.session_service_stateful.get_session(
            app_name = app_name,
            user_id = user_id,
            session_id = session_id
        )
        return session_state