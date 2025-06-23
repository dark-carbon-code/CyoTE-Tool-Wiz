# utils/deployment_context.py

from InquirerPy import inquirer
from utils.db import query_db
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def select_trl_level():
    rows = query_db("SELECT * FROM trl_levels ORDER BY level ASC")

    console.rule("[bold green]📊 Technology Readiness Levels (DOE-defined)")

    for row in rows:
        text = Text()
        text.append(f"{row['description']}\n\n", style="bold")
        text.append(f"[Scale]        {row.get('scale', 'N/A')}\n", style="cyan")
        text.append(f"[Users]        {row.get('users', 'N/A')}\n", style="cyan")
        text.append(f"[Deliverables] {row.get('deliverables', 'N/A')}\n", style="cyan")
        text.append(f"[Environment]  {row.get('environment', 'N/A')}\n", style="cyan")

        # Format viability field
        viability = row.get("commercial_viable")
        if viability in (1, "1", True):
            viability = "Yes"
        elif viability in (0, "0", False):
            viability = "No"
        else:
            viability = str(viability)

        text.append(f"[Viability]    {viability}\n", style="cyan")

        panel = Panel(
            text,
            title=f"TRL {row['level']}: {row['name']}",
            border_style="blue",
            padding=(1, 2)
        )
        console.print(panel)

    choices = [f"[{row['level']}] {row['name']}" for row in rows]
    selected = inquirer.select(
        message="📈 Select one TRL level after reviewing the descriptions above:",
        choices=choices,
        instruction="Use arrow keys to select."
    ).execute()

    return rows[choices.index(selected)]

def select_hosting_env():
    rows = query_db("SELECT id, label, description FROM hosting_env ORDER BY id ASC")

    console.rule("[bold cyan]💻 Hosting Environment Options")

    for row in rows:
        panel = Panel.fit(
            Text(row["description"], style="dim"),
            title=f"[bold]{row['label']}[/bold]",
            border_style="blue"
        )
        console.print(panel)

    choices = [row["label"] for row in rows]
    selected_labels = inquirer.checkbox(
        message="📦 Select Hosting Environment(s) (or leave blank to add custom):",
        choices=choices,
        instruction="Use [space] to select, [enter] to confirm.",
        cycle=True,
        transformer=lambda result: f"{len(result)} selected"
    ).execute()

    selected_rows = [row for row in rows if row["label"] in selected_labels]

    # 🔍 Allow additional notes per selection
    for row in selected_rows:
        if inquirer.confirm(message=f"🛠 Add extra details for '{row['label']}'?", default=False).execute():
            row["note"] = inquirer.text(message="📝 Describe usage details or constraints:").execute().strip()

    # ➕ Allow custom additions
    if inquirer.confirm(message="➕ Add custom hosting environment?", default=False).execute():
        while True:
            custom_label = inquirer.text(message="🔧 Custom environment name (or leave blank to finish):").execute().strip()
            if not custom_label:
                break
            custom_description = inquirer.text(message="📘 Provide a short description:").execute().strip()
            custom_note = inquirer.text(message="📝 (Optional) Add specific usage details:").execute().strip()

            custom_entry = {
                "id": None,
                "label": custom_label,
                "description": custom_description,
                "note": custom_note
            }

            selected_rows.append(custom_entry)

            console.print(Panel.fit(
                Text(custom_description + ("\n" + custom_note if custom_note else ""), style="dim"),
                title=f"[bold magenta]{custom_label} (custom)[/bold magenta]",
                border_style="magenta"
            ))

    # ✅ Summary
    console.print(f"\n✅ [bold green]{len(selected_rows)} Hosting Environment(s) selected[/bold green]\n")
    for row in selected_rows:
        console.print(f"• [bold]{row['label']}[/bold]: {row['description']}")
        if row.get("note"):
            console.print(f"  [italic cyan]➤ Detail:[/italic cyan] {row['note']}")

    return selected_rows

def multi_select_context(category_name, table_name):
    rows = query_db(f"SELECT id, label, description FROM {table_name} ORDER BY id ASC")

    console.rule(f"[bold cyan]📚 {category_name} Options")

    for row in rows:
        panel = Panel.fit(
            Text(row['description'], style="dim"),
            title=f"[bold]{row['label']}[/bold]",
            border_style="green"
        )
        console.print(panel)

    choices = [row["label"] for row in rows]
    selected_labels = inquirer.checkbox(
        message=f"📌 Select {category_name} (or leave blank to add custom):",
        choices=choices,
        instruction="Use [space] to select, [enter] to confirm.",
        cycle=True,
        transformer=lambda result: f"{len(result)} selected"
    ).execute()

    selected_rows = [row for row in rows if row["label"] in selected_labels]

    # 🔍 Add additional detail for each selected item
    for row in selected_rows:
        if inquirer.confirm(message=f"🛠 Add extra details for '{row['label']}'?", default=False).execute():
            note = inquirer.text(message="📝 Describe usage details or constraints:").execute().strip()
            row["note"] = note

    # ➕ Allow custom additions
    if inquirer.confirm(message=f"➕ Add custom {category_name.lower()}?", default=False).execute():
        while True:
            custom_label = inquirer.text(message=f"🔧 Custom {category_name[:-1]} name (or leave blank to finish):").execute().strip()
            if not custom_label:
                break
            custom_description = inquirer.text(message="📘 Provide a short description:").execute().strip()
            custom_note = inquirer.text(message="📝 (Optional) Add specific usage details:").execute().strip()
            selected_rows.append({
                "id": None,
                "label": custom_label,
                "description": custom_description,
                "note": custom_note
            })

            console.print(Panel.fit(
                Text(custom_description + ("\n" + custom_note if custom_note else ""), style="dim"),
                title=f"[bold magenta]{custom_label} (custom)[/bold magenta]",
                border_style="magenta"
            ))

    # ✅ Summary
    console.print(f"\n✅ [bold green]{len(selected_rows)} {category_name} selected[/bold green]\n")
    for row in selected_rows:
        console.print(f"• [bold]{row['label']}[/bold]: {row['description']}")
        if row.get("note"):
            console.print(f"  [italic cyan]➤ Detail:[/italic cyan] {row['note']}")

    return selected_rows
