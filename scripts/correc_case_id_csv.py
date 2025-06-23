from config import *

import pandas as pd
import sqlite3

# File paths
CSV_PATH = r"C:\Projects\cyote_tool_wiz\data\all_case_study_observables_w_d_notation_group_phase_terminal_final_v2.csv"
DB_PATH = rDB_PATH
OUTPUT_PATH = r"C:\Projects\cyote_tool_wiz\data\all_case_study_observables_corrected.csv"

# Load original CSV
csv_df = pd.read_csv(CSV_PATH)

# Connect to DB and load cases table
conn = sqlite3.connect(DB_PATH)
db_cases = pd.read_sql_query("SELECT case_id, case_name FROM cases", conn)
conn.close()

# Merge to get correct case_id from DB using case_name
merged_df = csv_df.drop(columns=['case_id']).merge(db_cases, on='case_name', how='left')

# Reorder columns to place case_id first (optional)
cols = ['case_id'] + [col for col in merged_df.columns if col != 'case_id']
merged_df = merged_df[cols]

# Save corrected CSV
merged_df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Corrected CSV saved to: {OUTPUT_PATH}")
