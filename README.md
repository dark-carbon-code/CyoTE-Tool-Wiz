# ☠ CyOTE Tool Wiz

> **Turn your cybersecurity tool into structured, machine-consumable knowledge aligned with CyOTE, MITRE ATT&CK, NIST CSF 2.0, and DOE resilience priorities.**

**CyOTE Tool Wiz** is an interactive CLI assistant developed by Idaho National Laboratory (INL) to help researchers, vendors, and security teams document OT/ICS tools using a structured, standards-aligned knowledge format. The resulting metadata can be used with LLM workflows, STIX pipelines, and threat hunting assistants.

---

## ✨ Key Features

- 🧭 **Interactive CLI Wizard** for tool profiling
- 🧠 **MITRE ATT&CK (ICS & Enterprise)** tactic-technique mapping
- 📡 **Observable type selection** (Host, Network, External Effects)
- 🧾 **CyOTE-aligned metadata** structure with live previews
- 🧰 **Use case alignment** with NIST CSF 2.0 (Function → Category → Subcategory → Example)
- 🛰 **Deployment context selection** including DOE TRL, interfaces, I/O types
- 📦 **Structured output**: JSON and SQLite (`tool_knowledge.db`)
- 🧑‍💼 **User role mapping** with optional NICE Framework linkage

---

## 🖥️ CLI Preview

Run the CLI using:

```bash
python cli.py
````

You’ll be greeted with:

```
 ██████╗██╗   ██╗ ██████╗ ████████╗███████╗
██╔════╝╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██╔════╝
██║      ╚████╔╝ ██║   ██║   ██║   █████╗
██║       ╚██╔╝  ██║   ██║   ██║   ██╔══╝
╚██████╗   ██║   ╚██████╔╝   ██║   ███████╗
 ╚═════╝   ╚═╝    ╚═════╝    ╚═╝   ╚══════╝

            ☠ CYOTE TOOL WIZ ☠

Turn your tool into a knowledge file
that can be used with LLM and agentic workflows

? 🔧 CYOTE TOOL WIZ - Choose an action:
❯ 🛠 Create a new tool entry
  🔁 Update an existing tool entry
  ❌ Exit
```

---

## 📂 Project Structure

```
cyote_tool_wiz/
├── cli.py                      # Entry point CLI launcher
├── wizard/                    # Core CLI workflows
├── tools/                     # Archived versions of the CLI wizard
├── utils/                     # NICE-CSF mappers, deployment context helpers
├── scripts/                   # Data validators, importers, fixers
├── data/                      # Input CSVs, JSON templates, output JSON
├── notebooks/                 # Jupyter analysis and prototype flows
├── schema/                    # JSON schema(s) for tool entries
├── requirements.txt           # Python package dependencies
```

---

## ⚙️ Setup

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

Recommended: Python 3.10+

---

## 🚀 Using the Tool Wizard

### Create a new tool entry

```bash
python cli.py
```

You’ll walk through:

* 🔐 MITRE Matrix → Tactics → Techniques
* 💾 Data sources → Observable types
* 🧭 CSF use case explorer (Function → Category → Example)
* 📡 Deployment context: TRL, interfaces, I/O types
* 🧠 Roles, GitHub links, Fact Sheets, Real-world usage

At the end, output is saved to:

* `data/tool_capabilities/<tool_name>_<timestamp>.json`
* Inserted into `data/tool_knowledge.db`

---

## 🧪 Example Output

Here’s a trimmed sample of the output JSON:

```json
{
  "name": "CyOTE Catch",
  "description": "Real-time network detection based on ICS patterns",
  "matrix": "ICS",
  "tactics": ["Initial Access", "Command and Control"],
  "techniques": [
    {"id": "T0801", "name": "Drive-by Compromise"}
  ],
  "observable_types": [
    {"name": "Unusual Network Connection", "category": "Network"}
  ],
  "csf_use_cases": [
    {
      "function": "DETECT",
      "category": "Security Continuous Monitoring",
      "description": "Detect anomalous activity..."
    }
  ],
  "deployment_context": {
    "TRL": "TRL 6 – Prototype demonstrated in relevant environment",
    "input_types": ["Packet Capture", "Syslog"],
    "output_types": ["Alert JSON", "Dashboard View"]
  }
}
```

---

## 📚 Reference Datasets

This project uses authoritative standards and mappings:

* **MITRE ATT\&CK v17.1** (ICS + Enterprise)
* **CyOTE Observable Types** (Host, Network, External Effects)
* **NIST CSF 2.0** full function-category-subcategory-example hierarchy
* **DOE TRL levels** and operational deployment metadata
* **NICE Work Roles** (optional enrichment layer)

Included source files:

* `enterprise-attack-v17.1-*.csv`
* `ics-attack-v17.1-*.csv`
* `csf-export.json`, `v2_nf_components.json`
* `trl_doe.json`, `observable_types_descriptions_filled.csv`

---

## 🧠 CyOTE Methodology

Learn more about the CyOTE framework and methodology here:
🔗 [https://inl.gov/cyote](https://inl.gov/cyote)

---

## 🤝 Contributing

Contributions welcome!
Please open an Issue or submit a Pull Request.

For lab-to-lab collaboration, contact:
📧 `cyote@inl.gov`

---

## 📜 License

This project is licensed under the MIT License.
See [`LICENSE`](LICENSE) for details.

---

> *Developed by Idaho National Laboratory (INL) for critical infrastructure defenders, utilities, vendors, and the DOE Grid Deployment Office.*


