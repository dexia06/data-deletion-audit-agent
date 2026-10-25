
import json
from datetime import datetime


def audit_deletion(record):
    remaining_sources = []

    for source, deleted in record["sources"].items():
        if not deleted:
            remaining_sources.append(source)

    if remaining_sources:
        status = "INCOMPLETE"
    else:
        status = "COMPLETE"

    report = {
        "customer_id": record["customer_id"],
        "status": status,
        "remaining_sources": remaining_sources,
        "audit_time": datetime.now().isoformat()
    }

    return report


if __name__ == "__main__":
    sample_record = {
        "customer_id": "C001",
        "sources": {
            "database": True,
            "backup": True,
            "logs": False,
            "cloud_storage": True
        }
    }

    result = audit_deletion(sample_record)

    print(json.dumps(result, indent=4))

