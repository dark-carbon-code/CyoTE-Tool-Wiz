from config import *

import sqlite3
from pathlib import Path

# Path to your SQLite database
db_path = Path(DB_PATH)

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Query the observable_types table
cur.execute("SELECT id, name, category FROM observable_types ORDER BY category, name")
rows = cur.fetchall()

# Display results
print("\n📋 Contents of `observable_types` table:\n")
for row in rows:
    print(f"  ID: {row[0]:<3} | Category: {row[2]:<18} | Name: {row[1]}")

print(f"\n📊 Total observable types: {len(rows)}")

# Clean up
conn.close()
