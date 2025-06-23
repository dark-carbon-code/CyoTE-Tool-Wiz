from config import *

import sqlite3
from pathlib import Path

# Path to the SQLite DB
db_path = Path(DB_PATH)

# SQL to create the junction table
create_sql = """
CREATE TABLE IF NOT EXISTS data_source_observable_types (
    data_source_id TEXT NOT NULL,
    observable_type_id INTEGER NOT NULL,
    PRIMARY KEY (data_source_id, observable_type_id),
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id),
    FOREIGN KEY (observable_type_id) REFERENCES observable_types(id)
);
"""

# Execute the script
with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()
    cur.execute(create_sql)
    conn.commit()

print("✅ data_source_observable_types table created (or already exists).")
