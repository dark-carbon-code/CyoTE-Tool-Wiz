import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_VARS = {
    "tool_capabilities": "TOOL_DIR",
    "chunks": "CHUNKS_DIR",
    "tool_knowledge.db": "DB_PATH"
}

def update_script(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated = False

    for folder, var in CONFIG_VARS.items():
        if folder in content:
            pattern = re.compile(rf"(\"|')([^\"']*{folder}[^\"']*)(\"|')")
            content = pattern.sub(f"{var}", content)
            updated = True

    if updated and "from config import" not in content:
        content = f"from config import *\n\n{content}"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Updated: {file_path}")

def process_all_py_files():
    for path in PROJECT_ROOT.rglob("*.py"):
        if "config.py" in path.name:
            continue
        update_script(path)

if __name__ == "__main__":
    process_all_py_files()
