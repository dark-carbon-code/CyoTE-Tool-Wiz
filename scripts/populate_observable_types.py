from config import *

import sqlite3
from pathlib import Path

# Path to your SQLite database
db_path = Path(DB_PATH)

# Connect to database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Helper to normalize name
def normalize(name):
    return name.strip().lower()

# Valid categories enforced by DB schema
VALID_CATEGORIES = ['Host', 'Network', 'External Effects']

# Revised categorization logic
def categorize(name):
    name_lc = name.lower()
    if any(keyword in name_lc for keyword in ["network", "dns", "connection"]):
        return "Network"
    elif any(keyword in name_lc for keyword in [
        "process", "file", "registry", "script", "command", "logon",
        "service", "module", "drive", "volume", "account", "job", "firmware", "kernel"
    ]):
        return "Host"
    elif "external" in name_lc or "human observation" in name_lc:
        return "External Effects"
    else:
        # Fallback: default to Host if uncategorized but required
        return "Host"

# Get existing observable types
cur.execute("SELECT name FROM observable_types")
existing = set(normalize(row[0]) for row in cur.fetchall())

# Get all data source names
cur.execute("SELECT name FROM data_sources")
data_sources = [row[0].strip() for row in cur.fetchall()]

inserted = 0
skipped = 0

for ds_name in data_sources:
    norm_name = normalize(ds_name)
    if norm_name in existing:
        skipped += 1
        continue

    category = categorize(ds_name)
    if category not in VALID_CATEGORIES:
        print(f"❌ Skipping '{ds_name}' → invalid category: {category}")
        continue

    try:
        cur.execute("INSERT INTO observable_types (name, category) VALUES (?, ?)", (ds_name, category))
        inserted += 1
    except sqlite3.IntegrityError as e:
        print(f"⚠️ Failed to insert '{ds_name}': {e}")

conn.commit()
conn.close()

# Final Summary
print("\n📦 Observable Types Population Complete")
print(f"✅ Inserted: {inserted}")
print(f"⏭️ Skipped: {skipped}")
print(f"📊 Total Processed: {inserted + skipped}")
