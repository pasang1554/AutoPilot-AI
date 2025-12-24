from langchain_core.prompts import ChatPromptTemplate
from config import get_llm

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm(0.1)

    def plan(self, goal: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are a planning agent.

Return STRICT JSON only.
Do NOT explain.

FORMAT:
{{
  "steps": [
    "step 1",
    "step 2",
    "step 3"
  ]
}}
"""
            ),
            ("human", "{goal}")
        ])

        chain = prompt | self.llm
        response = chain.invoke({"goal": goal}).content
        return response
