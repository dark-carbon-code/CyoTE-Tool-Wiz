import csv
from pathlib import Path

CSV_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-targeted-assets.csv")

def check_csv_headers():
    print(f"📂 Checking headers for: {CSV_PATH}")
    try:
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            print("\n🧾 CSV Headers:")
            for i, header in enumerate(headers):
                print(f"  {i + 1}. {header}")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

if __name__ == "__main__":
    check_csv_headers()
