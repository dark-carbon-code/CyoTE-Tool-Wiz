from config import TOOL_CAPABILITIES_DIR as TOOL_DIR, CHUNKS_DIR
import json
import uuid
from pathlib import Path
from rich import print
from datetime import datetime

def extract_chunks_for_rag(tool_json):
    """Extract structured text chunks from a tool JSON entry."""
    chunks = []
    tool_name = tool_json.get("tool_name", "Unknown Tool")

    # Basic tool description
    if (desc := tool_json.get("description", "")):
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "description",
            "content": f"[Tool Name]\n{tool_name}\n\n[Description]\n{desc}"
        })

    for role in tool_json.get("user_roles", []):
        role_text = f"- {role.get('name', '[Unnamed Role]')}: {role.get('description', '[No description]')}"
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "user_roles",
            "content": f"[User Role]\n{role_text}"
        })

    for tech in tool_json.get("techniques_supported", []):
        tech_text = f"{tech.get('id', '[No ID]')} - {tech.get('name', '[Unnamed Technique]')}\n{tech.get('description', '[No description]')}"
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "techniques_supported",
            "content": f"[Technique]\n{tech_text}"
        })

    for ds in tool_json.get("data_sources", []):
        components = "\n".join(
            f"  • {comp.get('name')}: {comp.get('description', '')}"
            for comp in ds.get("components", [])
        )
        ds_text = f"{ds.get('name')}: {ds.get('description', '')}\n{components}"
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "data_sources",
            "content": f"[Data Source]\n{ds_text}"
        })

    for obs in tool_json.get("observable_types", []):
        obs_text = f"- {obs.get('name')} ({obs.get('category')}): {obs.get('description', '[No description]')}"
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "observable_types",
            "content": f"[Observable Type]\n{obs_text}"
        })

    for uc in tool_json.get("use_cases", []):
        subcat = json.loads(uc["subcategories_json"]) if isinstance(uc.get("subcategories_json"), str) else uc.get("subcategories_json", [])
        examples = json.loads(uc["examples_json"]) if isinstance(uc.get("examples_json"), str) else uc.get("examples_json", [])

        uc_text = f"{uc.get('csf_function_id', '')} - {uc.get('name', '[Unnamed Use Case]')}\n{uc.get('description', '[No description]')}"
        if subcat:
            uc_text += "\n\n[Subcategories]\n" + "\n".join(f"- {s.get('title', '')}: {s.get('description', '')}" for s in subcat)
        if examples:
            uc_text += "\n\n[Examples]\n" + "\n".join(
                f"- {e.get('title', '')}: {e.get('description', '')}" if isinstance(e, dict) else f"- {e}" for e in examples
            )

        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "use_cases",
            "content": f"[Use Case]\n{uc_text}"
        })

    for section, items in tool_json.get("deployment_context", {}).items():
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    text = f"{item.get('label', item.get('name', '[Unnamed]'))}\n{item.get('description', '')}"
                    if item.get("note"):
                        text += f"\n➤ Note: {item['note']}"
                    chunks.append({
                        "id": str(uuid.uuid4()),
                        "tool_name": tool_name,
                        "section": section,
                        "content": f"[{section.replace('_', ' ').title()}]\n{text}"
                    })

    if (example_text := tool_json.get("example_usage")):
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "example_usage",
            "content": f"[Example Usage]\n{example_text}"
        })

    if (github := tool_json.get("github")):
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "github",
            "content": f"[GitHub]\n{github}"
        })

    if (factsheet := tool_json.get("factsheet")):
        chunks.append({
            "id": str(uuid.uuid4()),
            "tool_name": tool_name,
            "section": "factsheet",
            "content": f"[Fact Sheet]\n{factsheet}"
        })

    return chunks

def chunk_tool_to_jsonl(input_file):
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        tool_json = json.load(f)

    base_name = input_file.stem
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    out_file = CHUNKS_DIR / f"{base_name}__{timestamp}_chunks.jsonl"

    chunks = extract_chunks(tool_json)
    with open(out_file, "w", encoding="utf-8") as chunk_file:
        for chunk in chunks:
            chunk_file.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"[green]✔ Chunked (JSONL): {base_name} → {out_file.name}[/green]")

def process_all_tools():
    tool_files = sorted(TOOL_DIR.glob("*.json"))
    if not tool_files:
        print("[yellow]⚠ No tool JSON files found in TOOL_DIR[/yellow]")
        return

    for f in tool_files:
        chunk_tool_to_jsonl(f)

if __name__ == "__main__":
    process_all_tools()
