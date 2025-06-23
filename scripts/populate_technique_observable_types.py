from config import *

import sqlite3
from pathlib import Path

# Path to SQLite DB
db_path = Path(DB_PATH)

# Connect
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Clear existing entries (optional – uncomment if needed)
# cur.execute("DELETE FROM technique_observable_types")

# Build mapping: technique_id -> observable_type_id (via data source)
cur.execute("""
    SELECT DISTINCT 
        tds.technique_id,
        dot.observable_type_id
    FROM technique_data_sources tds
    JOIN data_source_observable_types dot ON tds.data_source_id = dot.data_source_id
""")

mappings = cur.fetchall()
print(f"🔍 Found {len(mappings)} technique → observable_type mappings.")

# Insert
inserted = 0
for technique_id, observable_type_id in mappings:
    try:
        cur.execute("""
            INSERT OR IGNORE INTO technique_observable_types (technique_id, observable_type_id)
            VALUES (?, ?)
        """, (technique_id, observable_type_id))
        inserted += 1
    except Exception as e:
        print(f"❌ Error inserting {technique_id} → {observable_type_id}: {e}")

conn.commit()
conn.close()
print(f"✅ Inserted {inserted} rows into technique_observable_types.")
