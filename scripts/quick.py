from config import *

import os

EXCLUDE_DIRS = {".venv", "__pycache__", ".git", ".mypy_cache", CHUNKS_DIR}
MAX_DEPTH = 4

def print_tree(start_path, prefix="", depth=0, output_lines=None):
    if output_lines is None:
        output_lines = []

    if depth > MAX_DEPTH:
        return output_lines

    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        return output_lines

    entries = [e for e in entries if e not in EXCLUDE_DIRS and not e.endswith(".pyc")]
    pointers = ["├── "] * (len(entries) - 1) + ["└── "]

    for pointer, entry in zip(pointers, entries):
        path = os.path.join(start_path, entry)
        output_lines.append(f"{prefix}{pointer}{entry}")
        if os.path.isdir(path):
            extension = "│   " if pointer == "├── " else "    "
            print_tree(path, prefix + extension, depth + 1, output_lines)

    return output_lines

if __name__ == "__main__":
    root_dir = r"C:\Projects\cyote_tool_wiz"
    output_file = os.path.join(root_dir, "project_structure_short.txt")

    print(f"📦 Generating filtered structure for: {root_dir}")
    structure = [f"📂 Project Structure (filtered): {root_dir}", ""]
    structure.extend(print_tree(root_dir))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(structure))

    print(f"✅ Output written to: {output_file}")
