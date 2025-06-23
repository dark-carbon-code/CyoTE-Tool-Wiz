from config import *

import sqlite3
from rich import print
from rich.table import Table
from pathlib import Path

DB_PATH = Path(DB_PATH)

def check_table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def print_table_schema(cursor, table_name):
    print(f"\n[bold cyan]📑 Schema for '{table_name}' table:[/bold cyan]")
    cursor.execute(f"PRAGMA table_info({table_name})")
    schema = cursor.fetchall()

    if not schema:
        print(f"[red]❌ Failed to retrieve schema for table '{table_name}'.[/red]")
        return

    schema_table = Table(title=f"{table_name} Schema", show_lines=True)
    schema_table.add_column("CID", style="dim", width=4)
    schema_table.add_column("Column Name")
    schema_table.add_column("Data Type")
    schema_table.add_column("Not Null")
    schema_table.add_column("Default Value")
    schema_table.add_column("Primary Key")

    for col in schema:
        schema_table.add_row(
            str(col[0]), col[1], col[2], str(bool(col[3])), str(col[4]) if col[4] is not None else "NULL", str(col[5])
        )
    print(schema_table)

def print_sample_rows(cursor, table_name, limit=5):
    print(f"\n[bold cyan]📦 Sample rows from '{table_name}' (limit {limit}):[/bold cyan]")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
    rows = cursor.fetchall()

    if not rows:
        print("[yellow]⚠️ No rows found in this table.[/yellow]")
        return

    columns = rows[0].keys()
    table = Table(show_lines=True, title=f"{table_name} Preview")
    for col in columns:
        table.add_column(col, overflow="fold")

    for row in rows:
        table.add_row(*(str(row[col]) if row[col] is not None else "NULL" for col in columns))

    print(table)

def print_row_count(cursor, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"[green]🔢 Total rows in '{table_name}':[/green] {count}")

def list_all_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]
    print(f"\n[bold cyan]📚 All tables in database:[/bold cyan] {tables}")
    return tables

def main():
    if not DB_PATH.exists():
        print(f"[bold red]❌ Database file not found at:[/bold red] {DB_PATH}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        list_all_tables(cur)

        table_name = "use_cases"
        if not check_table_exists(cur, table_name):
            print(f"[bold red]❌ Table '{table_name}' does not exist in the database.[/bold red]")
            return

        print_table_schema(cur, table_name)
        print_row_count(cur, table_name)
        print_sample_rows(cur, table_name, limit=10)

if __name__ == "__main__":
    main()
