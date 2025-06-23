from config import *

import sqlite3
from pathlib import Path

# Path to your DB
db_path = Path(DB_PATH)

# Connect to DB and inspect columns
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("\n📋 Columns in `tool_datasources` table:\n")
cur.execute("PRAGMA table_info(tool_datasources)")
columns = cur.fetchall()

for col in columns:
    print(f" - {col[1]} ({col[2]})")

conn.close()
