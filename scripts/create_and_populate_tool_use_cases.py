from config import *

import sqlite3
from pathlib import Path

db_path = Path(DB_PATH)

use_cases = [
    "Govern: Organizational Context",
    "Govern: Risk Management Strategy",
    "Govern: Roles, Responsibilities, and Authorities",
    "Govern: Policies, Processes, and Procedures",
    "Govern: Oversight",
    "Govern: Cybersecurity Supply Chain Risk Management",
    "Identify: Asset Management",
    "Identify: Risk Assessment",
    "Identify: Improvement",
    "Protect: Identity Management, Authentication, and Access Control",
    "Protect: Awareness and Training",
    "Protect: Data Security",
    "Protect: Platform Security",
    "Protect: Configuration Management",
    "Protect: Maintenance",
    "Protect: Protective Technology",
    "Detect: Anomalies and Events",
    "Detect: Security Continuous Monitoring",
    "Detect: Detection Processes",
    "Respond: Incident Management",
    "Respond: Communications",
    "Respond: Analysis",
    "Respond: Mitigation",
    "Respond: Improvements",
    "Recover: Recovery Planning",
    "Recover: Improvements",
    "Recover: Communications"
]

# Connect to DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop and recreate table
cur.execute("DROP TABLE IF EXISTS tool_use_cases")
cur.execute("""
    CREATE TABLE tool_use_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
""")

# Insert categories
inserted = 0
for uc in use_cases:
    try:
        cur.execute("INSERT INTO tool_use_cases (name) VALUES (?)", (uc,))
        inserted += 1
    except Exception as e:
        print(f"❌ Error inserting '{uc}': {e}")

conn.commit()
conn.close()

print(f"\n✅ Completed: {inserted} NIST CSF 2.0-aligned use cases inserted into tool_use_cases.")
