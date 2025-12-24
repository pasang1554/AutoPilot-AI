ALLOWED_TOOLS = {"calculator", "file_writer", "task_logger"}

def run_tool(tool_name: str, args: list):
    if tool_name not in ALLOWED_TOOLS:
        return f"ERROR: Tool '{tool_name}' is not allowed."

    if tool_name == "calculator":
        return calculate(args[0])

    if tool_name == "file_writer":
        return write_file(args[0], args[1])

    if tool_name == "task_logger":
        return log_task(args[0])
