from config import *

import sqlite3
from pathlib import Path

# Path to the SQLite database
db_path = Path(DB_PATH)

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create observable_types table
cur.execute("""
CREATE TABLE IF NOT EXISTS observable_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT CHECK(category IN ('Host', 'Network', 'External Effects')) NOT NULL
);
""")

# Commit and close
conn.commit()
conn.close()

print("✅ Table 'observable_types' created or already exists.")
