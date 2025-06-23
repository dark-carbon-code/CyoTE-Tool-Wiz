from config import *

import pandas as pd
import sqlite3
from pathlib import Path

# File paths
csv_path = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-datasources.csv")
db_path = Path(DB_PATH)

# Load CSV
df = pd.read_csv(csv_path, encoding="cp1252", dtype=str)
df = df.rename(columns=lambda x: x.strip().lower())

# Drop rows with missing values
df = df.dropna(subset=["id", "name"])

# Remove duplicates
unique_sources = df[["id", "name"]].drop_duplicates()

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Ensure ICS matrix exists
cur.execute("SELECT id FROM matrices WHERE name = 'ICS'")
row = cur.fetchone()
if not row:
    raise ValueError("❌ ICS matrix not found in matrices table.")
ics_matrix_id = row[0]

# Recreate data_sources table
print("🔄 Rebuilding `data_sources` table...")

cur.execute("DROP TABLE IF EXISTS data_sources")
cur.execute("""
CREATE TABLE data_sources (
    id TEXT NOT NULL,
    name TEXT NOT NULL,
    matrix_id INTEGER NOT NULL,
    PRIMARY KEY (id, name),
    FOREIGN KEY (matrix_id) REFERENCES matrices(id)
)
""")

# Insert entries
inserted = 0
for _, row in unique_sources.iterrows():
    try:
        cur.execute(
            "INSERT INTO data_sources (id, name, matrix_id) VALUES (?, ?, ?)",
            (row["id"].strip(), row["name"].strip(), ics_matrix_id)
        )
        inserted += 1
    except Exception as e:
        print(f"⚠️ Error inserting {row['id']} → {row['name']}: {e}")

conn.commit()
conn.close()

print(f"\n✅ Inserted {inserted} data source entries into `data_sources` table.")
