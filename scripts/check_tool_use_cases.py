from config import *

import sqlite3

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("PRAGMA table_info(tool_use_cases)")
columns = cur.fetchall()

print("📋 Columns in tool_use_cases table:\n")
for col in columns:
    print(f" - {col[1]}")

conn.close()
