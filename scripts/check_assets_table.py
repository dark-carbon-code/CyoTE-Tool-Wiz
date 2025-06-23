from config import *

import sqlite3
from rich import print

DB_PATH = DB_PATH

def check_assets_table():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Print schema
        print("[bold green]📦 Schema for 'assets' table:[/bold green]")
        cur.execute("PRAGMA table_info(assets)")
        for col in cur.fetchall():
            print(col)

        # Print contents
        print("\n[bold blue]📄 Contents of 'assets' table:[/bold blue]")
        cur.execute("SELECT id, name, description FROM assets ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(f"[{row[0]}] {row[1]} - {row[2] or 'No description'}")

if __name__ == "__main__":
    check_assets_table()
