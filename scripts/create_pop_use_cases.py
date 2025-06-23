from config import *

import sqlite3
import json
from pathlib import Path

# === Config ===
CSF_JSON_PATH = Path("C:/Projects/cyote_tool_wiz/data/csf-export.json")
DB_PATH = Path(DB_PATH)

# === Load CSF 2.0 Elements ===
with CSF_JSON_PATH.open("r", encoding="utf-8") as f:
    elements = json.load(f)["response"]["elements"]["elements"]

# === Parse Elements ===
functions = {}
categories = {}
subcategories = {}

for el in elements:
    el_type = el["element_type"]
    el_id = el["element_identifier"]
    title = el.get("title", "").strip()
    text = el.get("text", "").strip()

    if el_type == "function":
        functions[el_id] = {"title": title, "text": text}

    elif el_type == "category":
        categories[el_id] = {
            "title": title,
            "text": text,
            "function": el_id.split(".")[0],
            "subcategories": []
        }

    elif el_type == "subcategory":
        subcategories[el_id] = {
            "title": title,
            "text": text,
            "category": el_id.split("-")[0],
            "examples": []
        }

    elif el_type == "implementation_example":
        sid = ".".join(el_id.split(".")[:2])  # maps to subcategory
        if sid not in subcategories:
            subcategories[sid] = {
                "title": "",
                "text": "",
                "category": sid.split("-")[0],
                "examples": []
            }
        subcategories[sid]["examples"].append({
            "id": el_id,
            "title": title,
            "text": text
        })

# Link subcategories to categories
for sid, sdata in subcategories.items():
    cat_id = sdata["category"]
    if cat_id in categories:
        categories[cat_id]["subcategories"].append(sid)

# === Generate use case entries ===
use_cases = []
uid = 1
for cat_id, cat in categories.items():
    fn_id = cat["function"]
    fn_title = functions.get(fn_id, {}).get("title", fn_id)
    full_name = f"{fn_title}: {cat['title']}"
    description = cat["text"]

    sub_json = []
    ex_json = []

    for sid in sorted(cat["subcategories"]):
        sub = subcategories[sid]
        sub_json.append({
            "id": sid,
            "title": sub["title"],
            "text": sub["text"]
        })
        for ex in sub["examples"]:
            ex_json.append({
                "subcategory_id": sid,
                "example_id": ex["id"],
                "text": ex["text"]
            })

    use_cases.append((
        uid,
        full_name,
        cat_id,
        fn_id,
        description,
        json.dumps(sub_json, ensure_ascii=False),
        json.dumps(ex_json, ensure_ascii=False)
    ))
    uid += 1

# === Create or Replace use_cases Table ===
with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()

    # Drop and recreate the table
    cur.execute("DROP TABLE IF EXISTS use_cases")
    cur.execute("""
        CREATE TABLE use_cases (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            csf_category_id TEXT,
            csf_function_id TEXT,
            description TEXT,
            subcategories_json TEXT,
            examples_json TEXT
        );
    """)

    # Populate it
    cur.executemany("""
        INSERT INTO use_cases (
            id, name, csf_category_id, csf_function_id,
            description, subcategories_json, examples_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, use_cases)

    conn.commit()

print(f"✅ Populated use_cases table with {len(use_cases)} entries from CSF 2.0.")
