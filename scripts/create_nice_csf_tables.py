from config import *

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(DB_PATH)
EXCEL_PATH = Path("data/NICE Framework to CSF Mapping - v2.0.0 to V2 - March 2025.xlsx")

def create_mapping_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS nice_to_csf_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nice_role_id TEXT,
                csf_category_id TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS nice_to_csf_subcategories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nice_role_id TEXT,
                csf_subcategory_id TEXT
            )
        """)
        conn.commit()
    print("✅ Mapping tables created successfully.")

def populate_category_mapping():
    df = pd.read_excel(EXCEL_PATH, sheet_name=1)

    df = df.dropna(subset=["CSF 2.0 Category Identifier", "v2.0.0 NICE Framework  Work Roles"])
    df = df.astype(str)

    mappings = []
    for _, row in df.iterrows():
        category_id = row["CSF 2.0 Category Identifier"].strip()
        nice_roles = [r.strip() for r in row["v2.0.0 NICE Framework  Work Roles"].split(",")]

        for nr in nice_roles:
            if nr:
                mappings.append((nr, category_id))

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.executemany("""
            INSERT INTO nice_to_csf_categories (nice_role_id, csf_category_id) VALUES (?, ?)
        """, mappings)
        conn.commit()
    print(f"✅ Inserted {len(mappings)} category-level NICE→CSF mappings.")

def populate_subcategory_mapping():
    df = pd.read_excel(EXCEL_PATH, sheet_name=2)

    df = df.dropna(subset=["CSF 2.0 Subcategory ID", "v2.0.0 NICE Framework Work Roles"])
    df = df.astype(str)

    mappings = []
    for _, row in df.iterrows():
        sub_id = row["CSF 2.0 Subcategory ID"].strip()
        nice_roles = [r.strip() for r in row["v2.0.0 NICE Framework Work Roles"].split(",")]

        for nr in nice_roles:
            if nr:
                mappings.append((nr, sub_id))

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.executemany("""
            INSERT INTO nice_to_csf_subcategories (nice_role_id, csf_subcategory_id) VALUES (?, ?)
        """, mappings)
        conn.commit()
    print(f"✅ Inserted {len(mappings)} subcategory-level NICE→CSF mappings.")

if __name__ == "__main__":
    create_mapping_tables()
    populate_category_mapping()
    populate_subcategory_mapping()
