from config import *

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(DB_PATH)

with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    cur.execute("SELECT id, description, subcategories_json FROM use_cases")
    rows = cur.fetchall()

    updated_count = 0
    for row in rows:
        uc_id, desc, sub_json = row
        if desc and len(desc.strip()) > 0:
            continue  # skip already populated

        try:
            sub_list = json.loads(sub_json)
            full_text = " ".join(
                sub["text"].strip() for sub in sub_list if sub.get("text")
            )
            if full_text:
                cur.execute("""
                    UPDATE use_cases
                    SET description = ?
                    WHERE id = ?
                """, (full_text, uc_id))
                updated_count += 1
        except Exception as e:
            print(f"[!] Error parsing subcategories for ID {uc_id}: {e}")

    conn.commit()

print(f"✅ Updated {updated_count} use_cases with synthesized descriptions.")
