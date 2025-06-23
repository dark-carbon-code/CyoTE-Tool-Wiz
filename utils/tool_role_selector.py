from config import *

import sqlite3
import json
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.table import Table
from pathlib import Path

DB_PATH = Path(DB_PATH)
console = Console()

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

def preview_tool_roles(roles):
    """Display all tool roles in a rich table before prompting selection."""
    table = Table(title="📋 Tool Role Descriptions", expand=True, show_lines=True)
    table.add_column("Role", style="bold cyan", no_wrap=True)
    table.add_column("Description", style="white")

    for role in roles:
        table.add_row(role["name"], role["description"])

    console.print(table)

def select_tool_roles():
    roles = query_db("SELECT id, name, description FROM tool_roles ORDER BY name ASC")

    # Show preview before selection
    preview_tool_roles(roles)

    # Ask if user wants to re-display before picking
    if inquirer.confirm(message="🔍 View role descriptions again before selecting?", default=False).execute():
        preview_tool_roles(roles)

    # Select by name only to avoid truncating descriptions
    choices = [Choice(name=role["name"], value=role["id"]) for role in roles]
    selected_ids = inquirer.checkbox(
        message="👥 Select tool role(s):",
        choices=choices,
        instruction="Descriptions were shown above. Use space to select.",
        cycle=True
    ).execute()

    # Rebuild full role object + NICE mappings
    selected_roles = []
    for role in roles:
        if role["id"] in selected_ids:
            nice_roles = query_db("""
                SELECT nr.id, nr.title, nr.description,
                       nr.tasks_json, nr.knowledge_json, nr.skills_json
                FROM tool_role_nice_roles trnr
                JOIN nice_roles nr ON trnr.nice_role_id = nr.id
                WHERE trnr.tool_role_id = ?
            """, (role["id"],))

            # Deserialize JSON columns for full NICE role content
            enriched_nice_roles = []
            for nr in nice_roles:
                enriched_nice_roles.append({
                    "id": nr["id"],
                    "title": nr["title"],
                    "description": nr["description"],
                    "tasks": json.loads(nr["tasks_json"] or "[]"),
                    "knowledge": json.loads(nr["knowledge_json"] or "[]"),
                    "skills": json.loads(nr["skills_json"] or "[]")
                })

            role["nice_roles"] = enriched_nice_roles
            selected_roles.append(role)

    return selected_roles
