from config import *

import sqlite3
from pathlib import Path

# Path to DB
db_path = Path(__file__).resolve().parent.parent / "data" / DB_PATH
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Discovery tactic ID and associated technique IDs
tactic_id = "TA0102"
techniques = [
    "T0840",  # Network Connection Enumeration
    "T0842",  # Network Sniffing
    "T0846",  # Remote System Discovery
    "T0888",  # Remote System Information Discovery
    "T0887"   # Wireless Sniffing
]

# Insert mappings
for technique_id in techniques:
    cur.execute("""
        INSERT OR IGNORE INTO technique_tactics (technique_id, tactic_id)
        VALUES (?, ?)
    """, (technique_id, tactic_id))

conn.commit()
conn.close()
print("✅ TA0102 → techniques mapped successfully.")