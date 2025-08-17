from google.adk.tools.tool_context import ToolContext
from typing import Optional
from collections import defaultdict
import time
import random

class Tools:
    def __init__(self):
        self.history_cache = defaultdict(list)

    def get_jira_ticket(self, ticket: Optional[str], tool_context: ToolContext) -> str:
        """Retrieves markdown message from Jira system for demo test, directly return mock data."""
        print(ticket)

        # --- Read preference from state ---
        state = tool_context.state.get('Nodes')
        state['JIRA']['timestamp'] = time.time()
        state['JIRA']['message'] = "Waiting Agent Return..."
        state['JIRA']['status'] = 'running'
        tool_context.state['Nodes'] = state
        
        #time.sleep(random.randint(1,5))

        # Mock Data
        result = '''# Summary
Develop the workflow PoC based on ADK

## Description
This PoC is for a new workflow app with a multi-agent architecture by Google ADK. The following features will be implemented:

- **NLP Needs**: User can talk to the Host Agent about their needs within the flow.
- **Workflow Arrangement**: The Master Agent will collect Worker Agents from the library and confirm the sequence of jobs based on user needs.
- **Workflow Running**: Worker Agents will follow the Host Agent's order to complete their assigned jobs and then update the information to the Session State.
- **Show Workflow**: Develop a frontend to dynamically display the workflow state and the results of every agent.

## Task information
- **Status**: In Progress
- **Updated**: 2025-07-17T04:55:17.000+0000
- **Issue Type**: Task

## Relative Documentation
* https://confluence-url'''

        state['JIRA']['timestamp'] = time.time()
        state['JIRA']['message'] = result
        state['JIRA']['status'] = 'finished'
        tool_context.state['Nodes'] = state
        self.history_cache['JIRA'].append(
            {
                "date": time.time(),
                "content": result
            }
        )
        return result

    def get_confluence_info(self, ticket_url: Optional[str], tool_context: ToolContext) -> str: # MODIFIED SIGNATURE
        """Retrieves markdown message from Confluence system for demo test, directly return mock data."""
        print(ticket_url)
        state = tool_context.state.get('Nodes')
        state['CONFLUENCE']['timestamp'] = time.time()
        state['CONFLUENCE']['message'] = "Waiting Agent Return..."
        state['CONFLUENCE']['status'] = 'running'
        tool_context.state['Nodes'] = state

        result = '''[https://confluence-url](https://confluence-url)
Pilot will be progressing for the AI project with participation from all Value Streams and most Regions.
Recommended Team Composition:
* Business Analysts (BA): Responsible for gathering requirements, analyzing data, and supporting tool implementation.
* Project Managers (PM): Responsible for overseeing project delivery, timelines, and coordination.
* Project Management Office (PMO): Responsible for governance, reporting, and administrative support.'''

        #time.sleep(random.randint(1, 5))
        state['CONFLUENCE']['message'] = result

        # TODO: Confluence API call
        state['CONFLUENCE']['timestamp'] = time.time()
        state['CONFLUENCE']['status'] = 'finished'
        state['CONFLUENCE']['message'] = result
        tool_context.state['Nodes'] = state
        self.history_cache['CONFLUENCE'].append(
            {
                "date": time.time(),
                "content": result
            }
        )

        return result

    def security_logging(self, useless_info: Optional[str], tool_context: ToolContext) -> str:
        """Warning and log user if user's request is relevent from security perspective or not about work."""
        state = tool_context.state.get('Nodes')
        state['SECURITY']['status'] = 'running'
        tool_context.state['Nodes'] = state

        result = "This is not about our organization. And AI will not response for it. \nYour illegal message: " + useless_info
        state['SECURITY']['timestamp'] = time.time()
        state['SECURITY']['message'] = result
        state['SECURITY']['status'] = 'finished'
        tool_context.state['Nodes'] = state

        self.history_cache['SECURITY'].append(
            {
                "date": time.time(),
                "content": result
            }
        )

        return result
    
    def search_requirements(self, query: Optional[str], tool_context: ToolContext) -> str:
        """Search requirements in internal knowledge base based on query."""
        state = tool_context.state.get('Nodes')
        state['REQUIREMENTS']['status'] = 'running'
        state['REQUIREMENTS']['timestamp'] = time.time()
        state['REQUIREMENTS']['message'] = "Waiting Agent Return..."
        tool_context.state['Nodes'] = state

        # TODO: Search requirements in internal knowledge base
        result = '''Here’s a concise **Requirements Document** based on your provided Jira task description:

---

**# AI Application – Requirements Document**

**1. Overview**
Develop a Proof of Concept (PoC) for an AI-driven muti-agent application utilizing **. The system should enable natural language interaction, dynamic task orchestration, agent collaboration, and real-time visualization of workflow execution.

---

**2. Core Features**

### 2.1 Natural Language Processing (NLP) Interface

* Users can **describe workflow needs** via conversation with the **Host Agent**.
* The system must parse and interpret these inputs into actionable intents.

### 2.2 Workflow Composition

* A **Master Agent** orchestrates task planning:

  * Selects **Worker Agents** from an existing agent library.
  * Arranges them in a **logical sequence** based on the user’s needs.

### 2.3 Workflow Execution

* **Worker Agents** execute assigned tasks in order.
* Each agent:

  * Receives instructions from the Host Agent.
  * Executes its task autonomously.
  * Reports results and updates to the **Session State**.

### 2.4 Frontend Visualization

* A web-based UI will:

  * **Dynamically visualize** workflow state and progress.
  * Display results and status for each agent involved.
  * Refresh in real-time as the workflow progresses.

---

**3. Technical Requirements**

* **Backend**:

  * Based on **Google ADK** for agent definition and orchestration.
  * Session management for maintaining workflow context.

* **Frontend**:

  * Dynamic rendering of **workflow DAG or sequence view**.
  * Real-time updates from backend using WebSocket or polling.

* **Data**:

  * Session State must persist user intent, task status, agent responses.

---

**4. Status & Next Steps**

* **Current Status**: In Progress
* **Tasks**:

  * Define Host, Master, and Worker Agent behaviors.
  * Build ADK-based backend logic.
  * Design and implement dynamic frontend.
  * Integrate session state management.

---

Let me know if you'd like a breakdown into user stories or an architecture sketch next.
'''

        #time.sleep(random.randint(1, 5))

        state['REQUIREMENTS']['timestamp'] = time.time()
        state['REQUIREMENTS']['message'] = result
        state['REQUIREMENTS']['status'] = 'finished'
        tool_context.state['Nodes'] = state

        self.history_cache['REQUIREMENTS'].append(
            {
                "date": time.time(),
                "content": result
            }
        )
        return result
    
    def output_user_story(self, tool_context: ToolContext) -> str:
        """Return a fixed user story for PoC."""
        state = tool_context.state.get('Nodes')
        state['USER STORY']['status'] = 'running'
        state['USER STORY']['timestamp'] = time.time()
        state['USER STORY']['message'] = "Waiting Agent Return..."
        tool_context.state['Nodes'] = state

        # TODO: Search user story in internal knowledge base
        #time.sleep(random.randint(1, 5))
        result = '''Here is a **User Story** tailored for an IT developer, based on your AI Workflow App using Google ADK:

---

### **User Story: AI-Driven Workflow Orchestration with Multi-Agent System**

**Title:**
As a user, I want to describe my workflow needs in natural language and have an AI system organize, execute, and display the workflow using agents, so that I can automate multi-step processes without coding.

---

**Background:**
This PoC leverages **Google ADK** to build a **multi-agent architecture**, enabling dynamic workflow creation and execution based on user intent. The system involves a **Host Agent**, **Master Agent**, and multiple **Worker Agents** that communicate and collaborate to fulfill the user's goal.

---

### **Acceptance Criteria:**

1. **NLP Interaction:**

   * [ ] The system provides a chat interface where the user can express their workflow needs in natural language.
   * [ ] The **Host Agent** interprets user input and extracts actionable tasks or goals.

2. **Workflow Composition:**

   * [ ] The **Master Agent** selects relevant **Worker Agents** from a predefined library.
   * [ ] The **Master Agent** arranges Worker Agents into a sequence (or DAG) based on task dependencies and user goals.

3. **Workflow Execution:**

   * [ ] The **Host Agent** initiates workflow execution.
   * [ ] Each **Worker Agent** receives tasks, performs them, and updates the shared **Session State** with results.
   * [ ] Agents must operate independently but maintain a synchronized state via a session context.

4. **Frontend Visualization:**

   * [ ] A web interface displays the current workflow, showing:

     * Agent names and roles
     * Current task status (pending, running, completed)
     * Results or outputs from each Worker Agent
   * [ ] The UI updates in real time as the workflow progresses.

---

**Dependencies & Tech Stack:**

* **Agent Framework**: Google ADK
* **Frontend**: React or similar SPA framework (TBD)
* **Backend**: Python/Node (depending on ADK integration needs)
* **Real-time Updates**: WebSocket or polling mechanism
* **Data Store**: In-memory for PoC, expandable to Redis/Postgres

---

**Notes for Developers:**

* Keep agents modular and stateless where possible.
* Design with extensibility: users may eventually define custom Worker Agents or new types of workflows.
* Use mock Worker Agents for initial testing (e.g., math operations, data fetchers).
* Prioritize traceability—users should be able to trace how their input leads to specific agent actions.

---

Let me know if you'd like the **epic breakdown**, **technical tasks**, or **architecture diagram** next.
'''

        state['USER STORY']['timestamp'] = time.time()
        state['USER STORY']['message'] = result
        state['USER STORY']['status'] = 'finished'
        tool_context.state['Nodes'] = state

        self.history_cache['USER STORY'].append(
            {
                "date": time.time(),
                "content": result
            }
        )
        return result