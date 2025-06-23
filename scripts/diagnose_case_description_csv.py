import csv
from pathlib import Path

OBS_CSV = Path("C:/Projects/cyote_tool_wiz/data/cyote_par_observerables_clean.csv")
PROCEDURES_CSV = Path("C:/Projects/cyote_tool_wiz/data/ics-attack-v17.1-techniques-procedure-example.csv")

def normalize(text):
    return text.strip().lower().replace("\u200b", "") if text else ""

def get_keys_from_csv(path):
    keys = set()
    with path.open("r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = normalize(row.get("case_id"))
            cname = normalize(row.get("case_name"))
            if cid and cname:
                keys.add((cid, cname))
    return keys

def main():
    obs_keys = get_keys_from_csv(OBS_CSV)
    proc_keys = get_keys_from_csv(PROCEDURES_CSV)

    unmatched_proc = proc_keys - obs_keys
    unmatched_obs = obs_keys - proc_keys

    print(f"\n🧪 [Diagnostics] Comparison of case_id + case_name keys:\n")
    print(f"✅ In observables only: {len(unmatched_obs)} entries")
    for cid, cname in sorted(unmatched_obs):
        print(f"  OBS only: {cid} | {cname}")
    print(f"\n❌ In procedures only: {len(unmatched_proc)} entries")
    for cid, cname in sorted(unmatched_proc):
        print(f"  PROC only: {cid} | {cname}")

if __name__ == "__main__":
    main()
