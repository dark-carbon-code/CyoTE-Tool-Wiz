from config import *

import sqlite3
from pathlib import Path

# Path to your database
db_path = Path(DB_PATH)

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Check that every datasource_id in tool_datasources exists in data_sources
cur.execute("""
    SELECT td.datasource_id
    FROM tool_datasources td
    LEFT JOIN data_sources ds ON td.datasource_id = ds.id
    WHERE ds.id IS NULL
""")
invalid_links = cur.fetchall()

# Check that all data_sources are referenced at least once in tool_datasources
cur.execute("""
    SELECT ds.id, ds.name
    FROM data_sources ds
    LEFT JOIN tool_datasources td ON ds.id = td.datasource_id
    WHERE td.datasource_id IS NULL
""")
unreferenced_sources = cur.fetchall()

# Print results
print("\n🔍 Integrity Check: `tool_datasources` Table")

if invalid_links:
    print(f"\n❌ Invalid datasource_id references (not found in data_sources):")
    for row in invalid_links:
        print(f" - {row[0]}")
else:
    print("\n✅ All datasource_id values in `tool_datasources` reference valid entries.")

if unreferenced_sources:
    print(f"\n⚠️ Data sources defined in `data_sources` but NOT used in `tool_datasources`:")
    for row in unreferenced_sources:
        print(f" - {row[0]}: {row[1]}")
else:
    print("\n✅ All data_sources are referenced in tool_datasources at least once.")

conn.close()
