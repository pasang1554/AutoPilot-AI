from langchain_core.prompts import ChatPromptTemplate
from config import get_llm
from tools.tool_runner import run_tool


class ExecutorAgent:
    def __init__(self, memory):
        self.llm = get_llm(0.1)
        self.memory = memory

    def execute(self, plan_json: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are an execution agent.

STRICT RULES:
- DO NOT invent tools
- ONLY use these tools if ABSOLUTELY required:
  - calculator
  - file_writer
  - task_logger
- If no tool is required, DO NOT use any tool
- Never use echo, curl, shell, or web commands

Return STRICT JSON only.

FORMAT:
{{
  "execution": "...",
  "result": "..."
}}
"""
            ),
            (
                "human",
                "{plan}"
            )
        ])

        chain = prompt | self.llm
        response = chain.invoke({"plan": plan_json}).content

        # Tool execution (ONLY if explicitly requested)
        if "TOOL:" in response:
            tool_line = response.split("TOOL:")[1].strip()
            parts = tool_line.split("|")
            tool_name = parts[0]
            args = parts[1:]
            tool_result = run_tool(tool_name, args)
            response += f"\n\nTOOL_RESULT: {tool_result}"

        self.memory.add("executor", response)
        return response
