import json


def serialize_plan(plan: dict) -> str:
    return json.dumps(plan, sort_keys=True, indent=2)
