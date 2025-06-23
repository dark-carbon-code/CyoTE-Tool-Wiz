from config import *

import pandas as pd
import sqlite3
from collections import defaultdict

CSV_PATH = r"C:\Projects\cyote_tool_wiz\data\all_case_study_observables_w_d_notation_group_phase_terminal_final_v2.csv"
DB_PATH = rDB_PATH

def load_csv_case_techniques(path):
    df = pd.read_csv(path)
    df = df[df["case_id"].str.startswith("PAR")]  # Only PAR cases
    grouped = df.groupby("case_name")["tech_ics_id"].apply(lambda x: sorted(set(x))).to_dict()
    return grouped

def load_db_case_techniques(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT c.case_name, ct.tech_id
        FROM case_techniques ct
        JOIN cases c ON c.case_id = ct.case_id
        WHERE c.case_id LIKE 'PAR%'
    """)
    db_data = defaultdict(set)
    for case_name, tech_id in cur.fetchall():
        db_data[case_name].add(tech_id)
    conn.close()
    return {k: sorted(v) for k, v in db_data.items()}

def compare_technique_sets(csv_map, db_map):
    all_names = sorted(set(csv_map.keys()).union(db_map.keys()))
    for name in all_names:
        csv_set = set(csv_map.get(name, []))
        db_set = set(db_map.get(name, []))
        status = "✅ MATCH" if csv_set == db_set else "❌ MISMATCH"
        print(f"{name}:\n  - CSV ({len(csv_set)}): {sorted(csv_set)}\n  - DB  ({len(db_set)}): {sorted(db_set)}\n  → {status}\n")

if __name__ == "__main__":
    csv_techs = load_csv_case_techniques(CSV_PATH)
    db_techs = load_db_case_techniques(DB_PATH)
    compare_technique_sets(csv_techs, db_techs)
