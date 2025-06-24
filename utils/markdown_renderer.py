# utils/markdown_renderer.py

import hashlib
import json
from datetime import datetime
from pathlib import Path

def summarize_text(text: str, max_len: int = 300) -> str:
    text = text.strip().replace("\n", " ")
    return text[:max_len] + "..." if len(text) > max_len else text

def render_markdown_sections(tool: dict) -> dict:
    """Render all major sections of a tool entry into a dict of {section_name: markdown_str}"""
    sections = {}

    # Description
    if tool.get("description"):
        sections["description"] = f"# Description\n\n{tool['description']}"

    # Example Usage
    if tool.get("example_usage"):
        sections["example_usage"] = f"# Example Usage\n\n{tool['example_usage']}"

    # GitHub
    if tool.get("github"):
        sections["github"] = f"# GitHub Repository\n\n{tool['github']}"

    # Fact Sheet
    if tool.get("factsheet"):
        sections["factsheet"] = f"# Fact Sheet\n\n{tool['factsheet']}"

    # User Roles
    if tool.get("user_roles"):
        lines = ["# User Roles"]
        for role in tool["user_roles"]:
            lines.append(f"\n## {role.get('label', '')}")
            lines.append(role.get("description", ""))
            if role.get("nice_roles"):
                for nice in role["nice_roles"]:
                    lines.append(f"\n### {nice.get('title', '').strip()}")
                    lines.append(nice.get("description", ""))
                    if nice.get("tasks"):
                        lines.append("**Tasks:**\n" + "\n".join(f"- {t}" for t in nice["tasks"]))
                    if nice.get("knowledge"):
                        lines.append("**Knowledge Areas:**\n" + "\n".join(f"- {k}" for k in nice["knowledge"][:20]) + "\n...")
                    if nice.get("skills"):
                        lines.append("**Skills:**\n" + "\n".join(f"- {s}" for s in nice["skills"][:20]) + "\n...")
        sections["user_roles"] = "\n\n".join(lines)

    # Tactics
    if tool.get("tactics_supported"):
        lines = ["# ATT&CK Tactics"] + [f"- {t}" for t in tool["tactics_supported"]]
        sections["tactics_supported"] = "\n".join(lines)

    # Techniques
    if tool.get("techniques_supported"):
        lines = ["# ATT&CK Techniques"]
        for t in tool["techniques_supported"]:
            lines.append(f"## {t.get('id')} - {t.get('label')}")
            lines.append(t.get("description", ""))
        sections["techniques_supported"] = "\n\n".join(lines)

    # Data Sources
    if tool.get("data_sources"):
        lines = ["# Data Sources"]
        for ds in tool["data_sources"]:
            lines.append(f"## {ds.get('id')} - {ds.get('label')}")
            lines.append(ds.get("description", ""))
            for comp in ds.get("components", []):
                lines.append(f"### Component: {comp.get('label')}")
                lines.append(comp.get("description", ""))
        sections["data_sources"] = "\n\n".join(lines)

    # Observable Types
    if tool.get("observable_types"):
        lines = ["# Observable Types"]
        for obs in tool["observable_types"]:
            lines.append(f"## {obs.get('label')} ({obs.get('category')})")
            lines.append(obs.get("description", ""))
        sections["observable_types"] = "\n\n".join(lines)

    # CSF Use Cases
    if tool.get("use_cases"):
        lines = ["# CSF 2.0 Use Cases"]
        for uc in tool["use_cases"]:
            lines.append(f"## {uc.get('label')} ({uc.get('csf_category_id')})")
            lines.append(uc.get("description", ""))
            if isinstance(uc.get("subcategories_json"), list):
                lines.append("**Subcategories:**")
                for sub in uc["subcategories_json"]:
                    if isinstance(sub, dict):
                        lines.append(f"- {sub.get('id')}: {sub.get('text', '')}")
            if isinstance(uc.get("examples_json"), list):
                lines.append("**Implementation Examples:**")
                for ex in uc["examples_json"]:
                    if isinstance(ex, dict):
                        lines.append(f"- ({ex.get('subcategory_id')}) {ex.get('text')}")
        sections["use_cases"] = "\n\n".join(lines)

    # Related Cases
    if tool.get("related_cases"):
        lines = ["# Related ATT&CK Campaigns and Cases"]
        for case in tool["related_cases"]:
            lines.append(f"## {case.get('case_name')}")
            for desc in case.get("descriptions", []):
                lines.append(f"- {desc.get('tech_id')} - {desc.get('tech_name')}: {desc.get('case_description')}")
        sections["related_cases"] = "\n\n".join(lines)

    # Deployment Context
    if dc := tool.get("deployment_context"):
        lines = ["# Deployment Context"]
        if trl := dc.get("trl", {}).get("level"):
            lines.append(f"**TRL**: {trl}")
        for field in ["hosting_env", "interfaces", "access_methods", "input_types", "output_types", "import_formats", "export_formats"]:
            if dc.get(field):
                label = field.replace("_", " ").capitalize()
                values = ", ".join(
                    v if isinstance(v, str) else v.get("name") or v.get("description") or json.dumps(v)
                    for v in dc[field]
                )
                lines.append(f"**{label}**: {values}")
        sections["deployment_context"] = "\n\n".join(lines)

    return sections


def render_section_with_metadata(section_name: str, markdown_body: str, tool_name: str) -> str:
    """Adds frontmatter and summary to a markdown body"""
    chunk_id = hashlib.md5(markdown_body.encode("utf-8")).hexdigest()[:12]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = summarize_text(markdown_body)

    return (
        f"---\n"
        f"tool: {tool_name}\n"
        f"section: {section_name}\n"
        f"chunk_id: {chunk_id}\n"
        f"timestamp: {timestamp}\n"
        f"---\n\n"
        f"> **Summary:** {summary}\n\n"
        f"{markdown_body}"
    )
