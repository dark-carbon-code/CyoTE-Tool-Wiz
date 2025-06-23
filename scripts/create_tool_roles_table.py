from config import *

# File: scripts/create_tool_roles_table.py

import sqlite3

DB_PATH = DB_PATH

roles = [
    "IT Staff",
    "IT Cybersecurity",
    "OT Staff",
    "OT Cybersecurity",
    "Support Staff",
    "Management",
    "Engineering"
]

with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()

    # Drop and recreate tool_roles table if needed
    cur.execute("DROP TABLE IF EXISTS tool_roles")
    cur.execute("""
        CREATE TABLE tool_roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    for role in roles:
        cur.execute("INSERT INTO tool_roles (name) VALUES (?)", (role,))

    conn.commit()

print("✅ tool_roles table created and populated successfully.")
