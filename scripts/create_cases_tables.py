from config import *

import sqlite3
import csv
from pathlib import Path

DB_PATH = DB_PATH
CSV_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.enriched.csv")

def drop_and_create_tables(conn):
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS case_techniques")
    cur.execute("DROP TABLE IF EXISTS cases")

    cur.execute("""
        CREATE TABLE cases (
            case_id TEXT PRIMARY KEY,
            case_name TEXT NOT NULL,
            case_description TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE case_techniques (
            case_id TEXT,
            tech_id TEXT,
            PRIMARY KEY (case_id, tech_id),
            FOREIGN KEY (case_id) REFERENCES cases(case_id),
            FOREIGN KEY (tech_id) REFERENCES techniques(id)
        )
    """)

    conn.commit()
    print("✅ Tables `cases` and `case_techniques` were dropped and recreated.")

def populate_from_csv(conn):
    cur = conn.cursor()
    inserted_cases = 0
    inserted_links = 0
    seen_cases = set()
    seen_links = set()

    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            case_id = row["case_id"].strip()
            case_name = row["case_name"].strip()
            tech_id = row["tech_id"].strip()
            case_description = row.get("case_description", "").strip()

            # Insert unique cases
            if case_id not in seen_cases:
                cur.execute("""
                    INSERT INTO cases (case_id, case_name, case_description)
                    VALUES (?, ?, ?)
                """, (case_id, case_name, case_description))
                seen_cases.add(case_id)
                inserted_cases += 1

            # Insert junction
            link_key = (case_id, tech_id)
            if link_key not in seen_links:
                cur.execute("""
                    INSERT INTO case_techniques (case_id, tech_id)
                    VALUES (?, ?)
                """, link_key)
                seen_links.add(link_key)
                inserted_links += 1

    conn.commit()
    print(f"📥 Inserted {inserted_cases} unique cases.")
    print(f"🔗 Created {inserted_links} case-technique relationships.")

def main():
    with sqlite3.connect(DB_PATH) as conn:
        drop_and_create_tables(conn)
        populate_from_csv(conn)

if __name__ == "__main__":
    main()
