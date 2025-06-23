import pandas as pd
from pathlib import Path

# Path to the CSV file
csv_path = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-datasources.csv")

# Load CSV with proper encoding
df = pd.read_csv(csv_path, encoding="cp1252", dtype=str)

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Drop rows with missing 'id' or 'name'
df = df.dropna(subset=["id", "name"])

# Remove duplicates and sort
df = df.drop_duplicates(subset=["id", "name"]).sort_values(by="id")

# Print each entry
print("\n📋 Data Sources from CSV:\n")
for _, row in df.iterrows():
    print(f"{row['id']} -> {row['name']}")

# Print summary
print(f"\n📊 Total unique data sources: {len(df)}")
