import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "workday_data.json"

def get_workday_data() -> dict:
    with open(DATA_PATH, "r") as f:
        return json.load(f)
