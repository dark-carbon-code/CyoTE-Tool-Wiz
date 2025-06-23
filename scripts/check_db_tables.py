from config import *

import sqlite3
from pathlib import Path

# Path to your database
db_path = Path("data") / DB_PATH

# Expected table names (based on your schema)
expected_tables = {
    "matrices",
    "tactics",
    "techniques",
    "data_sources",
    "assets",
    "tools",
    "tool_roles",
    "tool_tactics",
    "tool_techniques",
    "tool_datasources",
    "tool_use_cases",
    "tool_observable_types"
}

# Connect to DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get actual tables in the DB
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
actual_tables = {row[0] for row in cursor.fetchall()}

print(DB_PATH)
for table in sorted(actual_tables):
    print(f"  ✅ {table}")

# Check for missing tables
missing_tables = expected_tables - actual_tables
if missing_tables:
    print("\n❌ Missing tables:")
    for table in sorted(missing_tables):
        print(f"  ❌ {table}")
else:
    print("\n🎉 All expected tables are present.")

conn.close()
