import time
from rich.console import Console

def print_banner():
    console = Console()
    lines = [
        "[bold cyan] ██████╗██╗   ██╗ ██████╗ ████████╗███████╗[/bold cyan]",
        "[bold cyan]██╔════╝╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██╔════╝[/bold cyan]",
        "[bold cyan]██║      ╚████╔╝ ██║   ██║   ██║   █████╗  [/bold cyan]",
        "[bold cyan]██║       ╚██╔╝  ██║   ██║   ██║   ██╔══╝  [/bold cyan]",
        "[bold cyan]╚██████╗   ██║   ╚██████╔╝   ██║   ███████╗[/bold cyan]",
        "[bold cyan] ╚═════╝   ╚═╝    ╚═════╝    ╚═╝   ╚══════╝[/bold cyan]",
        "",
        "[bold magenta]            ☠ CYOTE TOOL WIZ ☠[/bold magenta]",
        "",
        "[yellow]Turn your tool into a knowledge file[/yellow]",
        "[green]that can be used with LLM and agentic workflows[/green]",
        ""
    ]

    for line in lines:
        console.print(line)
        time.sleep(0.15)
