from config import *

import sqlite3
import csv
from pathlib import Path

CSV_PATH = Path("data/ics-attack-v17.1-techniques-targeted-assets.csv")
DB_PATH = Path(DB_PATH)

def ensure_table_exists():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS technique_assets (
                technique_id TEXT NOT NULL,
                asset_id TEXT NOT NULL,
                PRIMARY KEY (technique_id, asset_id),
                FOREIGN KEY (technique_id) REFERENCES techniques(id),
                FOREIGN KEY (asset_id) REFERENCES assets(id)
            )
        """)
        conn.commit()
    print("✅ Ensured technique_assets table exists.")

def load_mappings_from_csv():
    print("🔄 Loading technique-to-asset relationships from CSV...")
    mappings = []
    with open(CSV_PATH, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tech_id = row["technique_id"].strip()
            asset_id = row["asset_id"].strip()
            if tech_id and asset_id:
                mappings.append((tech_id, asset_id))
    print(f"📊 Loaded {len(mappings)} mappings.")
    return mappings

def insert_mappings(mappings):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        inserted = 0
        for tech_id, asset_id in mappings:
            try:
                cur.execute("INSERT OR IGNORE INTO technique_assets (technique_id, asset_id) VALUES (?, ?)", (tech_id, asset_id))
                inserted += 1
            except sqlite3.IntegrityError as e:
                print(f"⚠️ Skipping ({tech_id}, {asset_id}): {e}")
        conn.commit()
    print(f"✅ Inserted {inserted} new technique-asset relationships.")

def main():
    ensure_table_exists()
    mappings = load_mappings_from_csv()
    insert_mappings(mappings)

if __name__ == "__main__":
    main()
