class MemoryStore:
    def __init__(self):
        self.memory = []

    def add(self, role: str, content: str):
        self.memory.append({"role": role, "content": content})

    def get_all(self):
        return self.memory

    def clear(self):
        self.memory = []
