from config import *

import sqlite3
import json
from pathlib import Path
from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm

DB_PATH = Path(DB_PATH)
console = Console()

def load_tool_roles():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute("SELECT id, name FROM tool_roles").fetchall()

def load_nice_roles():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute("SELECT id, title, description, tasks_json, knowledge_json, skills_json FROM nice_roles ORDER BY title ASC").fetchall()

def display_nice_role(nice_role):
    text = Text()
    text.append(f"[bold]{nice_role['title']}[/bold] ({nice_role['id']})\n", style="cyan")
    text.append(f"\n[italic]Description:[/italic]\n{nice_role['description']}\n\n")

    tasks = json.loads(nice_role['tasks_json'])
    knowledge = json.loads(nice_role['knowledge_json'])
    skills = json.loads(nice_role['skills_json'])

    text.append("[bold]Tasks:[/bold]\n")
    for t in tasks[:5]:
        text.append(f"- {t}\n")
    if len(tasks) > 5:
        text.append("  ...\n")

    text.append("\n[bold]Knowledge Areas:[/bold]\n")
    for k in knowledge[:5]:
        text.append(f"- {k}\n")
    if len(knowledge) > 5:
        text.append("  ...\n")

    text.append("\n[bold]Skills:[/bold]\n")
    for s in skills[:5]:
        text.append(f"- {s}\n")
    if len(skills) > 5:
        text.append("  ...\n")

    console.print(Panel(text, title=f"NICE Role: {nice_role['title']}", expand=True))

def collect_mappings():
    tool_roles = load_tool_roles()
    nice_roles = load_nice_roles()
    mappings = {}

    for tr in tool_roles:
        console.rule(f"🧩 Tool Role: [bold yellow]{tr['name']}[/bold yellow]")
        selected_ids = []

        for nr in nice_roles:
            display_nice_role(nr)
            if Confirm.ask(f"Link this NICE role to '{tr['name']}'?"):
                selected_ids.append(nr['id'])

        mappings[tr['id']] = selected_ids

    return mappings

def preview_and_confirm(mappings):
    console.rule("📋 Preview Selections")
    tool_roles = {tr['id']: tr['name'] for tr in load_tool_roles()}
    nice_roles = {nr['id']: nr['title'] for nr in load_nice_roles()}

    for tid, nids in mappings.items():
        console.print(f"\n[bold]{tool_roles[tid]}[/bold] →", style="green")
        for nid in nids:
            console.print(f"  - {nice_roles.get(nid, nid)} ({nid})")

    return Confirm.ask("\n✅ Save these mappings to the database?")

def save_mappings(mappings):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for tid, nids in mappings.items():
            for nid in nids:
                cur.execute("""
                    INSERT OR IGNORE INTO tool_role_nice_roles (tool_role_id, nice_role_id)
                    VALUES (?, ?)
                """, (tid, nid))
        conn.commit()
    console.print("\n✅ [bold green]Mappings saved successfully.")

if __name__ == "__main__":
    mappings = collect_mappings()
    if preview_and_confirm(mappings):
        save_mappings(mappings)
    else:
        console.print("❌ [bold red]Aborted. No changes saved.")