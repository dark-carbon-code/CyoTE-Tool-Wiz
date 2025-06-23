from config import *

import sqlite3

db_path = DB_PATH

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Ensure no ID conflict
cur.execute("SELECT id FROM data_sources WHERE id = 'DS0099'")
if cur.fetchone():
    raise ValueError("❌ DS0099 already exists in data_sources. Choose another ID or delete the existing one.")

# Update the ID
cur.execute("""
    UPDATE data_sources
    SET id = 'DS0099'
    WHERE name = 'External Effects: Human Observation Needed'
""")

conn.commit()
conn.close()

print("✅ Data source ID updated to DS0099.")
