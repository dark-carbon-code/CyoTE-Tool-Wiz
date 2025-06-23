from config import *

import sqlite3
import json
from InquirerPy import inquirer
from utils.file_utils import save_tool_json
from rich import print
from pathlib import Path

DB_PATH = DB_PATH

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def insert_tool_to_db(tool_data):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO tools (tool_name, description) VALUES (?, ?)", 
                    (tool_data["tool_name"], tool_data["description"]))
        tool_id = cur.lastrowid

        for role in tool_data["user_roles"]:
            cur.execute("INSERT INTO tool_roles (tool_id, name) VALUES (?, ?)", (tool_id, role))

        for tactic in tool_data["tactics_supported"]:
            tactic_id = tactic.split(" - ")[0]
            cur.execute("INSERT INTO tool_tactics (tool_id, tactic_id) VALUES (?, ?)", (tool_id, tactic_id))

        for tech in tool_data["techniques_supported"]:
            cur.execute("INSERT INTO tool_techniques (tool_id, technique_id) VALUES (?, ?)", (tool_id, tech["id"]))

        for ds in tool_data["data_sources"]:
            ds_id = ds.split(" - ")[0]
            cur.execute("INSERT INTO tool_datasources (tool_id, data_source_id) VALUES (?, ?)", (tool_id, ds_id))

        for obs in tool_data["observable_types"]:
            cur.execute("INSERT INTO tool_observable_types (tool_id, observable_name) VALUES (?, ?)", (tool_id, obs))

        for uc_id in tool_data["use_cases"]:
            cur.execute("INSERT INTO tool_use_cases (id) VALUES (?) ON CONFLICT DO NOTHING", (uc_id,))
            cur.execute("INSERT INTO tool_use_case_links (tool_id, use_case_id) VALUES (?, ?)", (tool_id, uc_id))

        for ctx_id in tool_data["deployment_context"]:
            cur.execute("INSERT INTO tool_deployment_context_links (tool_id, context_id) VALUES (?, ?)", (tool_id, ctx_id))

        cur.execute("UPDATE tools SET example_usage = ?, github = ?, factsheet = ? WHERE id = ?", (
            tool_data.get("example_usage", ""), 
            tool_data.get("github", None), 
            tool_data.get("factsheet", None), 
            tool_id
        ))

        conn.commit()

