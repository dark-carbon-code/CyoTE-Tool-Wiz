from config import *

import sqlite3

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("PRAGMA table_info(tools)")
for row in cur.fetchall():
    print(row)
