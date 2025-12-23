def log_task(task: str) -> str:
    with open("task_log.txt", "a", encoding="utf-8") as f:
        f.write(task + "\n")
    return "Task logged."
