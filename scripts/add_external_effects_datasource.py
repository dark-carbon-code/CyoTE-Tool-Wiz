from config import *

import sqlite3
from pathlib import Path

# Paths
db_path = Path(DB_PATH)

# Connect to database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Step 1: Fetch all existing data source IDs
cur.execute("SELECT id FROM data_sources")
existing_ids = {row[0] for row in cur.fetchall() if row[0].startswith("DS")}

# Step 2: Find the next available DS00NN ID
next_id = None
i = 1
while True:
    candidate = f"DS{str(i).zfill(4)}"
    if candidate not in existing_ids:
        next_id = candidate
        break
    i += 1

# Step 3: Get ICS matrix ID
cur.execute("SELECT id FROM matrices WHERE name = 'ICS'")
matrix_row = cur.fetchone()
if not matrix_row:
    raise ValueError("❌ ICS matrix not found.")
ics_matrix_id = matrix_row[0]

# Step 4: Insert the new data source
new_name = "External Effects: Human Observation Needed"
try:
    cur.execute("""
        INSERT INTO data_sources (id, name, matrix_id)
        VALUES (?, ?, ?)
    """, (next_id, new_name, ics_matrix_id))
    conn.commit()
    print(f"✅ Inserted data source: {next_id} → {new_name}")
except Exception as e:
    print(f"❌ Failed to insert data source: {e}")

conn.close()
