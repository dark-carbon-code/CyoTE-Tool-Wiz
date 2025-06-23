import csv
from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables.csv")
OUTPUT_PATH = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_normalized.csv")

def normalize_case_ids():
    case_name_to_id = {}
    next_id = 1

    with INPUT_PATH.open(mode="r", encoding="utf-8-sig", newline='') as infile, \
         OUTPUT_PATH.open(mode="w", encoding="utf-8", newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            case_name = row["case_name"].strip()
            if case_name not in case_name_to_id:
                case_name_to_id[case_name] = f"PAR{next_id:03}"
                next_id += 1
            row["case_id"] = case_name_to_id[case_name]
            writer.writerow(row)

    print(f"✅ Normalized case_ids and saved to: {OUTPUT_PATH}")
    print(f"🔢 Unique cases found: {len(case_name_to_id)}")

if __name__ == "__main__":
    normalize_case_ids()
