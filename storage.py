import json
import os
import time

SAVE_FILE = "save.json"

DEFAULT_DATA = {
    "start_time": None,
    "paused": False,
    "pause_time": None,
    "paused_total": 0
}


def load():
    if not os.path.exists(SAVE_FILE):
        save(DEFAULT_DATA)
        return DEFAULT_DATA

    with open(SAVE_FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def reset():
    save(DEFAULT_DATA)
