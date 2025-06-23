from config import *
import json
from InquirerPy import inquirer
from rich import print
from utils.file_utils import get_tool_files, load_tool_json, save_tool_json
from utils.csv_loader import load_mitre_data

def update_tool():
    print("[bold yellow]\n--- CYOTE TOOL WIZ: Update Existing Tool ---[/bold yellow]")

    tool_files = get_tool_files()
    if not tool_files:
        print("[red]No tool files found in:[/red]", TOOL_CAPABILITIES_DIR)
        return

    selected_file = inquirer.select(
        message="\U0001F527 Select a tool to update:",
        choices=tool_files
    ).execute()

    file_path = TOOL_CAPABILITIES_DIR / selected_file
    tool_data = load_tool_json(file_path)

    print(f"\n[bold cyan]Editing tool:[/bold cyan] [green]{tool_data.get('tool_name')}[/green]")

    if not inquirer.confirm(message="\U0001F504 Do you want to overwrite all fields with new inputs?").execute():
        print("[green]✅ No changes made.[/green]")
        return

    tool_name = inquirer.text(
        message="\U0001F6E0 Tool name:",
        default=tool_data.get("tool_name", "")
    ).execute()

    description = inquirer.text(
        message="\U0001F4D8 Description:",
        default=tool_data.get("description", "")
    ).execute()

    user_roles = inquirer.checkbox(
        message="\U0001F465 Update user roles:",
        choices=[
            "IT Staff", "IT Cybersecurity", "OT Staff", "OT Cybersecurity",
            "Support Staff", "Management", "Engineering"
        ],
        default=tool_data.get("user_roles", [])
    ).execute()

    matrix = inquirer.select(
        message="\U0001F9ED Which MITRE matrix was originally used for this tool?",
        choices=["ICS", "Enterprise"]
    ).execute()

    tactics = load_mitre_data("tactics", matrix=matrix)
    techniques = load_mitre_data("techniques", matrix=matrix)
    data_sources = load_mitre_data("data_sources", matrix=matrix)

    selected_tactics = inquirer.checkbox(
        message="\U0001F3AF Update supported tactics:",
        choices=[t["name"] for t in tactics],
        default=tool_data.get("tactics_supported", [])
    ).execute()

    selected_techniques = inquirer.checkbox(
        message="\U0001F9F0 Update supported techniques:",
        choices=[f"{t['id']} - {t['name']}" for t in techniques],
        default=[f"{t['id']} - {t['name']}" for t in tool_data.get("techniques_supported", [])]
    ).execute()

    selected_data_sources = inquirer.checkbox(
        message="\U0001F50D Update data sources:",
        choices=[f"{ds['name']} - {ds['description']}" for ds in data_sources],
        default=[f"{ds['name']} - {ds['description']}" for ds in tool_data.get("data_sources", [])]
    ).execute()

    observable_types = inquirer.checkbox(
        message="\U0001F9E0 Update observable types:",
        choices=[f"{ot['category']} - {ot['name']}" for ot in tool_data.get("observable_types", [])],
        default=[f"{ot['category']} - {ot['name']}" for ot in tool_data.get("observable_types", [])]
    ).execute()

    use_cases_input = inquirer.text(
        message="\U0001F4A1 Update use cases (comma separated):",
        default=", ".join([uc['name'] for uc in tool_data.get("use_cases", [])])
    ).execute()
    use_cases = [uc.strip() for uc in use_cases_input.split(",") if uc.strip()]

    deployment_context = inquirer.text(
        message="\U0001F680 Deployment context (freeform override):",
        default=json.dumps(tool_data.get("deployment_context", {}))
    ).execute()

    example_usage = inquirer.text(
        message="\U0001F4CC Example usage:",
        default=tool_data.get("example_usage", "")
    ).execute()

    github = inquirer.text(
        message="\U0001F517 GitHub link:",
        default=tool_data.get("github", "")
    ).execute()

    factsheet = inquirer.text(
        message="\U0001F4C4 Factsheet or documentation link:",
        default=tool_data.get("factsheet", "")
    ).execute()

    updated_entry = {
        "tool_name": tool_name,
        "description": description,
        "user_roles": user_roles,
        "tactics_supported": selected_tactics,
        "techniques_supported": selected_techniques,
        "observable_types": observable_types,
        "use_cases": use_cases,
        "data_sources": selected_data_sources,
        "deployment_context": deployment_context,
        "example_usage": example_usage,
        "github": github or None,
        "factsheet": factsheet or None
    }

    save_tool_json(updated_entry, file_name=selected_file)
    print(f"\n[bold blue]\u2714 Tool entry for '{tool_name}' updated successfully![/bold blue]")

if __name__ == "__main__":
    update_tool()
