
# 🛠️ CyOTE Tool Wiz – Offline Setup on Work Machine

This guide provides step-by-step instructions for setting up the CyOTE Tool Wiz on a work computer **without needing to download the Ollama model from the internet**.

---

## 1. Clone the Repository

On your work computer, open a terminal and run:

```bash
git clone https://github.com/dark-carbon-code/CyoTE-Tool-Wiz.git
cd CyoTE-Tool-Wiz
````

---

## 2. Download and Extract the Ollama Model (gemma3:12b)

Since your work computer has limited download access, you should retrieve the model from your personal Google Drive:

**Download link:**
[gemma3:12b models.zip](https://drive.google.com/file/d/1Az9Mp3gtuBI6PGQqJXHtNajq3w292sq8/view?usp=drive_link)

Once downloaded:

1. Move the `models.zip` file into the project directory (`CyoTE-Tool-Wiz/`)
2. Extract it using:

```bash
unzip models.zip -d models/
```

This should produce a folder like:

```
models/
├── manifest.json
├── sha256:<model_blob1>
├── sha256:<model_blob2>
├── ...
```

---

## 3. Start Dockerized Environment

Ensure Docker Desktop is installed. Then run:

```bash
docker-compose up -d
```

This will start:

* `ollama` container with API on port `11434`
* `open-webui` container on port `3000`, mapped to `chunks_md/`

---

## 4. Verify the Setup

Visit [http://localhost:3000](http://localhost:3000) in your browser.

Check that Open WebUI is running and able to detect the `gemma3:12b` model.

In a terminal, verify the model with:

```bash
curl http://localhost:11434/api/tags
```

You should see `gemma3:12b` in the list.

---

## 5. Use the CLI

To generate a tool entry:

```bash
python cli.py
```

You will be guided through interactive prompts and the output will be saved in:

* `tool_capabilities/` – full tool JSON
* `chunks_md/` – Markdown section files
* `data/tool_markdown_summaries/` – combined `.md` + `.json` for RAG

---

## 6. Directory Overview

```
CyoTE-Tool-Wiz/
├── cli.py
├── docker-compose.yml
├── models/                  # Manually extracted model blobs
├── chunks_md/               # RAG-ready .md sections
├── tool_capabilities/       # Saved tool entries (.json)
├── data/tool_markdown_summaries/
├── utils/
│   ├── md_chunk_exporter.py
│   ├── markdown_renderer.py
│   └── rag_formatter.py
├── wizard/
│   └── interactive_create.py
└── SETUP_ON_WORK.md         # This file
```