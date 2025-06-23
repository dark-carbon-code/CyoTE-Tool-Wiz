from config import *

import sqlite3
from pathlib import Path

# Path to the SQLite database
db_path = Path(DB_PATH)

# Establish connection
with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()

    # Fetch all observable types (id + name)
    cur.execute("SELECT id, name FROM observable_types")
    observable_types = cur.fetchall()
    observable_lookup = {name.lower(): id for id, name in observable_types}

    # Fetch all data sources (id + name)
    cur.execute("SELECT id, name FROM data_sources")
    data_sources = cur.fetchall()

    inserted = 0
    unmatched = []

    for ds_id, ds_name in data_sources:
        ds_name_lower = ds_name.lower()

        # Try exact match first
        if ds_name_lower in observable_lookup:
            obs_id = observable_lookup[ds_name_lower]
            cur.execute("""
                INSERT OR IGNORE INTO data_source_observable_types (data_source_id, observable_type_id)
                VALUES (?, ?)
            """, (ds_id, obs_id))
            inserted += 1
            continue

        # Try partial matching: look for substring match
        matched = False
        for obs_name, obs_id in observable_lookup.items():
            if obs_name in ds_name_lower or ds_name_lower in obs_name:
                cur.execute("""
                    INSERT OR IGNORE INTO data_source_observable_types (data_source_id, observable_type_id)
                    VALUES (?, ?)
                """, (ds_id, obs_id))
                inserted += 1
                matched = True
                break

        if not matched:
            unmatched.append((ds_id, ds_name))

    conn.commit()

# Print results
print(f"\n✅ Inserted {inserted} mappings into data_source_observable_types.")

if unmatched:
    print("\n⚠️ Unmatched data sources (no matching observable type):")
    for ds_id, name in unmatched:
        print(f"  - {ds_id}: {name}")
else:
    print("🎉 All data sources successfully mapped to observable types.")
