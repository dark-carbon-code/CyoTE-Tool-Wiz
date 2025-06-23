from config import *

# scripts/fill_missing_data_sources.py
import sqlite3
from pathlib import Path
import pandas as pd

# File paths
data_sources_csv = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques_data_sources.csv")
db_path = Path(DB_PATH)

# Load normalized technique → data source pairs
df = pd.read_csv(data_sources_csv)
df.columns = [col.strip().lower() for col in df.columns]

# Extract all unique data source names
unique_sources = sorted(set(df['data_source'].dropna().str.strip()))

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Get matrix_id for ICS
cur.execute("SELECT id FROM matrices WHERE name = 'ICS'")
matrix_row = cur.fetchone()
if not matrix_row:
    raise Exception("❌ No matrix named 'ICS' found in `matrices` table.")

matrix_id = matrix_row[0]

# Load existing data_sources
cur.execute("SELECT name FROM data_sources")
existing_sources = set(row[0].strip() for row in cur.fetchall())

# Insert missing ones with matrix_id
inserted = 0
for source in unique_sources:
    if source not in existing_sources:
        cur.execute(
            "INSERT INTO data_sources (name, matrix_id) VALUES (?, ?)",
            (source, matrix_id)
        )
        inserted += 1

conn.commit()
conn.close()

print(f"✅ Inserted {inserted} missing data sources into `data_sources` with matrix_id = {matrix_id}.")
