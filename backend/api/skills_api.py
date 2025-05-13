import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "skills_data.json"

def get_skills_data() -> dict:
    with open(DATA_PATH, "r") as f:
        return json.load(f)
