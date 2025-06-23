from config import *

import sqlite3
import os

DB_PATH = rDB_PATH

def inspect_par_cases(db_path):
    if not os.path.exists(db_path):
        print(f"❌ Database file not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("🔍 [DB SCHEMA CHECK]")
    # Check schema of relevant tables
    for table in ["cases", "case_techniques"]:
        cur.execute(f"PRAGMA table_info({table})")
        columns = cur.fetchall()
        if not columns:
            print(f"❌ Table `{table}` does not exist.")
        else:
            print(f"✅ Table `{table}` exists with columns:")
            for col in columns:
                print(f"   - {col[1]} ({col[2]})")

    print("\n📊 [PAR CASE TECHNIQUE SUMMARY]")
    # Get PAR case_ids
    cur.execute("SELECT case_id FROM cases WHERE case_id LIKE 'PAR%'")
    par_cases = [row[0] for row in cur.fetchall()]

    if not par_cases:
        print("⚠️ No PAR case_ids found in the `cases` table.")
        return

    for case_id in sorted(par_cases):
        cur.execute("""
            SELECT tech_id
            FROM case_techniques
            WHERE case_id = ?
            ORDER BY tech_id
        """, (case_id,))
        tech_ids = sorted({row[0] for row in cur.fetchall()})

        print(f"{case_id}: {len(tech_ids)} techniques")
        print(f"  → {tech_ids}")

    conn.close()

if __name__ == "__main__":
    inspect_par_cases(DB_PATH)
