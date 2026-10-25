
import json
from datetime import datetime


def audit_deletion(record):
    remaining_sources = [
        source
        for source, deleted in record["sources"].items()
        if not deleted
    ]

    return {
        "customer_id": record["customer_id"],
        "status": "INCOMPLETE" if remaining_sources else "COMPLETE",
        "remaining_sources": remaining_sources,
        "audit_time": datetime.now().isoformat()
    }


def main():
    with open("sample_data.json", "r") as file:
        data = json.load(file)

    reports = []

    for customer in data["customers"]:
        if customer["deletion_requested"]:
            reports.append(audit_deletion(customer))

    print(json.dumps(reports, indent=4))

    with open("audit_report.json", "w") as file:
        json.dump(reports, file, indent=4)

    print("\nAudit report saved to audit_report.json")


if __name__ == "__main__":
    main()
