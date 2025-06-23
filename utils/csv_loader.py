import csv
import json
from pathlib import Path

DATA_DIR = Path("data")

def load_csv_to_dict(filepath):
    """
    Load a CSV file into a list of dictionaries, with encoding fallback.
    Tries UTF-8 first, then falls back to Windows-1252 (common for Excel files).
    """
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            return list(csv.DictReader(csvfile))
    except UnicodeDecodeError:
        with open(filepath, newline='', encoding='windows-1252') as csvfile:
            return list(csv.DictReader(csvfile))


def load_mitre_data(data_type, matrix=None):
    files = {
        "tactics": {
            "ICS": "ics-attack-v17.1-tactics.csv",
            "Enterprise": "enterprise-attack-v17.1-tactics.csv"
        },
        "techniques": {
            "ICS": "ics-attack-v17.1-techniques.csv",
            "Enterprise": "enterprise-attack-v17.1-techniques.csv"
        },
        "data_sources": {
            "ICS": "ics-attack-v17.1-datasources.csv",
            "Enterprise": "enterprise-attack-v17.1-datasources.csv"
        }
    }

    if data_type not in files or matrix not in files[data_type]:
        return []

    file_path = DATA_DIR / files[data_type][matrix]
    rows = load_csv_to_dict(file_path)

    if data_type == "tactics":
        return sorted([
            json.dumps({"name": row["name"].strip(), "matrix": matrix})
            for row in rows if row.get("name")
        ])

    if data_type == "techniques":
        return sorted([
            {
                "id": row.get("technique_id", "").strip(),
                "name": row.get("name", "").strip(),
                "matrix": matrix,
                "tactic": row.get("tactic", "").strip(),
                "description": row.get("description", "").strip()
            }
            for row in rows if row.get("technique_id")
        ], key=lambda x: x["id"])

    if data_type == "data_sources":
        return sorted([
            {
                "name": row.get("name", "").strip(),
                "description": row.get("description", "").strip()
            }
            for row in rows if row.get("name")
        ], key=lambda x: x["name"])

    return []


def get_techniques_by_matrix_tactic(techniques, tactic_name):
    return [t for t in techniques if t.get("tactic", "").lower() == tactic_name.lower()]


def get_technique_description(techniques, technique_id):
    for t in techniques:
        if t["id"] == technique_id:
            return t.get("description", "No description found.")
    return "Technique not found."