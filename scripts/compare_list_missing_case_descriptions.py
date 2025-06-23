from config import *

import pandas as pd
import sqlite3
import json
from collections import defaultdict

CSV_PATH = "C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.enriched.csv"
DB_PATH = DB_PATH
TABLE_NAME = "case_technique_examples"

# --- Step 1: Load and validate CSV ---
print("📥 Loading CSV...")
df = pd.read_csv(CSV_PATH)
required_cols = {"case_id", "case_name", "tech_id", "tech_name", "case_description"}
missing_cols = required_cols - set(df.columns)
if missing_cols:
    raise ValueError(f"❌ Missing columns in CSV: {missing_cols}")

df = df.dropna(subset=["case_id", "tech_id", "case_description"]).drop_duplicates()
print(f"✅ Loaded {len(df)} unique (case_id, tech_id, case_description) rows.")

# --- Step 2: Connect to DB and inspect schema ---
print("🔍 Connecting to database and inspecting schema...")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
existing_tables = {row[0] for row in cur.fetchall()}
print(f"📚 Tables in DB: {existing_tables}")

# Check and create/adjust table
if TABLE_NAME not in existing_tables:
    print(f"🧱 Creating new table '{TABLE_NAME}'...")
    cur.execute(f"""
        CREATE TABLE {TABLE_NAME} (
            case_id TEXT,
            case_name TEXT,
            tech_id TEXT,
            tech_name TEXT,
            case_description TEXT,
            PRIMARY KEY (case_id, tech_id, case_description)
        )
    """)
else:
    # Inspect table columns
    cur.execute(f"PRAGMA table_info({TABLE_NAME});")
    current_columns = {row[1] for row in cur.fetchall()}
    missing_fields = required_cols - current_columns
    for col in missing_fields:
        print(f"➕ Adding missing column: {col}")
        cur.execute(f"ALTER TABLE {TABLE_NAME} ADD COLUMN {col} TEXT")

conn.commit()

# --- Step 3: Insert Data ---
print("📤 Inserting new rows...")
inserted = 0
for row in df.itertuples(index=False):
    cur.execute(f"""
        INSERT OR IGNORE INTO {TABLE_NAME} 
        (case_id, case_name, tech_id, tech_name, case_description)
        VALUES (?, ?, ?, ?, ?)
    """, (row.case_id, row.case_name, row.tech_id, row.tech_name, row.case_description))
    inserted += 1

conn.commit()
print(f"✅ Inserted {inserted} new rows into '{TABLE_NAME}'.")

# --- Step 4: Verify count ---
cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
total = cur.fetchone()[0]
print(f"📊 Total records in '{TABLE_NAME}': {total}")

# --- Step 5: Print Sample JSON Output ---
print("\n📦 Sample `related_cases` JSON (first 2 grouped cases):\n")

cur.execute(f"""
    SELECT case_id, case_name, tech_id, tech_name, case_description
    FROM {TABLE_NAME}
    ORDER BY case_id, tech_id
""")
rows = cur.fetchall()

case_map = defaultdict(lambda: {"case_id": "", "case_name": "", "descriptions": []})
for row in rows:
    cid, cname, tid, tname, desc = row
    if not desc or not desc.strip():
        continue
    case_map[cid]["case_id"] = cid
    case_map[cid]["case_name"] = cname or "Unknown Case"
    case_map[cid]["descriptions"].append({
        "tech_id": tid,
        "tech_name": tname,
        "case_description": desc
    })

sample_output = list(case_map.values())[:2]
print(json.dumps(sample_output, indent=2))

conn.close()
