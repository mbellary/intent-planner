import hashlib
import json


def compute_hash(data):

    canonical = json.dumps(data, sort_keys=True)

    return hashlib.sha256(canonical.encode()).hexdigest()
