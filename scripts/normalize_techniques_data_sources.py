import pandas as pd
from pathlib import Path

# File paths
techniques_file = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques.csv")
output_file = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques_data_sources.csv")

# Load CSV using cp1252 to avoid UTF-8 decoding errors
techniques_df = pd.read_csv(techniques_file, encoding="cp1252")

# Determine the technique ID column name
if "id" in techniques_df.columns:
    id_column = "id"
elif "ID" in techniques_df.columns:
    id_column = "ID"
else:
    raise ValueError("❌ Cannot find a technique ID column in the CSV.")

# Set default for techniques with no data sources
fallback_data_source = "External Effects: Human Observation Needed"

# Normalize the mapping
normalized_technique_datasources = []

for _, row in techniques_df.iterrows():
    technique_id = row[id_column]
    raw_sources = row.get("data sources", "")

    if pd.isna(raw_sources) or raw_sources.strip() == "":
        normalized_technique_datasources.append((technique_id, fallback_data_source))
        continue

    for source in raw_sources.split(","):
        cleaned_source = source.strip()
        if cleaned_source:
            normalized_technique_datasources.append((technique_id, cleaned_source))

# Remove duplicates
normalized_technique_datasources = sorted(set(normalized_technique_datasources))

# Output to CSV
output_df = pd.DataFrame(normalized_technique_datasources, columns=["technique_id", "data_source"])
output_df.to_csv(output_file, index=False, encoding="utf-8")

# Print results
print("\n✅ Normalized Technique → Data Source Mappings:\n")
for technique_id, data_source in normalized_technique_datasources:
    print(f"{technique_id} -> {data_source}")

# Final count summary
print(f"\n📊 Total unique Technique → Data Source relationships: {len(normalized_technique_datasources)}")
print(f"📝 Output written to: {output_file}")
