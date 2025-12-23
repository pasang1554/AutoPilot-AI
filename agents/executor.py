from langchain_core.prompts import ChatPromptTemplate
from config import get_llm
from tools.calculator import calculate
from tools.file_writer import write_file
from tools.task_logger import log_task

class ExecutorAgent:
    def __init__(self, memory):
        self.llm = get_llm(0.1)
        self.memory = memory

    def execute(self, plan: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             """You are an executor agent.
Follow the plan exactly.
You can use tools:
- calculate(expression)
- write_file(filename, content)
- log_task(task)
Respond with execution steps and result."""),
            ("human", "{plan}")
        ])

        chain = prompt | self.llm
        response = chain.invoke({"plan": plan}).content

        self.memory.add("executor", response)
        log_task("Executed plan")

        return response
