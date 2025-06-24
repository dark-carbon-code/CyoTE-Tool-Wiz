import json


def generate_markdown_summary(tool: dict) -> str:
    """Convert CyOTE tool metadata to a rich, RAG-ready Markdown format."""
    lines = []

    # Title
    lines.append(f"# Tool: {tool.get('tool_name', tool.get('name', 'Unnamed Tool'))}")
    lines.append("")

    # Description
    if desc := tool.get("description"):
        lines.append("## 🔍 Description")
        lines.append(desc.strip())
        lines.append("")

    # Long description or fact sheet
    if facts := tool.get("fact_sheet_text") or tool.get("factsheet"):
        lines.append("## 🧾 Fact Sheet / Extended Description")
        lines.append(facts.strip())
        lines.append("")

    # GitHub URL
    if github := tool.get("github") or tool.get("github_url"):
        lines.append("## 💻 GitHub")
        lines.append(github)
        lines.append("")

    # Example usage
    if example := tool.get("example_usage"):
        lines.append("## 🧪 Example Usage")
        lines.append(example.strip())
        lines.append("")

    # MITRE Matrix
    if matrix := tool.get("matrix"):
        lines.append("## 📊 MITRE Matrix")
        lines.append(matrix)
        lines.append("")

    # Tactics
    if tactics := tool.get("tactics_supported") or tool.get("tactics"):
        lines.append("## 🎯 ATT&CK Tactics")
        for tactic in tactics:
            lines.append(f"- {tactic}")
        lines.append("")

    # Techniques
    if techniques := tool.get("techniques_supported") or tool.get("techniques"):
        lines.append("## 🧬 ATT&CK Techniques")
        for tech in techniques:
            tech_id = tech.get("id", "")
            tech_name = tech.get("name", "")
            lines.append(f"- {tech_id}: {tech_name}")
        lines.append("")

    # Observable Types
    if obs_types := tool.get("observable_types"):
        lines.append("## 👁 Observable Types")
        for obs in obs_types:
            name = obs.get("name", "")
            category = obs.get("category", "")
            lines.append(f"- {name} ({category})")
        lines.append("")

    # CSF Use Cases
    if csf := tool.get("use_cases") or tool.get("csf_use_cases"):
        lines.append("## 🛡️ CSF 2.0 Use Cases")
        for uc in csf:
            func = uc.get("csf_function_id", uc.get("function", ""))
            cat = uc.get("csf_category_id", uc.get("category", ""))
            desc = uc.get("description", "")
            lines.append(f"- **{func} → {cat}**")
            if desc:
                lines.append(f"  _\"{desc.strip()}\"_")
        lines.append("")

    # Roles
    if roles := tool.get("user_roles") or tool.get("roles"):
        lines.append("## 👥 User Roles")
        for role in roles:
            name = role.get("name", "")
            justification = role.get("justification", "")
            lines.append(f"- **{name}**: {justification}")
        lines.append("")

    # Deployment Context
    if deploy := tool.get("deployment_context", {}):
        lines.append("## 🚀 Deployment Context")

        # TRL
        if trl := deploy.get("trl") or deploy.get("TRL"):
            label = trl.get("label", trl)
            lines.append(f"- **Technology Readiness Level (TRL)**: {label}")

        for field in [
            "hosting_env", "interfaces", "input_types", "output_types",
            "access_methods", "import_formats", "export_formats"
        ]:
            values = deploy.get(field)
            if values:
                pretty_name = field.replace("_", " ").capitalize()
                str_values = []
                for v in values:
                    if isinstance(v, dict):
                        str_values.append(v.get("name", str(v)))
                    else:
                        str_values.append(str(v))
                lines.append(f"- **{pretty_name}**: {', '.join(str_values)}")
        lines.append("")

    # Targeted Assets
    if assets := tool.get("targeted_assets"):
        lines.append("## 🏗️ Targeted Assets")
        for asset in assets:
            name = asset.get("name", "")
            desc = asset.get("description", "")
            lines.append(f"- **{name}**: {desc}")
        lines.append("")

    # Related Cases
    if cases := tool.get("related_cases"):
        lines.append("## 📚 Related CyOTE Cases")
        for case in cases:
            case_name = case.get("case_name", "Unknown Case")
            lines.append(f"- **{case_name}**")
            for desc in case.get("descriptions", []):
                tech_name = desc.get("tech_name", "")
                case_desc = desc.get("case_description", "")
                lines.append(f"  - {tech_name}: _{case_desc.strip()}_")
        lines.append("")

    # Optional: Full raw metadata for fallback
    lines.append("---")
    lines.append("## 🧾 Full JSON Metadata")
    lines.append("```json")
    lines.append(json.dumps(tool, indent=2, ensure_ascii=False))
    lines.append("```")

    return "\n".join(lines)
