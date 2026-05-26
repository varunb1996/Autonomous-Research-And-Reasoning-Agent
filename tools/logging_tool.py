import os

from datetime import datetime

os.makedirs(
    "logs",
    exist_ok=True
)

LOG_FILE = "logs/agent_logs.txt"


def log_event(event):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"[{timestamp}] {event}\n"
        )