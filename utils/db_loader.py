from config import *

import json
import sqlite3
from pathlib import Path
from langchain.docstore.document import Document
from rich import print


def load_jsonl_chunks(jsonl_path: Path) -> list[Document]:
    """
    Load .jsonl chunked documents into LangChain-compatible Document objects.

    Args:
        jsonl_path (Path): Path to a .jsonl file.

    Returns:
        list[Document]: List of documents ready for embedding.
    """
    if not jsonl_path.exists():
        raise FileNotFoundError(f"Chunk file not found: {jsonl_path}")

    documents = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            documents.append(Document(page_content=data["content"], metadata=data["metadata"]))

    print(f"[green]✔ Loaded {len(documents)} documents from:[/green] {jsonl_path}")
    return documents


def load_db_entries(db_path: Path) -> list[Document]:
    ""DB_PATH""
    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    documents = []

    # Example: Load tool descriptions and join related roles/use cases
    query = """
        SELECT t.tool_name, t.description, r.name as role_name, uc.name as use_case_name
        FROM tools t
        LEFT JOIN tool_roles tr ON t.id = tr.tool_id
        LEFT JOIN roles r ON tr.role_id = r.id
        LEFT JOIN tool_use_cases tuc ON t.id = tuc.tool_id
        LEFT JOIN use_cases uc ON tuc.use_case_id = uc.id
    """

    for row in cursor.execute(query):
        tool_name, description, role_name, use_case_name = row
        content = f"Tool: {tool_name}\nDescription: {description}\nUser Role: {role_name}\nUse Case: {use_case_name}"
        metadata = {
            "tool_name": tool_name,
            "role": role_name,
            "use_case": use_case_name,
            "source": DB_PATH
        }
        documents.append(Document(page_content=content, metadata=metadata))

    conn.close()
    print(fDB_PATH)
    return documents
