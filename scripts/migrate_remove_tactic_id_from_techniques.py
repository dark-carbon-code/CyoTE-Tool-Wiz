from config import *

import sqlite3
from pathlib import Path

# Set the database path
project_root = Path(__file__).resolve().parent.parent
db_path = project_root / "data" / DB_PATH

conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("🔄 Starting migration: Removing 'tactic_id' from 'techniques' table...")

# Step 1: Create a temporary table without the tactic_id
cur.execute("""
CREATE TABLE techniques_temp (
    id TEXT PRIMARY KEY,
    stix_id TEXT,
    name TEXT,
    description TEXT,
    url TEXT,
    matrix_id INTEGER,
    FOREIGN KEY (matrix_id) REFERENCES matrices(id)
);
""")

# Step 2: Copy data from old table into the new temp table
cur.execute("""
INSERT INTO techniques_temp (id, stix_id, name, description, url, matrix_id)
SELECT id, stix_id, name, description, url, matrix_id
FROM techniques;
""")

# Step 3: Drop the old techniques table
cur.execute("DROP TABLE techniques;")

# Step 4: Rename the new temp table to techniques
cur.execute("ALTER TABLE techniques_temp RENAME TO techniques;")

# Step 5: Verify
cur.execute("PRAGMA table_info(techniques);")
columns = cur.fetchall()
print("✅ New 'techniques' table schema:")
for col in columns:
    print(f"  - {col[1]} ({col[2]})")

# Commit and close
conn.commit()
conn.close()
print("🎉 Migration complete.")
