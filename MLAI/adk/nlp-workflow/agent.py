from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from tools.tool import Tools

MODEL = "deepseek/deepseek-chat"
base_tools = Tools()

jira_agent = LlmAgent(
    model=LiteLlm(model=MODEL),
    name="JIRA",
    instruction="You are the Jira Agent. Your ONLY task is to provide Jira info using 'get_jira_info' tool."
                "The tool will format the Jira info based on user preference stored in state. "
                "You should save your response to state and return to 'Master' agent every time.",
    description="Provides Jira info",
    tools=[base_tools.get_jira_ticket],
    output_key="agentJiraLast"
)

confluence_agent = LlmAgent(
    model=LiteLlm(model=MODEL),
    name="CONFLUENCE",
    instruction="You are the Confluence Agent. Your ONLY task is to provide Confluence info using 'get_confluence_info' tool."
                "The tool will format the Confluence info based on user preference stored in state. "
                "You should save your response to state and return to 'Master' agent every time.",
    description="Output Confluence info in markdown format",
    tools=[base_tools.get_confluence_info],
    output_key="agentConflLast"
)

security_agent = LlmAgent(
    model=LiteLlm(model=MODEL),
    name="SECURITY",
    instruction="You are the Security Agent. Your task is to provide the default warning info and log user request to the security log using 'security_logging' tool."
                "The tool will log user request to the security log. "
                "You should save your response to state and return to 'Master' agent every time.",
    description="Output Security info in markdown format",
    tools=[base_tools.security_logging]
)

requirements_agent = LlmAgent(
    model=LiteLlm(model=MODEL),
    name="REQUIREMENTS",
    instruction="You are the Requirements Agent. Your task is to provide the professional requirement based on user's request."
                "You can analysis user's intent and create query from user's message, then use the tool 'search_requirements' to search the requirements in internal knowledge base."
                "You should save your response to state and return to 'Master' agent every time.",
    description="Output Requirements in markdown format",
    tools=[base_tools.search_requirements],
    output_key="agentRequirementLast"
)

user_story_agent = LlmAgent(
    model=LiteLlm(model=MODEL),
    name="USER_STORY",
    instruction="You are the User Story Agent. Your task is to write professional UserStory based on requirements."
                "You can analysis requirements and create query from requirements, then use the tool 'search_user_story' to search history UserStory as reference."
                "You should save your response to state and return to 'Master' agent every time.",
    description="Output UserStory in markdown format",
    tools=[base_tools.output_user_story],
    output_key="agentUserStoryLast"
)

task_agent = LlmAgent(
    name="TASK_CONTROLLER", # New version name
    model=LiteLlm(model=MODEL) ,
    description="Get task list and delegates all tasks to sub agents.",
    instruction="Your job is to get task list from {task_list} , then make this task list more professional and more clear. Delegate each task to the appropriate sub agent."
                "you have specialized sub-agents: "
                "1. 'JIRA': Handles Jira requests when user need info from Jira."
                "2. 'CONFLUENCE': Handles Confluence requests when user need info from Confluence."
                "3. 'REQUIREMENTS': Handles Requirements requests when user need advice for Requirements."
                "4. 'USER_STORY': Handles User Story requests when user need to translate Requirements to User Story."
                "5. 'SECURITY': Handles illegal requests when user input any info not related to their work(No relevant agent was found)."
                "If the user's request is not related to any known sub agents, just delegate it to the security agent. And reply 'This question is illegal here!'",
    sub_agents=[jira_agent, confluence_agent, security_agent, requirements_agent, user_story_agent], # Include sub-agents
    output_key="task_result"
)

plan_agent = LlmAgent(
    name="PLANNER",
    model=LiteLlm(model=MODEL),
    description="The primary user assistant. Create plan and generator task list.",
    instruction="Get User request and split info into a task list",
    output_key="task_list"

)

pipline = SequentialAgent(
    name="workflow_pipline",
    sub_agents=[plan_agent, task_agent]
)

workflow_agent = LlmAgent(
    name="workflow_agent",
    model=LiteLlm(model=MODEL),
    description="The primary user assistant. It collaborates with the user to run a workflow.",
    instruction=f"""
You are a workflow assistant. your job is get user request and user this request info to start the workflow agent 'workflow_pipline' 
""",
    sub_agents=[pipline],
    output_key="response"
)

root_agent = workflow_agent

