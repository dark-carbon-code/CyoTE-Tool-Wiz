import pandas as pd
from pathlib import Path

# File path
observables_path = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_clean.csv")

# Load CSV
df = pd.read_csv(observables_path)

# Total number of entries in the column
total_descriptions = df['case_description'].shape[0]

# Number of unique descriptions
unique_descriptions = df['case_description'].nunique()

# Print results
print(f"📄 Total `case_description` entries: {total_descriptions}")
print(f"🔢 Unique `case_description` entries: {unique_descriptions}")
