import sys
import json
from datetime import datetime
from rich import print
from pathlib import Path
from wizard.ascii_art import print_banner
from wizard.interactive_create import create_tool
from wizard.interactive_update import update_tool
from InquirerPy import inquirer

# Optional imports
try:
    from scripts.print_tool_entry_schema import print_example_tool_schema
except ImportError:
    print_example_tool_schema = None

try:
    from utils.file_utils import generate_empty_tool_template, TOOL_CAPABILITIES_DIR
except ImportError:
    generate_empty_tool_template = None
    TOOL_CAPABILITIES_DIR = Path("./tool_capabilities")


def main():
    # CLI arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == "--schema":
            if print_example_tool_schema:
                print_example_tool_schema()
            else:
                print("[red]❌ Schema print function not found.[/red]")
            return

        elif arg == "--template":
            if not generate_empty_tool_template:
                print("[red]❌ Template generation function not available.[/red]")
                return

            TOOL_CAPABILITIES_DIR.mkdir(parents=True, exist_ok=True)
            template = generate_empty_tool_template()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            out_file = TOOL_CAPABILITIES_DIR / f"empty_tool_template_{timestamp}.json"

            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(template, f, indent=2)

            print(f"[green]✅ Empty tool template saved to:[/green] {out_file}")
            return

    # Interactive mode
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
