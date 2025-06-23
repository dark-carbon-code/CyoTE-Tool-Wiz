import csv
from pathlib import Path

OBSERVABLES_FILE = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_clean.csv")
PROCEDURES_FILE = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.csv")

def append_data():
    # Read headers from both CSVs
    with PROCEDURES_FILE.open("r", encoding="utf-8-sig", newline="") as pfile:
        procedure_reader = csv.DictReader(pfile)
        procedure_fields = procedure_reader.fieldnames

    with OBSERVABLES_FILE.open("r", encoding="utf-8", newline="") as ofile:
        observable_reader = csv.DictReader(ofile)
        observable_fields = observable_reader.fieldnames

        # Check matching columns
        common_fields = [field for field in observable_fields if field in procedure_fields]
        if not common_fields:
            print("❌ No matching columns between files. Aborting.")
            return

        # Read all new data
        new_rows = [
            {field: row[field] for field in common_fields}
            for row in observable_reader
        ]

    # Append new data to the procedures CSV
    with PROCEDURES_FILE.open("a", encoding="utf-8", newline="") as pfile:
        writer = csv.DictWriter(pfile, fieldnames=procedure_fields)
        for row in new_rows:
            writer.writerow(row)

    print(f"✅ Appended {len(new_rows)} rows from observables to procedures.")
    print(f"📄 Updated file: {PROCEDURES_FILE}")

if __name__ == "__main__":
    append_data()
