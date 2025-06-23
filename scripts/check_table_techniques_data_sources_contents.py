from config import *

import sqlite3
from tabulate import tabulate

# Path to the database
db_path = DB_PATH

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Query to join technique_data_sources with data_sources and display results
query = """
SELECT 
    tds.technique_id, 
    ds.id AS data_source_id,
    ds.name AS data_source_name
FROM 
    technique_data_sources tds
JOIN 
    data_sources ds ON tds.data_source_id = ds.id
ORDER BY 
    tds.technique_id, ds.name
"""

cur.execute(query)
rows = cur.fetchall()

# Print results
print("\n📋 Contents of technique_data_sources (joined with data_sources):\n")
print(tabulate(rows, headers=["Technique ID", "Data Source ID", "Data Source Name"], tablefmt="grid"))

# Print count
print(f"\n📊 Total rows in technique_data_sources: {len(rows)}")

# Clean up
conn.close()
