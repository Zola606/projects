"""Normalize synthetic SOC events; no network access or external data."""
import json
import sys
from datetime import datetime, timezone


def normalize(event):
    required = ("timestamp", "source", "event_type")
    missing = [key for key in required if not event.get(key)]
    if missing:
        raise ValueError(f"missing fields: {', '.join(missing)}")
    timestamp = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
    return {
        "timestamp": timestamp.astimezone(timezone.utc).isoformat(),
        "source": str(event["source"]).strip().lower(),
        "event_type": str(event["event_type"]).strip().lower(),
        "severity": event.get("severity", "low"),
        "asset": event.get("asset", "unknown"),
    }


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(normalize(json.loads(line))))

