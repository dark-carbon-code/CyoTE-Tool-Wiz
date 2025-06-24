from config import CHUNKS_DIR, TOOL_CAPABILITIES_DIR
import os
import json
from datetime import datetime
from rich import print
from pathlib import Path
from utils.chunker import extract_chunks_for_rag
import ast

TOOL_DIR = TOOL_CAPABILITIES_DIR

def ensure_directory_exists():
    TOOL_DIR.mkdir(parents=True, exist_ok=True)

def save_tool_json(entry, file_name=None):
    """
    Save a tool entry as a JSON file and generate RAG chunks.
    """
    ensure_directory_exists()

    clean_entry = convert_stringified_lists(entry)
    normalized_entry = normalize_labels(clean_entry)

    if file_name:
        filename = file_name
    else:
        sanitized_name = normalized_entry['tool_name'].replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{sanitized_name}_{timestamp}.json"

    file_path = TOOL_DIR / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(normalized_entry, f, indent=2, ensure_ascii=False)

    print(f"[green]✔ Saved to: {file_path}[/green]")

    # Create chunks for RAG
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    chunks = extract_chunks_for_rag(entry)

    chunk_file = CHUNKS_DIR / filename.replace(".json", ".jsonl")
    with open(chunk_file, 'w', encoding='utf-8') as cf:
        for chunk in chunks:
            json.dump(chunk, cf)
            cf.write('\n')

    print(f"[blue]✔ Chunks saved to: {chunk_file}[/blue]")

    return filename

def get_tool_files():
    ensure_directory_exists()
    return sorted([f.name for f in TOOL_DIR.glob("*.json")])

def load_tool_json(filename):
    file_path = TOOL_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_observable_types(tactic_descriptions, technique_descriptions, data_source_descriptions):
    """
    Heuristically classify observable categories.
    """
    obs_types = set()

    def classify(text):
        text = text.lower()
        if any(k in text for k in ["log", "sysmon", "event", "registry", "process", "file", "memory", "command", "powershell", "execution"]):
            return "Host"
        elif any(k in text for k in ["packet", "network", "flow", "tcp", "udp", "dns", "snmp", "modbus", "ethernet"]):
            return "Network"
        elif any(k in text for k in ["effect", "impact", "outage", "latency", "pressure", "valve", "response function", "set point", "safety"]):
            return "External Effects"
        return None

    for desc in tactic_descriptions + technique_descriptions + data_source_descriptions:
        category = classify(desc)
        if category:
            obs_types.add(category)

    return sorted(obs_types)

def convert_stringified_lists(obj):
    if isinstance(obj, dict):
        return {k: convert_stringified_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_stringified_lists(v) for v in obj]
    elif isinstance(obj, str):
        try:
            val = ast.literal_eval(obj)
            if isinstance(val, list):
                return [convert_stringified_lists(i) for i in val]
        except (ValueError, SyntaxError):
            pass
        return obj
    else:
        return obj

def normalize_labels(obj):
    if isinstance(obj, dict):
        return {("label" if k == "name" else k): normalize_labels(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [normalize_labels(i) for i in obj]
    return obj

def save_chunks_for_tool(tool_entry, file_name):
    """
    Standalone method to extract and save chunks from a given tool entry JSON
    (used in interactive_create after tool JSON is saved).
    """
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

    chunks = extract_chunks_for_rag(tool_entry)
    base_name = Path(file_name).stem
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    out_file = CHUNKS_DIR / f"{base_name}__{timestamp}_chunks.jsonl"

    with open(out_file, "w", encoding="utf-8") as f:
        for chunk in chunks:
            json.dump(chunk, f, ensure_ascii=False)
            f.write("\n")

    print(f"[green]✔ Extracted {len(chunks)} chunks to: {out_file.name}[/green]")

def generate_empty_tool_template():
    return {
        "tool_name": "",
        "description": "",
        "user_roles": [],
        "tactics_supported": [],
        "techniques_supported": [],
        "data_sources": [],
        "observable_types": [],
        "use_cases": [],
        "deployment_context": {
            "trl": {
                "level": "",
                "description": "",
                "commercial_viable": False,
                "commercial_viable_label": ""
            },
            "hosting_env": [],
            "interfaces": [],
            "access_methods": [],
            "input_types": [],
            "output_types": [],
            "import_formats": [],
            "export_formats": []
        },
        "targeted_assets": [],
        "related_cases": [],
        "example_usage": "",
        "github": "",
        "factsheet": ""
    }
