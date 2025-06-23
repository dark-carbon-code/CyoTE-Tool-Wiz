from config import *

import pandas as pd
import sqlite3
from pathlib import Path

# File paths
normalized_csv = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques_data_sources.csv")
db_path = Path(DB_PATH)

# Load normalized mapping file
df = pd.read_csv(normalized_csv, encoding="utf-8", dtype=str)
df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))

# Connect to SQLite
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Load lookup tables from DB
cur.execute("SELECT id, name FROM data_sources")
data_source_lookup = {name.strip(): id_ for id_, name in cur.fetchall()}

cur.execute("SELECT id FROM techniques")
valid_techniques = {tech_id for (tech_id,) in cur.fetchall()}

# Clear existing data
cur.execute("DELETE FROM technique_data_sources")

# Insert new mappings
inserted = 0
missing_sources = {}
missing_techniques = set()

for _, row in df.iterrows():
    technique_id = row["technique_id"].strip()
    data_source_name = row["data_source"].strip()

    if not technique_id or technique_id not in valid_techniques:
        missing_techniques.add(technique_id)
        continue

    data_source_id = data_source_lookup.get(data_source_name)
    if not data_source_id:
        missing_sources.setdefault(data_source_name, []).append(technique_id)
        continue

    cur.execute("""
        INSERT OR IGNORE INTO technique_data_sources (technique_id, data_source_id)
        VALUES (?, ?)
    """, (technique_id, data_source_id))
    inserted += 1

conn.commit()
conn.close()

# Summary output
print(f"\n✅ Inserted {inserted} rows into technique_data_sources.")

if missing_sources:
    print("\n⚠️ Missing data sources:")
    for ds, techs in sorted(missing_sources.items()):
        print(f"  {ds} → Techniques: {', '.join(techs)}")

if missing_techniques:
    print("\n⚠️ Missing or invalid technique IDs:")
    for tech in sorted(missing_techniques):
        print(f"  {tech}")

if not missing_sources and not missing_techniques:
    print("🎉 All technique → data source relationships successfully mapped.")
