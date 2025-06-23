from config import *

# scripts/reset_and_populate_tool_deployment_context.py

import sqlite3

db_path = DB_PATH
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop and recreate table
cur.execute("DROP TABLE IF EXISTS tool_deployment_context")
cur.execute("""
    CREATE TABLE tool_deployment_context (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT NOT NULL,
        description TEXT,
        category TEXT CHECK(category IN ('Input', 'Output', 'Format', 'Hosting', 'Interface')) NOT NULL
    )
""")

entries = [
    # --- INPUTS ---
    ("Tool Input: STIX 2.1 Bundle", "Structured CTI ingestion format used by most threat intel platforms", "Input"),
    ("Tool Input: PCAP File", "Network packet capture used for protocol analysis or anomaly detection", "Input"),
    ("Tool Input: JSON File", "Generic structured input for configurations, logs, or indicators", "Input"),
    ("Tool Input: CSV File", "Tabular indicators, logs, or IOCs in a spreadsheet-compatible format", "Input"),
    ("Tool Input: PDF Report", "Narrative CTI or threat reports for parsing, summarizing, or entity extraction", "Input"),
    ("Tool Input: TXT File", "Unstructured logs or plaintext artifacts", "Input"),

    # --- OUTPUTS ---
    ("Tool Output: STIX 2.1 Bundle", "Enriched CTI output compatible with OpenCTI or MISP", "Output"),
    ("Tool Output: PDF Summary", "Formatted report of results, analytics, or emulation findings", "Output"),
    ("Tool Output: JSON File", "Structured output of enriched observables, configs, or logs", "Output"),
    ("Tool Output: CSV Export", "Human-readable structured report of tool results", "Output"),
    ("Tool Output: PCAP File", "Generated or filtered network captures for replay or analysis", "Output"),
    ("Tool Output: TXT Log", "Plain text logging of tool activity or scan results", "Output"),

    # --- FORMATS ---
    ("Format: STIX 2.1", "Structured Threat Intelligence format by OASIS used in CTI exchanges", "Format"),
    ("Format: JSON", "Standard structured data format for input/output between tools", "Format"),
    ("Format: CSV", "Comma-separated format used in logs, indicators, or observables", "Format"),
    ("Format: PDF", "Portable Document Format used for human-readable reports", "Format"),
    ("Format: TXT", "Raw plaintext format", "Format"),
    ("Format: PCAP", "Packet Capture file used for deep network inspection", "Format"),

    # --- HOSTING ENVIRONMENTS ---
    ("Hosted: Local CLI", "Runs as a command-line tool on analyst workstation or testbed", "Hosting"),
    ("Hosted: Cloud Service", "Accessible over the internet via secured portal or API", "Hosting"),
    ("Hosted: Containerized (Docker)", "Runs in a portable containerized environment", "Hosting"),
    ("Hosted: Virtual Machine", "Requires virtual appliance or VM image", "Hosting"),
    ("Hosted: SaaS Platform", "Subscription-based platform with hosted dashboard and services", "Hosting"),
    ("Hosted: Web Service Application", "Tool is deployed as a browser-accessible web service hosted internally or in the cloud", "Hosting"),
    ("Hosted: Local Application Executable", "Tool runs as a native GUI application installed on a local system", "Hosting"),

    # --- USER INTERFACE & INPUT TYPES ---
    ("User Input: CLI Prompt", "Tool requires user to provide input interactively via terminal", "Interface"),
    ("User Input: Form Fields (GUI)", "Tool provides form fields for entering observables, filters, or parameters", "Interface"),
    ("User Input: Drag-and-Drop Upload", "Allows analysts to upload artifacts via drag-and-drop (e.g., PCAPs, PDFs)", "Interface"),
    ("User Input: API Payload Configuration", "User manually structures JSON/STIX payloads to submit to the tool", "Interface"),
    ("User Input: File Path or Directory Selection", "Requires user to specify input file paths or scan directories", "Interface"),
    ("Interface: Web Dashboard", "Browser-based interface for search, configuration, and results visualization", "Interface"),
    ("Interface: REST API", "Tool exposes endpoints for integration with other systems", "Interface"),
    ("Interface: CLI Utility", "Command-line driven interface for automation and batch use", "Interface"),
]

for label, desc, cat in entries:
    cur.execute(
        "INSERT INTO tool_deployment_context (label, description, category) VALUES (?, ?, ?)",
        (label, desc, cat)
    )

conn.commit()
conn.close()

print("✅ tool_deployment_context table reset and updated with new hosting options.")
