from config import *

# scripts/json_output_preview.py

import sqlite3
import json
from rich import print

DB_PATH = DB_PATH

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

def build_par_tool_json():
    print("[bold green]📦 [1] Building tool entry for all CyOTE PAR techniques[/bold green]")

    # Fetch all distinct PAR techniques
    techs = query_db("""
        SELECT DISTINCT t.id, t.name, t.description
        FROM techniques t
        JOIN case_technique_examples cte ON cte.tech_id = t.id
    """)
    tech_ids = [t["id"] for t in techs]

    # Fetch related tactics
    placeholder = ",".join(["?"] * len(tech_ids))
    tactics = query_db(f"""
        SELECT DISTINCT tt.tactic_id, ta.name
        FROM technique_tactics tt
        JOIN tactics ta ON ta.id = tt.tactic_id
        WHERE tt.technique_id IN ({placeholder})
    """, tech_ids)
    tactic_ids = [f"{t['tactic_id']} - {t['name']}" for t in tactics]

    # Fetch related assets
    assets = query_db(f"""
        SELECT DISTINCT a.id, a.name, a.description
        FROM assets a
        JOIN technique_assets ta ON ta.asset_id = a.id
        WHERE ta.technique_id IN ({placeholder})
    """, tech_ids)

    # Fetch case descriptions
    case_entries = query_db(f"""
        SELECT case_id, case_name, tech_id, tech_name, case_description
        FROM case_technique_examples
        WHERE tech_id IN ({placeholder})
    """, tech_ids)

    # Organize case descriptions properly
    case_map = {}
    for row in case_entries:
        if not row["case_description"].strip():
            continue
        cid = row["case_id"]
        if cid not in case_map:
            case_map[cid] = {
                "case_id": cid,
                "case_name": row["case_name"] or "Unknown Case",
                "descriptions": []
            }
        case_map[cid]["descriptions"].append({
            "tech_id": row["tech_id"],
            "tech_name": row["tech_name"],
            "case_description": row["case_description"]
        })
    related_cases = list(case_map.values())

    # Fetch data sources and observables
    data_sources = query_db(f"""
        SELECT DISTINCT ds.id, ds.name
        FROM data_sources ds
        JOIN technique_data_sources tds ON ds.id = tds.data_source_id
        WHERE tds.technique_id IN ({placeholder})
    """, tech_ids)

    ds_ids = [ds["id"] for ds in data_sources]
    if ds_ids:
        ds_placeholder = ",".join(["?"] * len(ds_ids))
        observables = query_db(f"""
            SELECT DISTINCT ot.name, ot.category
            FROM observable_types ot
            JOIN data_source_observable_types dsot ON dsot.observable_type_id = ot.id
            WHERE dsot.data_source_id IN ({ds_placeholder})
        """, ds_ids)
    else:
        observables = []

    # Build tool JSON
    tool_entry = {
        "tool_name": "Example Tool with All PAR Techniques",
        "description": "This tool includes all MITRE ATT&CK for ICS techniques associated with CyOTE PAR case studies.",
        "user_roles": [{"name": "Researcher"}],
        "tactics_supported": tactic_ids,
        "techniques_supported": techs,
        "data_sources": data_sources,
        "observable_types": observables,
        "targeted_assets": assets,
        "related_cases": related_cases,
        "use_cases": [],
        "deployment_context": [],
        "example_usage": "Used to benchmark all known PAR-relevant techniques across asset types and observables.",
        "github": None,
        "factsheet": None
    }

    print(f"\n[bold cyan]📑 Preview JSON Output Structure[/bold cyan]")
    print(json.dumps(tool_entry, indent=2))

def main():
    build_par_tool_json()

if __name__ == "__main__":
    main()
