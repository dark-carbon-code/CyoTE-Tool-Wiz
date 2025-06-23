from config import *

import sqlite3
from pathlib import Path
from collections import Counter

# Path to the database
db_path = Path(DB_PATH)

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("\n📋 Validating `tool_deployment_context` table...\n")

# Total entries
cur.execute("SELECT COUNT(*) FROM tool_deployment_context")
total = cur.fetchone()[0]
print(f"🔢 Total entries: {total}")

# Count by category
cur.execute("SELECT category, COUNT(*) FROM tool_deployment_context GROUP BY category")
print("\n📂 Count by category:")
for cat, count in cur.fetchall():
    print(f"  • {cat}: {count}")

# Check for duplicate labels
cur.execute("SELECT label FROM tool_deployment_context")
labels = [row[0] for row in cur.fetchall()]
dupes = [item for item, count in Counter(labels).items() if count > 1]
if dupes:
    print("\n⚠️ Duplicate labels found:")
    for d in dupes:
        print(f"  • {d}")
else:
    print("\n✅ No duplicate labels found.")

# Check for missing descriptions
cur.execute("SELECT label FROM tool_deployment_context WHERE description IS NULL OR TRIM(description) = ''")
missing_desc = cur.fetchall()
if missing_desc:
    print("\n⚠️ Entries missing descriptions:")
    for (label,) in missing_desc:
        print(f"  • {label}")
else:
    print("\n✅ All entries have descriptions.")

# Done
conn.close()
