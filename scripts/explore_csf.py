import json
from InquirerPy import inquirer
from rich.console import Console

CSF_JSON_PATH = "C:/Projects/cyote_tool_wiz/data/csf-export.json"
console = Console()

def load_csf_elements():
    with open(CSF_JSON_PATH, "r", encoding="utf-8") as f:
        csf_data = json.load(f)
    return csf_data["response"]["elements"]["elements"]

def group_elements(elements):
    functions = {}
    categories = {}
    subcategories = {}

    for el in elements:
        el_type = el.get("element_type")
        el_id = el.get("element_identifier")
        title = el.get("title", "").strip()
        text = el.get("text", "").strip()

        if el_type == "function":
            functions[el_id] = {"title": title, "text": text, "categories": []}

        elif el_type == "category":
            categories[el_id] = {
                "title": title,
                "text": text,
                "function": el_id.split(".")[0],
                "subcategories": []
            }

        elif el_type == "subcategory":
            subcategories[el_id] = {
                "title": title,
                "text": text,
                "category": el_id.split("-")[0],
                "examples": []
            }

        elif el_type == "implementation_example":
            parts = el_id.split(".")
            if len(parts) >= 2:
                sub_id = ".".join(parts[:2])
                if sub_id not in subcategories:
                    subcategories[sub_id] = {
                        "title": "",
                        "text": text,  # use first example as description fallback
                        "category": sub_id.split("-")[0],
                        "examples": []
                    }
                elif not subcategories[sub_id]["text"]:
                    subcategories[sub_id]["text"] = text
                subcategories[sub_id]["examples"].append({
                    "id": el_id,
                    "text": text,
                    "title": title
                })

    # Link categories to functions
    for cid, c in categories.items():
        fn = c["function"]
        if fn in functions:
            functions[fn]["categories"].append(cid)

    # Link subcategories to categories
    for sid, s in subcategories.items():
        cat = s["category"]
        if cat in categories:
            categories[cat]["subcategories"].append(sid)

    return functions, categories, subcategories


def main():
    elements = load_csf_elements()
    functions, categories, subcategories = group_elements(elements)

    fn_choice = inquirer.select(
        message="Select a CSF 2.0 Function:",
        choices=[{"name": f"{fid}: {f['title']}", "value": fid} for fid, f in functions.items()]
    ).execute()

    console.rule(f"[bold green]Function: {functions[fn_choice]['title']} ({fn_choice})")
    console.print(functions[fn_choice]["text"])
    console.print()

    cat_choices = functions[fn_choice]["categories"]
    cat_choice = inquirer.select(
        message="Select a Category:",
        choices=[{"name": f"{cid}: {categories[cid]['title']}", "value": cid} for cid in cat_choices]
    ).execute()

    console.rule(f"[bold cyan]Category: {categories[cat_choice]['title']} ({cat_choice})")
    console.print(categories[cat_choice]["text"])
    console.print()

    console.rule("[bold yellow]Subcategories & Examples")

    for sid in sorted(categories[cat_choice]["subcategories"]):
        sub = subcategories[sid]
        desc = sub["title"] or sub["text"] or "No description"
        console.print(f"\n[bold]{sid}[/bold]: {desc}")

        for example in sub["examples"]:
            if example["text"]:
                console.print(f"   - [italic]{example['text']}[/italic]")

    console.print()


if __name__ == "__main__":
    main()
