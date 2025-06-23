from config import *

import sqlite3
from pathlib import Path

# Path to the SQLite database
db_path = Path(__file__).resolve().parent.parent / "data" / DB_PATH
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Define tactic-to-technique mappings
tactic_technique_map = {
    "TA0102": [  # Discovery
        "T0840",  # Network Connection Enumeration
        "T0842",  # Network Sniffing
        "T0846",  # Remote System Discovery
        "T0888",  # Remote System Information Discovery
        "T0887"   # Wireless Sniffing
    ],
    "TA0103": [  # Evasion
        "T0858", "T0820", "T0872", "T0849", "T0851", "T0856", "T0894"
    ],
    "TA0111": [  # Privilege Escalation
        "T0890", "T0874"
    ],
    "TA0110": [  # Persistence
        "T0891", "T0889", "T0839", "T0873", "T0857", "T0859"
    ],
    "TA0104": [  # Execution
        "T0895", "T0858", "T0807", "T0871", "T0823", "T0874", "T0821",
        "T0834", "T0853", "T0863"
    ],
    "TA0108": [  # Initial Access
        "T0817", "T0819", "T0866", "T0822", "T0883", "T0886", "T0847",
        "T0848", "T0865", "T0862", "T0864", "T0860"
    ],
    "TA0105": [  # Impact
        "T0879", 
        "T0813", 
        "T0815",
        "T0826",
        "T0827",
        "T0828",
        "T0837",
        "T0880",
        "T0829",
        "T0831",
        "T0832",
        "T0882"
    ],
    "TA0106": [  # Impair Process Control
        "T0806",  # Brute Force I/O
        "T0836",  # Modify Parameter
        "T0839",  # Module Firmware
        "T0856",  # Spoof Reporting Message
        "T0855",  # Unauthorized Command Message
    ],
    "TA0107": [  # Inhibit Response Function
        "T0800",  # Activate Firmware Update Mode
        "T0878",  # Alarm Suppression
        "T0803",  # Block Command Message
        "T0804",  # Block Reporting Message
        "T0805",  # Block Serial COM
        "T0892",  # Change Credential
        "T0809",  # Data Destruction
        "T0814",  # Denial of Service
        "T0816",  # Device Restart/Shutdown
        "T0835",  # Manipulate I/O Image
        "T0838",  # Modify Alarm Settings
        "T0851",  # Rootkit
        "T0881",  # Service Stop
        "T0857",  # System Firmware
    ],
    "TA0100": [  # Collection
        "T0830",  # Adversary-in-the-Middle
        "T0802",  # Automated Collection
        "T0811",  # Data from Information Repositories
        "T0893",  # Data from Local System
        "T0868",  # Detect Operating Mode
        "T0877",  # I/O Image
        "T0801",  # Monitor Process State
        "T0861",  # Point & Tag Identification
        "T0845",  # Program Upload
        "T0852",  # Screen Capture
        "T0887",  # Wireless Sniffing
    ],
    "TA0101": [  # Command and Control
        "T0885",
        "T0884",
        "T0869"
    ],
    "TA0109": [ # Lateral Movement
        "T0812",
        "T0866",
        "T0891",
        "T0867",
        "T0843",
        "T0886",
        "T0859"
    ]
}

# Insert mappings
insert_count = 0
for tactic_id, technique_ids in tactic_technique_map.items():
    for technique_id in technique_ids:
        cur.execute("""
            INSERT OR IGNORE INTO technique_tactics (technique_id, tactic_id)
            VALUES (?, ?)
        """, (technique_id, tactic_id))
        insert_count += 1

conn.commit()
conn.close()

print(f"✅ Successfully inserted {insert_count} technique-tactic mappings.")
