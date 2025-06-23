from config import *

import sqlite3
from rich import print

# Path to your SQLite database
db_path = DB_PATH

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check table structure
print("[bold blue]📋 Columns in tool_deployment_context table:[/bold blue]\n")
cursor.execute("PRAGMA table_info(tool_deployment_context)")
columns = cursor.fetchall()
for col in columns:
    print(f" - {col[1]} ({col[2]})")

# Check table contents
print("\n[bold green]📄 Entries in tool_deployment_context:[/bold green]\n")
cursor.execute("SELECT id, category, description FROM tool_deployment_context")
rows = cursor.fetchall()
for row in rows:
    print(f"[{row[0]}] {row[1]} → {row[2]}")

print(f"\n📊 Total rows: {len(rows)}")

# Clean up
cursor.close()
conn.close()
