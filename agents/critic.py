from langchain_core.prompts import ChatPromptTemplate
from config import get_llm

class CriticAgent:
    def __init__(self):
        self.llm = get_llm(0.1)

    def review(self, execution: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are a strict critic agent. Validate logic, correctness, and completeness."),
            ("human", "{execution}")
        ])

        chain = prompt | self.llm
        return chain.invoke({"execution": execution}).content
