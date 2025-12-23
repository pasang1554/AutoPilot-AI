from langchain_core.prompts import ChatPromptTemplate
from config import get_llm

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm(0.1)

    def plan(self, goal: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a senior planner agent. Break the goal into clear numbered steps."),
            ("human", "{goal}")
        ])
        chain = prompt | self.llm
        return chain.invoke({"goal": goal}).content
