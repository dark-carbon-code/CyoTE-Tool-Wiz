from config import *

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(DB_PATH)

def query_db(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

def get_use_cases_for_nice_roles(nice_role_ids):
    if not nice_role_ids:
        return []

    placeholders = ",".join(["?"] * len(nice_role_ids))

    # Get mapped CSF categories and subcategories
    cat_rows = query_db(f"""
        SELECT DISTINCT csf_category_id FROM nice_to_csf_categories
        WHERE nice_role_id IN ({placeholders})
    """, nice_role_ids)

    subcat_rows = query_db(f"""
        SELECT DISTINCT csf_subcategory_id FROM nice_to_csf_subcategories
        WHERE nice_role_id IN ({placeholders})
    """, nice_role_ids)

    cat_ids = set(row["csf_category_id"] for row in cat_rows)
    subcat_ids = set(row["csf_subcategory_id"] for row in subcat_rows)

    # Start with category-mapped use cases
    all_use_cases = []
    seen_ids = set()

    if cat_ids:
        cat_placeholders = ",".join(["?"] * len(cat_ids))
        cat_cases = query_db(f"""
            SELECT * FROM use_cases WHERE csf_category_id IN ({cat_placeholders})
        """, list(cat_ids))
        all_use_cases.extend(cat_cases)
        seen_ids.update(uc["id"] for uc in cat_cases)

    # Now enrich with subcategory-mapped use cases
    if subcat_ids:
        all_cases = query_db("SELECT * FROM use_cases")
        for uc in all_cases:
            try:
                subcats = json.loads(uc.get("subcategories_json", "[]"))
                for sub in subcats:
                    if sub.get("id") in subcat_ids and uc["id"] not in seen_ids:
                        all_use_cases.append(uc)
                        seen_ids.add(uc["id"])
                        break
            except Exception:
                continue  # Skip bad JSON or missing fields

    return all_use_cases
