from config import *

import sqlite3
import csv

DB_PATH = DB_PATH
OUTPUT_CSV = "C:/Projects/cyote_tool_wiz/data/observable_types_descriptions_template.csv"

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, name, category FROM observable_types ORDER BY id")
    rows = cur.fetchall()

    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "description"])
        for row in rows:
            writer.writerow([row[0], row[1], row[2], ""])  # blank description for user input

    print(f"✅ Template CSV saved to: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
