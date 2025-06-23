from config import *

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = DB_PATH
CSV_DIR = Path(TOOL_DIR)

TABLES = {
    "trl_levels": {
        "csv": "trl_levels.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS trl_levels (
                id INTEGER PRIMARY KEY,
                level INTEGER,
                name TEXT,
                description TEXT,
                deliverables TEXT,
                users TEXT,
                environment TEXT,
                scale TEXT,
                commercial_viable BOOLEAN
            )
        """
    },
    "hosting_env": {
        "csv": "hosting_env.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS hosting_env (
                id INTEGER PRIMARY KEY,
                label TEXT,
                description TEXT
            )
        """
    },
    "interface_types": {
        "csv": "interface_types.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS interface_types (
                id INTEGER PRIMARY KEY,
                label TEXT,
                description TEXT
            )
        """
    },
    "access_methods": {
        "csv": "access_methods.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS access_methods (
                id INTEGER PRIMARY KEY,
                label TEXT,
                description TEXT
            )
        """
    },
    "input_types": {
        "csv": "input_types.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS input_types (
                id INTEGER PRIMARY KEY,
                label TEXT,
                description TEXT
            )
        """
    },
    "output_types": {
        "csv": "output_types.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS output_types (
                id INTEGER PRIMARY KEY,
                label TEXT,
                description TEXT
            )
        """
    },
    "import_formats": {
        "csv": "import_formats.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS import_formats (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        """
    },
    "export_formats": {
        "csv": "export_formats.csv",
        "schema": """
            CREATE TABLE IF NOT EXISTS export_formats (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        """
    }
}

def create_and_populate_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for table_name, meta in TABLES.items():
            print(f"📐 Creating table: {table_name}")
            cur.execute(meta["schema"])
            conn.commit()

            csv_path = CSV_DIR / meta["csv"]
            df = pd.read_csv(csv_path)

            # Optional cleaning for JSON-like columns
            if "deliverables" in df.columns:
                df["deliverables"] = df["deliverables"].apply(lambda x: str(x) if not pd.isna(x) else "")
            if "users" in df.columns:
                df["users"] = df["users"].apply(lambda x: str(x) if not pd.isna(x) else "")

            df.to_sql(table_name, conn, if_exists="replace", index=False)
            count = cur.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
            print(f"✅ Loaded {count} rows into [{table_name}]")

if __name__ == "__main__":
    create_and_populate_tables()
