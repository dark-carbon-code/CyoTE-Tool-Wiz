from config import *

import sqlite3
import csv
from pathlib import Path

DB_PATH = DB_PATH
CSV_PATH = "C:/Projects/cyote_tool_wiz/data/observable_types_descriptions_filled.csv"

def ensure_description_column(conn):
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(observable_types)")
    columns = [row[1] for row in cur.fetchall()]
    if "description" not in columns:
        print("➕ Adding 'description' column to observable_types...")
        cur.execute("ALTER TABLE observable_types ADD COLUMN description TEXT")
        conn.commit()
    else:
        print("✅ 'description' column already exists.")

def update_descriptions(conn, rows):
    cur = conn.cursor()
    updated = 0
    for row in rows:
        cur.execute("""
            UPDATE observable_types
            SET description = ?
            WHERE id = ?
        """, (row["description"], row["id"]))
        updated += cur.rowcount
    conn.commit()
    return updated

def main():
    print("🔍 Connecting to database...")
    if not Path(DB_PATH).exists():
        print(f"❌ Database not found: {DB_PATH}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        ensure_description_column(conn)

        print(f"📄 Loading CSV: {CSV_PATH}")
        with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]

        print(f"📦 Updating {len(rows)} observable_type descriptions...")
        count = update_descriptions(conn, rows)
        print(f"✅ {count} descriptions updated in the database.")

if __name__ == "__main__":
    main()
