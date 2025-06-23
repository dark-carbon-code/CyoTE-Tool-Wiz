from config import *

import sqlite3
from pathlib import Path

# Path to the database
db_path = Path(DB_PATH)

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("🔍 Database Integrity and Validation Report\n")

# 1. Table existence check
expected_tables = {
    "techniques", "data_sources", "observable_types",
    "technique_tactics", "technique_data_sources",
    "technique_observable_types", "data_source_observable_types"
}

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
actual_tables = {row[0] for row in cur.fetchall()}

missing_tables = expected_tables - actual_tables
extra_tables = actual_tables - expected_tables

print("📦 Tables:")
for table in sorted(actual_tables):
    print(f"  ✅ {table}")

if missing_tables:
    print("\n❌ Missing expected tables:")
    for table in sorted(missing_tables):
        print(f"  - {table}")

# 2. Foreign key consistency check
def check_fk_consistency(junction_table, fk_column, ref_table, ref_column):
    cur.execute(f"""
        SELECT jt.{fk_column}
        FROM {junction_table} jt
        LEFT JOIN {ref_table} rt ON jt.{fk_column} = rt.{ref_column}
        WHERE rt.{ref_column} IS NULL
    """)
    missing = cur.fetchall()
    if missing:
        print(f"\n❌ {junction_table}.{fk_column} has {len(missing)} broken references to {ref_table}.{ref_column}")
        for value in missing:
            print(f"   - Missing: {value[0]}")
    else:
        print(f"✅ {junction_table}.{fk_column} references {ref_table}.{ref_column} are valid.")

print("\n🔗 Foreign Key Validations:")

# Validate junction table references
check_fk_consistency("technique_tactics", "technique_id", "techniques", "id")
check_fk_consistency("technique_data_sources", "technique_id", "techniques", "id")
check_fk_consistency("technique_data_sources", "data_source_id", "data_sources", "id")
check_fk_consistency("technique_observable_types", "technique_id", "techniques", "id")
check_fk_consistency("technique_observable_types", "observable_type_id", "observable_types", "id")
check_fk_consistency("data_source_observable_types", "data_source_id", "data_sources", "id")
check_fk_consistency("data_source_observable_types", "observable_type_id", "observable_types", "id")

conn.close()
print("\n🎉 Database integrity validation complete.")
