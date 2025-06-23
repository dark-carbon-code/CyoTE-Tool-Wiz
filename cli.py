from rich import print
from wizard.ascii_art import print_banner
from wizard.interactive_create import create_tool
from wizard.interactive_update import update_tool
from InquirerPy import inquirer

def main():
    print_banner()

    action = inquirer.select(
        message="🔧 CYOTE TOOL WIZ - Choose an action:",
        choices=[
            "🛠 Create a new tool entry",
            "🔁 Update an existing tool entry",
            "❌ Exit"
        ]
    ).execute()

    if action.startswith("🛠"):
        create_tool()
    elif action.startswith("🔁"):
        update_tool()
    else:
        print("[yellow]👋 Exiting CYOTE TOOL WIZ. Stay cyber-safe![/yellow]")

if __name__ == "__main__":
    main()