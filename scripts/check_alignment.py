from config import *

import sqlite3
from pathlib import Path

# === Configuration ===
DB_PATH = Path(DB_PATH)

def summarize_use_cases():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        
        # Confirm table exists
        cur.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' AND name='use_cases'
        """)
        if not cur.fetchone():
            print("❌ Table 'use_cases' does not exist.")
            return
        
        # Count rows
        cur.execute("SELECT COUNT(*) FROM use_cases")
        total = cur.fetchone()[0]
        print(f"\n✅ use_cases table exists with [bold]{total}[/bold] entries.\n")

        # Fetch and summarize
        cur.execute("SELECT id, name, description FROM use_cases ORDER BY id")
        rows = cur.fetchall()

        for row in rows:
            uc_id, name, desc = row
            desc = desc or ""
            print(f"🆔 ID {uc_id} | {name}")
            print(f"   ↪ Description length: {len(desc)} characters")
            print(f"   ↪ Preview: {desc[:120].strip()}...\n")

if __name__ == "__main__":
    summarize_use_cases()
