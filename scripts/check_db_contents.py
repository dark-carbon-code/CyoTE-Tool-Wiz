from config import *

from pathlib import Path
import sqlite3

# Set path to the SQLite DB
db_path = Path(__file__).resolve().parent.parent / "data" / DB_PATH

# Connect to DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List of tables to inspect
tables = [
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
]

print("📋 Sample contents of each table:\n")

for table in tables:
    print(f"🔎 {table}:")
    try:
        cursor.execute(f"SELECT * FROM {table} LIMIT 5")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print("  ", row)
        else:
            print("  (No records found)")
    except sqlite3.Error as e:
        print(f"  ❌ Error accessing {table}: {e}")
    print()

conn.close()
