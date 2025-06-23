import csv
from pathlib import Path

INPUT_PATH = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_normalized.csv")
OUTPUT_PATH = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_terminal_only.csv")

def filter_terminal_observables():
    with INPUT_PATH.open("r", encoding="utf-8", newline="") as infile, \
         OUTPUT_PATH.open("w", encoding="utf-8", newline="") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        count = 0
        for row in reader:
            if row.get("obs_terminal", "").strip().upper() == "TRUE":
                writer.writerow(row)
                count += 1

    print(f"✅ Saved {count} terminal observables to: {OUTPUT_PATH}")

if __name__ == "__main__":
    filter_terminal_observables()
