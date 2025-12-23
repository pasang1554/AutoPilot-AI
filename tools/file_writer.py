def write_file(filename: str, content: str) -> str:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File '{filename}' written successfully."
    except Exception as e:
        return f"File write error: {str(e)}"
