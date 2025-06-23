from config import *

import sqlite3
import json
from InquirerPy import inquirer
from utils.file_utils import save_tool_json
from rich import print

DB_PATH = DB_PATH

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def create_tool():
    print("[bold green]\n--- CYOTE TOOL WIZ: Create New Tool Entry ---[/bold green]")

    tool_name = inquirer.text(message="🛠 Tool name:").execute()
    description = inquirer.text(message="📘 Description:").execute()

    # User Roles
    roles = query_db("SELECT name FROM tool_roles")
    selected_roles = inquirer.checkbox(
        message="👥 Select applicable user roles:",
        choices=[r["name"] for r in roles],
        instruction="(Use spacebar to select one or more)"
    ).execute()

    # Matrix Selection
    matrix_choice = inquirer.select(
        message="🧭 Choose a MITRE matrix to start with:",
        choices=["ICS", "Enterprise"]
    ).execute()

    # Tactic Selection
    tactics = query_db("""SELECT t.id, t.name FROM tactics t JOIN matrices m ON t.matrix_id = m.id WHERE m.name = ?""", (matrix_choice,))
    selected_tactic_ids = inquirer.checkbox(
        message="🎯 Select supported tactics:",
        choices=[f"{t['id']} - {t['name']}" for t in tactics]
    ).execute()

    # Technique Entry: Known
    known_tech_input = inquirer.text(
        message="🔍 Enter known Technique IDs or Names (comma-separated):",
        default=""
    ).execute()

    selected_techniques = []
    if known_tech_input:
        known_vals = [k.strip().lower() for k in known_tech_input.split(",")]
        all_techs = query_db("SELECT id, name, description FROM techniques WHERE matrix = ?", (matrix_choice,))
        for val in known_vals:
            for t in all_techs:
                if val in t["id"].lower() or val in t["name"].lower():
                    selected_techniques.append(dict(t))

    # Manual Technique Selection
    if inquirer.confirm(message="➕ Manually select techniques by tactic?", default=True).execute():
        for tactic in selected_tactic_ids:
            tactic_id = tactic.split(" - ")[0]
            techs = query_db("""
                SELECT t.id, t.name, t.description
                FROM techniques t
                JOIN technique_tactics tt ON tt.technique_id = t.id
                WHERE tt.tactic_id = ?
            """, (tactic_id,))
            if techs:
                manual_selection = inquirer.checkbox(
                    message=f"📌 Select techniques under [bold]{tactic}[/bold]:",
                    choices=[f"{t['id']} - {t['name']}" for t in techs]
                ).execute()
                for choice in manual_selection:
                    tid = choice.split(" - ")[0]
                    match = next((t for t in techs if t["id"] == tid), None)
                    if match and match not in selected_techniques:
                        selected_techniques.append(dict(match))
                        print(f"[cyan]{match['id']}[/cyan]: {match['description']}\n")

    # Data Sources
    ds_results = query_db("""SELECT ds.id, ds.name FROM data_sources ds JOIN matrices m ON ds.matrix_id = m.id WHERE m.name = ?""", (matrix_choice,))
    selected_ds_ids = inquirer.checkbox(
        message="🔎 Select data sources (before observable types):",
        choices=[f"{ds['id']} - {ds['name']}" for ds in ds_results]
    ).execute()

    # Observable Types
    obs_results = query_db("SELECT name, category FROM observable_types")
    obs_choices = [f"{obs['category']} - {obs['name']}" for obs in obs_results]
    selected_obs_types = inquirer.checkbox(
        message="📊 Select observable types (based on data source relevance):",
        choices=obs_choices
    ).execute()

    # Use Cases
    use_cases = query_db("SELECT id, name FROM tool_use_cases")
    selected_use_cases = inquirer.checkbox(
        message="📈 Select NIST CSF 2.0-aligned use cases:",
        choices = [{"name": uc["name"], "value": uc["id"]} for uc in use_cases]
    ).execute()

    # Deployment Context
    dep_context = query_db("SELECT id, label, description FROM tool_deployment_context")

    # Show full label and description in the prompt, store selected IDs
    selected_contexts = inquirer.checkbox(
        message="🚀 Select deployment context details (inputs/outputs/hosting/interface):",
        choices=[{"name": f"{row['label']} → {row['description']}", "value": row["id"]} for row in dep_context],
        instruction="(Choose all that apply for how the tool operates and integrates)"
    ).execute()

    # Free Text: Example Usage, GitHub, Fact Sheet
    example_usage = inquirer.text(message="📌 Paste example usage or doc excerpt:").execute()
    github_link = inquirer.text(message="🔗 GitHub link (optional):").execute()
    fact_sheet = inquirer.text(message="📄 Fact sheet/documentation link (optional):").execute()

    # Save as JSON
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
    print(f"\n[bold blue]✔ Tool entry for '{tool_name}' saved successfully![/bold blue]")
