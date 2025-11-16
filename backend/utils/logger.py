import datetime

def log(msg):
    """Simple colorful logger with timestamps."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\033[96m[{time}] SIAG:\033[0m {msg}")
