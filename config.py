from pathlib import Path

# Dynamically determine project root (assumes config.py is in project root)
PROJECT_ROOT = Path(__file__).resolve().parent

# Common directories
DATA_DIR = PROJECT_ROOT / "data"
TOOL_CAPABILITIES_DIR = DATA_DIR / "tool_capabilities"
CHUNKS_DIR = DATA_DIR / "chunks"
DB_PATH = DATA_DIR / "tool_knowledge.db"
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "cyote_assistant.ipynb"
