def log_message(message):
    print(f"[LOG] {message}")

def format_data(data):
    return {key: str(value) for key, value in data.items()}