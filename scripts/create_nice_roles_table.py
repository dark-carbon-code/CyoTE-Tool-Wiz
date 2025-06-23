from config import *

import sqlite3
from pathlib import Path

DB_PATH = Path(DB_PATH)

def create_mapping_table():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tool_role_nice_roles (
                tool_role_id INTEGER NOT NULL,
                nice_role_id TEXT NOT NULL,
                PRIMARY KEY (tool_role_id, nice_role_id),
                FOREIGN KEY (tool_role_id) REFERENCES tool_roles(id),
                FOREIGN KEY (nice_role_id) REFERENCES nice_roles(id)
            );
        """)
        conn.commit()
        print("✅ Table 'tool_role_nice_roles' created or already exists.")

if __name__ == "__main__":
    create_mapping_table()
