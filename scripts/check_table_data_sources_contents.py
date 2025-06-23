from config import *

import sqlite3

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT id, name FROM data_sources ORDER BY name")
rows = cur.fetchall()

print("\n🧩 Current entries in data_sources table:\n")
for ds_id, name in rows:
    print(f"{ds_id} -> {name}")

conn.close()
