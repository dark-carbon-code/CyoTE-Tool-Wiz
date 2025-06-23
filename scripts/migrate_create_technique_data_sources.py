from config import *

import sqlite3
from pathlib import Path

db_path = Path(DB_PATH)
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create junction table for technique-data_source relationship
cur.execute("""
CREATE TABLE IF NOT EXISTS technique_data_sources (
    technique_id TEXT NOT NULL,
    data_source_id INTEGER NOT NULL,
    PRIMARY KEY (technique_id, data_source_id),
    FOREIGN KEY (technique_id) REFERENCES techniques(id),
    FOREIGN KEY (data_source_id) REFERENCES tool_datasources(id)
);
""")

conn.commit()
conn.close()

print("✅ Created table: technique_data_sources")
