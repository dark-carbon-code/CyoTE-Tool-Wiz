from config import *

import sqlite3
import csv
from pathlib import Path

# Paths
DB_PATH = Path(DB_PATH)
CSV_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.enriched.csv")

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Create `cases` table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cases (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)

        # Create `technique_cases` junction table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS technique_cases (
                technique_id TEXT NOT NULL,
                case_id TEXT NOT NULL,
                PRIMARY KEY (technique_id, case_id),
                FOREIGN KEY (technique_id) REFERENCES techniques(id),
                FOREIGN KEY (case_id) REFERENCES cases(id)
            )
        """)

        conn.commit()

def import_data():
    seen_cases = set()
    rows_inserted = 0
    links_inserted = 0

    with sqlite3.connect(DB_PATH) as conn, CSV_PATH.open("r", encoding="utf-8") as csvfile:
        cur = conn.cursor()
        reader = csv.DictReader(csvfile)

        for row in reader:
            case_id = row["case_id"].strip()
            case_name = row["case_name"].strip()
            case_desc = row["case_description"].strip()
            tech_id = row["tech_id"].strip()

            # Insert case if not seen before
            if case_id not in seen_cases:
                cur.execute("""
                    INSERT OR IGNORE INTO cases (id, name, description)
                    VALUES (?, ?, ?)
                """, (case_id, case_name, case_desc))
                seen_cases.add(case_id)
                rows_inserted += 1

            # Insert technique-case relationship
            cur.execute("""
                INSERT OR IGNORE INTO technique_cases (technique_id, case_id)
                VALUES (?, ?)
            """, (tech_id, case_id))
            links_inserted += 1

        conn.commit()

    print(f"✅ Inserted {rows_inserted} unique cases.")
    print(f"🔗 Created {links_inserted} technique-case relationships.")

if __name__ == "__main__":
    print("🔄 Creating tables and importing case data...")
    create_tables()
    import_data()
