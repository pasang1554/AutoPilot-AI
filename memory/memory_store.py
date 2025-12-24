class MemoryStore:
    def __init__(self):
        self.history = []

    def add(self, role: str, content: str):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_context(self):
        return "\n".join(
            f"{item['role'].upper()}: {item['content']}"
            for item in self.history
        )

    def clear(self):
        self.history = []
