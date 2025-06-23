from config import *

from pathlib import Path
import sqlite3
import csv

# Define project paths (go up one level to reach project root)
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
db_path = data_dir / DB_PATH

if not db_path.exists():
    raise FileNotFoundError(f"❌ Database file not found at {db_path}")

# Load CSV into dict rows
def load_csv(path):
    try:
        with open(path, newline='', encoding='utf-8-sig') as f:
            return list(csv.DictReader(f))
    except UnicodeDecodeError:
        with open(path, newline='', encoding='windows-1252') as f:
            return list(csv.DictReader(f))

# Ensure matrix exists and return its ID
def ensure_matrix(cur, name):
    cur.execute("INSERT OR IGNORE INTO matrices (name) VALUES (?)", (name,))
    cur.execute("SELECT id FROM matrices WHERE name = ?", (name,))
    return cur.fetchone()[0]

# Paths to CSVs
ics_tactics_csv = data_dir / "ics-attack-v17.1-tactics.csv"
ics_techniques_csv = data_dir / "ics-attack-v17.1-techniques.csv"
ics_datasources_csv = data_dir / "ics-attack-v17.1-datasources.csv"
ics_assets_csv = data_dir / "ics-attack-v17.1-assets.csv"

ent_tactics_csv = data_dir / "enterprise-attack-v17.1-tactics.csv"
ent_techniques_csv = data_dir / "enterprise-attack-v17.1-techniques.csv"
ent_datasources_csv = data_dir / "enterprise-attack-v17.1-datasources.csv"

# Connect to SQLite
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Insert matrix names and get IDs
ics_matrix_id = ensure_matrix(cur, "ICS")
ent_matrix_id = ensure_matrix(cur, "Enterprise")

### ─── Tactics ───
for row in load_csv(ics_tactics_csv):
    cur.execute("""
        INSERT OR REPLACE INTO tactics (id, stix_id, name, description, url, matrix_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], row["url"], ics_matrix_id))

for row in load_csv(ent_tactics_csv):
    cur.execute("""
        INSERT OR REPLACE INTO tactics (id, stix_id, name, description, url, matrix_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], row["url"], ent_matrix_id))

### ─── Techniques ───
for row in load_csv(ics_techniques_csv):
    cur.execute("""
        INSERT OR REPLACE INTO techniques (id, stix_id, name, description, url, tactic_id, matrix_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], row["url"], None, ics_matrix_id))  # Normalization later

for row in load_csv(ent_techniques_csv):
    cur.execute("""
        INSERT OR REPLACE INTO techniques (id, stix_id, name, description, url, tactic_id, matrix_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], row["url"], None, ent_matrix_id))  # Normalization later

### ─── Data Sources ───
for row in load_csv(ics_datasources_csv):
    cur.execute("""
        INSERT OR REPLACE INTO data_sources (id, stix_id, name, description, matrix_id)
        VALUES (?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], ics_matrix_id))

for row in load_csv(ent_datasources_csv):
    cur.execute("""
        INSERT OR REPLACE INTO data_sources (id, stix_id, name, description, matrix_id)
        VALUES (?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], ent_matrix_id))

### ─── Assets ───
for row in load_csv(ics_assets_csv):
    cur.execute("""
        INSERT OR REPLACE INTO assets (id, stix_id, name, description, url)
        VALUES (?, ?, ?, ?, ?)
    """, (row["id"], row["STIX ID"], row["name"], row["description"], row["url"]))

# Commit changes
conn.commit()
conn.close()

print("✅ Database populated successfully.")
