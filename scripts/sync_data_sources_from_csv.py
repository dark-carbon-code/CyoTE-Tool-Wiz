from config import *

import sqlite3
import pandas as pd
from pathlib import Path

# File and DB paths
csv_path = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-datasources.csv")
db_path = Path(DB_PATH)

# Load CSV
df = pd.read_csv(csv_path, encoding="cp1252", dtype=str)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Get matrix_id for ICS
cur.execute("SELECT id FROM matrices WHERE name = 'ICS'")
ics_matrix_id = cur.fetchone()
if not ics_matrix_id:
    raise ValueError("ICS matrix not found in matrices table.")
ics_matrix_id = ics_matrix_id[0]

# Track insertions
inserted = 0
skipped = 0

# Sync each entry
for _, row in df.iterrows():
    ds_id = row.get("id", "").strip()
    ds_name = row.get("name", "").strip()
    if not ds_id or not ds_name:
        continue

    cur.execute("SELECT 1 FROM data_sources WHERE id = ?", (ds_id,))
    exists = cur.fetchone()
    if exists:
        skipped += 1
    else:
        cur.execute(
            "INSERT INTO data_sources (id, name, matrix_id) VALUES (?, ?, ?)",
            (ds_id, ds_name, ics_matrix_id)
        )
        inserted += 1

conn.commit()
conn.close()

# Report
print(f"\n✅ Inserted {inserted} new data sources.")
print(f"⏭️ Skipped {skipped} existing data sources.")
