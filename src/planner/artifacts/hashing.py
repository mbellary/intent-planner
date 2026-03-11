import hashlib
import json
from typing import Any


def canonical_json_bytes(data: dict[str, Any]) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")


def compute_hash(data: dict[str, Any]) -> str:
    canonical = canonical_json_bytes(data)
    return hashlib.sha256(canonical).hexdigest()
