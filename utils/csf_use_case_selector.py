from config import *

import sqlite3
import json
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

DB_PATH = DB_PATH
console = Console()

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

def display_use_case_details(use_case):
    title_text = Text(f"{use_case['csf_function_id']} - {use_case['name']}", style="bold")
    body = Text()

    # Description
    body.append("Description:\n", style="bold")
    desc = use_case.get("description", "").strip()
    body.append(f"{desc if desc else 'No description available.'}\n\n")

    # Subcategories
    body.append("Subcategories:\n", style="bold")
    try:
        subcats = json.loads(use_case.get("subcategories_json", "[]"))
        if subcats:
            for s in subcats:
                sid = s.get("id", "Unknown ID")
                text = s.get("text", "").strip()
                if text:
                    body.append(f"• {sid} — {text}\n")
                else:
                    body.append(f"• {sid} — No content available at this time.\n", style="italic")
        else:
            body.append("No subcategories available.\n", style="italic")
    except Exception:
        body.append("No subcategories available.\n", style="italic")
    body.append("\n")

    # Implementation Examples
    body.append("Implementation Examples:\n", style="bold")
    try:
        examples = json.loads(use_case.get("examples_json", "[]"))
        if examples:
            for ex in examples:
                text = ex.get("text", "").strip()
                body.append(f"- {text}\n")
        else:
            body.append("No implementation examples available.\n", style="italic")
    except Exception:
        body.append("No implementation examples available.\n", style="italic")

    console.print(Panel(body, title=title_text, expand=True))

def select_csf_use_cases():
    rows = query_db("SELECT DISTINCT csf_function_id FROM use_cases ORDER BY csf_function_id ASC")
    all_function_ids = sorted({row['csf_function_id'] for row in rows})

    func_labels = {
        "GV": "GOVERN", "ID": "IDENTIFY", "PR": "PROTECT",
        "DE": "DETECT", "RS": "RESPOND", "RC": "RECOVER"
    }

    choices = [
        Choice(name=f"{fid} - {func_labels.get(fid, 'Unknown')}", value=fid)
        for fid in all_function_ids
    ]
    selected_ids = inquirer.checkbox(
        message="📘 Select CSF 2.0 Function(s) to browse:",
        choices=choices,
        cycle=True,
        instruction="Use arrow keys and space to select multiple."
    ).execute()

    selected_use_cases = []

    for fid in selected_ids:
        console.rule(f"📂 Browsing use cases under {fid} - {func_labels.get(fid, 'Unknown')}")
        use_cases = query_db("SELECT * FROM use_cases WHERE csf_function_id = ?", (fid,))
        for uc in use_cases:
            display_use_case_details(uc)
            confirm = inquirer.confirm(
                message="✅ Include this use case?", default=True
            ).execute()
            if confirm:
                selected_use_cases.append(uc)

    if selected_use_cases:
        console.rule("[bold cyan]📋 Use Case Summary")
        summary_choices = [
            Choice(name=f"{uc['csf_function_id']} - {uc['name']}", value=uc)
            for uc in selected_use_cases
        ]
        final_selected = inquirer.checkbox(
            message="✅ Review and confirm selected use cases:",
            choices=summary_choices,
            instruction="Use space to toggle, Enter to confirm.",
            cycle=True
        ).execute()
        console.rule("[bold green]✅ Final use case selection complete")
        return final_selected
    else:
        console.print("[yellow]⚠ No use cases were selected.[/yellow]")
        return []
