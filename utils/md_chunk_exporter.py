# utils/md_chunk_exporter.py

import os
import json
from pathlib import Path
from datetime import datetime
from rich import print
from utils.markdown_renderer import render_markdown_sections, render_section_with_metadata

CHUNKS_MD_DIR = Path("chunks_md")
TOOL_DIR = Path("tool_capabilities")


def write_md_file(filename_prefix: str, section: str, content: str, tool_name: str):
    """Writes a single markdown file with metadata and summary."""
    filename = f"{filename_prefix}__{section}.md"
    path = CHUNKS_MD_DIR / filename
    final_md = render_section_with_metadata(section, content, tool_name)

    with open(path, "w", encoding="utf-8") as f:
        f.write(final_md)

    print(f"[green]✔ {section} saved:[/green] {path}")


def export_tool_to_md_chunks(tool: dict, filename_hint: str = None):
    """Exports a tool entry into separate markdown files by section."""
    CHUNKS_MD_DIR.mkdir(parents=True, exist_ok=True)

    tool_name = tool.get("tool_name", "unnamed_tool").replace(" ", "_").replace("/", "-")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    base = f"{tool_name}__{filename_hint or timestamp}"

    section_map = render_markdown_sections(tool)

    for section, markdown_body in section_map.items():
        write_md_file(base, section, markdown_body, tool_name)


def export_latest_tool_file():
    """Helper to load the most recent tool JSON and export its Markdown chunks."""
    files = sorted(TOOL_DIR.glob("*.json"), key=os.path.getmtime, reverse=True)
    if not files:
        print("[red]❌ No tool JSON files found in tool_capabilities/[/red]")
        return

    latest_file = files[0]
    with open(latest_file, "r", encoding="utf-8") as f:
        tool = json.load(f)

    export_tool_to_md_chunks(tool, filename_hint="sections")


if __name__ == "__main__":
    export_latest_tool_file()
