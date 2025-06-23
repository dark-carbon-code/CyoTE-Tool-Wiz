from config import *

import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent.parent / "data" / DB_PATH
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("🔗 technique_tactics mappings:")
for row in cur.execute("""
    SELECT tt.tactic_id, tt.technique_id, t.name, tech.name
    FROM technique_tactics tt
    JOIN tactics t ON tt.tactic_id = t.id
    JOIN techniques tech ON tt.technique_id = tech.id
    ORDER BY tt.tactic_id
"""):
    print(f"  • {row[0]} → {row[1]}  ({row[2]} → {row[3]})")

conn.close()
