from config import *

import sqlite3
from pathlib import Path

DB_PATH = DB_PATH

def main(limit=10):
    print("🔍 Connecting to database...")
    if not Path(DB_PATH).exists():
        print(f"❌ Database not found at {DB_PATH}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # Confirm column exists
        cur.execute("PRAGMA table_info(observable_types)")
        columns = [row["name"] for row in cur.fetchall()]
        if "description" not in columns:
            print("❌ 'description' column not found in observable_types.")
            return

        # Fetch contents
        cur.execute("SELECT id, name, category, description FROM observable_types ORDER BY id")
        rows = cur.fetchall()
        print(f"📊 Total rows: {len(rows)}\n")

        for row in rows[:limit]:
            print(f"🧱 [{row['id']}] {row['name']} ({row['category']}):")
            print(f"    {row['description'][:200]}{'...' if len(row['description']) > 200 else ''}\n")

if __name__ == "__main__":
    main()
