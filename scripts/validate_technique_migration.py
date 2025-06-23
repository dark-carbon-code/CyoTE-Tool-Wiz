from config import *

import sqlite3
from pathlib import Path

# Set the database path
project_root = Path(__file__).resolve().parent.parent
db_path = project_root / "data" / DB_PATH

conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("🔍 Validating 'techniques' table migration...")

# Step 1: Get the current columns in the techniques table
cur.execute("PRAGMA table_info(techniques);")
columns = [row[1] for row in cur.fetchall()]

expected_columns = {'id', 'stix_id', 'name', 'description', 'url', 'matrix_id'}
unexpected_columns = set(columns) - expected_columns
missing_columns = expected_columns - set(columns)

if 'tactic_id' in columns:
    print("❌ 'tactic_id' column still exists — migration failed.")
else:
    print("✅ 'tactic_id' column is correctly removed.")

if missing_columns:
    print(f"❌ Missing expected columns: {missing_columns}")
else:
    print("✅ All expected columns are present.")

if unexpected_columns:
    print(f"⚠️ Unexpected columns detected: {unexpected_columns}")

# Step 2: Check number of rows in techniques
cur.execute("SELECT COUNT(*) FROM techniques;")
techniques_count = cur.fetchone()[0]

print(f"📊 Total techniques records: {techniques_count}")

# Step 3: Check for orphaned technique_tactics relationships
cur.execute("""
SELECT COUNT(*) FROM technique_tactics
WHERE technique_id NOT IN (SELECT id FROM techniques);
""")
orphans = cur.fetchone()[0]
if orphans > 0:
    print(f"❌ Found {orphans} orphaned records in 'technique_tactics'.")
else:
    print("✅ No orphaned 'technique_tactics' relationships.")

conn.close()
print("🧪 Validation complete.")
