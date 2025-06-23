from config import *

import sqlite3
from pathlib import Path
from rich import print

DB_PATH = Path(DB_PATH)

with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    cur.execute("SELECT id, name, LENGTH(description), SUBSTR(description, 1, 120) FROM use_cases ORDER BY id")
    rows = cur.fetchall()

print(f"\n✅ [bold]use_cases[/bold] table loaded with {len(rows)} entries.\n")
for row in rows:
    uc_id, name, length, preview = row
    print(f"🆔 ID {uc_id} | {name}")
    print(f"   ↪ Description length: {length} characters")
    print(f"   ↪ Preview: {preview.strip()}...\n")