def create_tool():
    print("[bold green]\n--- CYOTE TOOL WIZ: Create New Tool Entry ---[/bold green]")

    tool_name = inquirer.text(message="🛠 Tool name:").execute()
    description = inquirer.text(message="📘 Describe what this tool does and how it's used:").execute()

    roles = query_db("SELECT name FROM tool_roles")
    selected_roles = inquirer.checkbox(
        message="👥 Select applicable user roles:",
        choices=[r["name"] for r in roles],
        instruction="(Spacebar to select)"
    ).execute()

    matrix_choice = inquirer.select(
        message="🧭 Choose MITRE matrix:",
        choices=["ICS", "Enterprise"]
    ).execute()

    tactics = query_db("""SELECT t.id, t.name FROM tactics t 
                          JOIN matrices m ON t.matrix_id = m.id WHERE m.name = ?""", (matrix_choice,))
    selected_tactic_ids = inquirer.checkbox(
        message="🎯 Select supported tactics:",
        choices=[f"{t['id']} - {t['name']}" for t in tactics]
    ).execute()

    known_input = inquirer.text(
        message="🔍 Known Technique IDs or Names (comma-separated):", default=""
    ).execute()

    selected_techniques = []
    if known_input:
        known_vals = [k.strip().lower() for k in known_input.split(",")]
        all_techs = query_db("SELECT id, name, description FROM techniques WHERE matrix = ?", (matrix_choice,))
        for val in known_vals:
            for t in all_techs:
                if val in t["id"].lower() or val in t["name"].lower():
                    selected_techniques.append(dict(t))

    if inquirer.confirm(message="➕ Select techniques manually by tactic?", default=True).execute():
        for tactic in selected_tactic_ids:
            tactic_id = tactic.split(" - ")[0]
            techs = query_db("""
                SELECT t.id, t.name, t.description FROM techniques t
                JOIN technique_tactics tt ON tt.technique_id = t.id
                WHERE tt.tactic_id = ?
            """, (tactic_id,))
            if techs:
                manual_selection = inquirer.checkbox(
                    message=f"📌 Techniques under [bold]{tactic}[/bold]:",
                    choices=[f"{t['id']} - {t['name']}" for t in techs]
                ).execute()
                for choice in manual_selection:
                    tid = choice.split(" - ")[0]
                    match = next((t for t in techs if t["id"] == tid), None)
                    if match and match not in selected_techniques:
                        selected_techniques.append(dict(match))
                        print(f"[cyan]{match['id']}[/cyan]: {match['description']}\n")

    # 🔎 Step: Show assets impacted by selected techniques
    if selected_techniques:
        tech_ids = tuple(t["id"] for t in selected_techniques)
        placeholder = ",".join(["?"] * len(tech_ids))
        asset_query = f"""
            SELECT DISTINCT a.id, a.name FROM assets a
            JOIN technique_assets ta ON a.id = ta.asset_id
            WHERE ta.technique_id IN ({placeholder})
        """
        assets = query_db(asset_query, tech_ids)
        if assets:
            print("\n[bold yellow]🎯 Assets potentially targeted by selected techniques:[/bold yellow]")
            for a in assets:
                print(f" - [green]{a['id']}[/green]: {a['name']}")

    ds_results = query_db("""SELECT ds.id, ds.name FROM data_sources ds 
                             JOIN matrices m ON ds.matrix_id = m.id WHERE m.name = ?""", (matrix_choice,))
    selected_ds_ids = inquirer.checkbox(
        message="🔎 Select data sources:",
        choices=[f"{ds['id']} - {ds['name']}" for ds in ds_results]
    ).execute()

    obs_results = query_db("SELECT name, category FROM observable_types")
    obs_choices = [f"{obs['category']} - {obs['name']}" for obs in obs_results]
    selected_obs_types = inquirer.checkbox(
        message="📊 Select observable types (based on DS relevance):",
        choices=obs_choices
    ).execute()

    use_cases = query_db("SELECT id, name FROM tool_use_cases")
    selected_use_cases = inquirer.checkbox(
        message="📈 Select NIST CSF 2.0 use cases:",
        choices=[{"name": uc["name"], "value": uc["id"]} for uc in use_cases]
    ).execute()

    dep_context = query_db("SELECT id, label, description FROM tool_deployment_context")
    selected_contexts = inquirer.checkbox(
        message="🚀 Select deployment context details (inputs/outputs/hosting/interface):",
        choices=[{"name": f"{r['label']} → {r['description']}", "value": r["id"]} for r in dep_context]
    ).execute()

    example_usage = inquirer.text(message="📌 Paste example usage from doc or README:").execute()
    github_link = inquirer.text(message="🔗 GitHub URL (if available):").execute()
    fact_sheet = inquirer.text(message="📄 Fact Sheet or PDF URL (if available):").execute()

    tool_entry = {
        "tool_name": tool_name,
        "description": description,
        "user_roles": selected_roles,
        "tactics_supported": selected_tactic_ids,
        "techniques_supported": selected_techniques,
        "data_sources": selected_ds_ids,
        "observable_types": selected_obs_types,
        "use_cases": selected_use_cases,
        "deployment_context": selected_contexts,
        "example_usage": example_usage,
        "github": github_link or None,
        "factsheet": fact_sheet or None
    }

    save_tool_json(tool_entry)
#    insert_tool_to_db(tool_entry)

    print(f"\n[bold blue]✔ Tool entry for '{tool_name}' saved successfully to JSON and database![/bold blue]")

if __name__ == "__main__":
    create_tool()
