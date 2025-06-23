from config import *

# scripts/import_par_case_descriptions.py

import sqlite3
import csv
from pathlib import Path

DB_PATH = DB_PATH
CSV_PATH = "C:/Projects/cyote_tool_wiz/data/par_case_technique_descriptions_terminal_only.csv"

def main():
    print("📦 [1] Connecting to database...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Optional: Backup existing PAR rows
    print("🗂 [2] Backing up existing PAR entries...")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS case_technique_examples_backup AS 
        SELECT * FROM case_technique_examples WHERE case_id LIKE 'PAR%'
    """)
    conn.commit()

    # Delete existing PAR entries
    print("🧹 [3] Deleting old PAR entries...")
    cur.execute("DELETE FROM case_technique_examples WHERE case_id LIKE 'PAR%'")
    conn.commit()

    # Load and deduplicate new entries from CSV
    print("📄 [4] Loading new entries from CSV...")
    unique_rows = set()
    with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (
                row["case_id"].strip(),
                row["case_name"].strip(),
                row["tech_id"].strip(),
                row["tech_name"].strip(),
                row["case_description"].strip()
            )
            if all(key):  # Ensure no empty field in the composite key
                unique_rows.add(key)

    print(f"🔁 Deduplicated entries to insert: {len(unique_rows)}")

    cur.executemany("""
        INSERT INTO case_technique_examples 
        (case_id, case_name, tech_id, tech_name, case_description)
        VALUES (?, ?, ?, ?, ?)
    """, list(unique_rows))
    conn.commit()

    # Verify insert count
    cur.execute("SELECT COUNT(*) FROM case_technique_examples WHERE case_id LIKE 'PAR%'")
    new_total = cur.fetchone()[0]

    print(f"✅ [5] Inserted {len(unique_rows)} new PAR entries.")
    print(f"📊 [6] Total PAR entries in DB: {new_total}")
    conn.close()

if __name__ == "__main__":
    main()
