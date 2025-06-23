from config import *

import sqlite3
import csv
from pathlib import Path

CSV_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.enriched.csv")
DB_PATH = DB_PATH

def count_unique_cases_in_csv():
    seen = set()
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["case_id"].strip(), row["case_description"].strip())
            seen.add(key)
    return seen

def fetch_cases_from_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT case_id, case_description FROM cases")
        all_cases = set(cur.fetchall())

        cur.execute("""
            SELECT DISTINCT c.case_id, c.case_description
            FROM cases c
            JOIN case_techniques ct ON c.case_id = ct.case_id
        """)
        linked_cases = set(cur.fetchall())

    return all_cases, linked_cases

def main():
    csv_cases = count_unique_cases_in_csv()
    db_cases, linked = fetch_cases_from_db()

    print(f"📄 Total unique case descriptions in CSV: {len(csv_cases)}")
    print(f"🗂  Cases in `cases` table: {len(db_cases)}")
    print(f"🔗 Cases linked to at least one technique: {len(linked)}")

    missing = csv_cases - db_cases
    if missing:
        print(f"\n❌ Missing {len(missing)} cases from DB (case_id + description):")
        for cid, desc in sorted(missing)[:10]:
            print(f" - {cid}: {desc[:80]}...")
    else:
        print("\n✅ All CSV case descriptions exist in the database.")

    not_linked = db_cases - linked
    if not_linked:
        print(f"\n⚠️  {len(not_linked)} cases in DB are NOT linked to any technique.")
        for cid, desc in sorted(not_linked)[:10]:
            print(f" - {cid}: {desc[:80]}...")
    else:
        print("\n✅ All cases in DB are linked to techniques.")

if __name__ == "__main__":
    main()
