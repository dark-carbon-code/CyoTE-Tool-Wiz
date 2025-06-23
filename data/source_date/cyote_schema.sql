
-- 1. MITRE Matrices
CREATE TABLE IF NOT EXISTS matrices (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- 2. Tactics
CREATE TABLE IF NOT EXISTS tactics (
    id TEXT PRIMARY KEY,
    stix_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    url TEXT,
    matrix_id INTEGER NOT NULL,
    FOREIGN KEY(matrix_id) REFERENCES matrices(id)
);

-- 3. Techniques
CREATE TABLE IF NOT EXISTS techniques (
    id TEXT PRIMARY KEY,
    stix_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    url TEXT,
    tactic_id TEXT,
    matrix_id INTEGER NOT NULL,
    FOREIGN KEY(tactic_id) REFERENCES tactics(id),
    FOREIGN KEY(matrix_id) REFERENCES matrices(id)
);

-- 4. Data Sources
CREATE TABLE IF NOT EXISTS data_sources (
    id TEXT PRIMARY KEY,
    stix_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    matrix_id INTEGER NOT NULL,
    FOREIGN KEY(matrix_id) REFERENCES matrices(id)
);

-- 5. ICS Assets
CREATE TABLE IF NOT EXISTS assets (
    id TEXT PRIMARY KEY,
    stix_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    url TEXT
);

-- 6. Tools (CyOTE Tool Entries)
CREATE TABLE IF NOT EXISTS tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_name TEXT,
    description TEXT,
    deployment_context TEXT,
    example_usage TEXT,
    github TEXT,
    factsheet TEXT
);

-- 7. Tool Roles
CREATE TABLE IF NOT EXISTS tool_roles (
    tool_id INTEGER,
    role TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id)
);

-- 8. Tool Tactics
CREATE TABLE IF NOT EXISTS tool_tactics (
    tool_id INTEGER,
    tactic_id TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id),
    FOREIGN KEY(tactic_id) REFERENCES tactics(id)
);

-- 9. Tool Techniques
CREATE TABLE IF NOT EXISTS tool_techniques (
    tool_id INTEGER,
    technique_id TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id),
    FOREIGN KEY(technique_id) REFERENCES techniques(id)
);

-- 10. Tool Data Sources
CREATE TABLE IF NOT EXISTS tool_datasources (
    tool_id INTEGER,
    datasource_id TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id),
    FOREIGN KEY(datasource_id) REFERENCES data_sources(id)
);

-- 11. Tool Use Cases
CREATE TABLE IF NOT EXISTS tool_use_cases (
    tool_id INTEGER,
    use_case TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id)
);

-- 12. Tool Observable Types
CREATE TABLE IF NOT EXISTS tool_observable_types (
    tool_id INTEGER,
    type_category TEXT,
    description TEXT,
    FOREIGN KEY(tool_id) REFERENCES tools(id)
);
