import csv
from pathlib import Path
import unicodedata

OBS_PATH = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_clean.csv")
PROC_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.csv")
OUTPUT_PATH = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.enriched.csv")

def normalize(text):
    if not text:
        return ""
    return unicodedata.normalize("NFKD", text).strip().lower().replace("\u200b", "").replace("\ufeff", "")

def load_observable_descriptions():
    desc_map = {}
    with OBS_PATH.open("r", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = normalize(row.get("case_id"))
            cname = normalize(row.get("case_name"))
            desc = row.get("case_description", "").strip()
            if cid and cname and desc:
                desc_map[(cid, cname)] = desc
    return desc_map

def enrich_procedures(desc_map):
    updated = 0
    unmatched_keys = []

    with PROC_PATH.open("r", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    for row in rows:
        cid = normalize(row.get("case_id"))
        cname = normalize(row.get("case_name"))
        key = (cid, cname)

        if cid.startswith("par"):
            if not row.get("case_description") and key in desc_map:
                row["case_description"] = desc_map[key]
                updated += 1
            elif not row.get("case_description") and key not in desc_map:
                unmatched_keys.append((cid, cname))

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Enriched {updated} PAR entries with case descriptions.")
    print(f"💾 Output written to: {OUTPUT_PATH}")
    if unmatched_keys:
        print(f"⚠️ {len(unmatched_keys)} PAR entries could not be matched. Sample:")
        for cid, cname in unmatched_keys[:5]:
            print(f" - {cid} | {cname}")

if __name__ == "__main__":
    print("🔄 Enriching PAR entries with case descriptions...")
    descs = load_observable_descriptions()
    enrich_procedures(descs)
