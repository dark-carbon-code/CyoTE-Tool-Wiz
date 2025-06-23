import csv
from pathlib import Path

INPUT_FILE = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_terminal_only.csv")
OUTPUT_FILE = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_clean.csv")
COLUMNS_TO_DROP = {"case_alias", "obs_terminal"}

def drop_columns():
    with INPUT_FILE.open("r", encoding="utf-8", newline="") as infile, \
         OUTPUT_FILE.open("w", encoding="utf-8", newline="") as outfile:

        reader = csv.DictReader(infile)
        output_fields = [f for f in reader.fieldnames if f not in COLUMNS_TO_DROP]

        writer = csv.DictWriter(outfile, fieldnames=output_fields)
        writer.writeheader()

        for row in reader:
            cleaned_row = {k: v for k, v in row.items() if k in output_fields}
            writer.writerow(cleaned_row)

    print(f"✅ Columns dropped: {', '.join(COLUMNS_TO_DROP)}")
    print(f"📁 Cleaned file saved as: {OUTPUT_FILE}")

if __name__ == "__main__":
    drop_columns()
