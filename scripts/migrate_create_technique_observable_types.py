from config import *

import sqlite3
from pathlib import Path

# Path to the SQLite database
db_path = Path(DB_PATH)

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create the technique_observable_types table
cur.execute("""
CREATE TABLE IF NOT EXISTS technique_observable_types (
    technique_id TEXT NOT NULL,
    observable_type_id INTEGER NOT NULL,
    PRIMARY KEY (technique_id, observable_type_id),
    FOREIGN KEY (technique_id) REFERENCES techniques(id),
    FOREIGN KEY (observable_type_id) REFERENCES observable_types(id)
)
""")

conn.commit()
conn.close()
print("✅ Created 'technique_observable_types' table (if not already present).")
