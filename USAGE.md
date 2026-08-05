# How to run tos-to-odrl

## Prerequisites

- Python 3.10+
- A virtual environment with dependencies installed:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- An `.env` file with your API key (only needed for OpenAI / remote models):
  ```
  OPENAI_API_KEY=sk-...
  ```

---

## CLI — `main.py`

The main entry point. Runs the full pipeline (split → metadata → TTL → validate → analysis → evaluation) and saves results to an output directory.

### Basic usage

```bash
python main.py --input <file> --output <dir/> [options]
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--input` | *(required)* | Input file: `.json` (pre-split), `.txt`, or `.pdf` |
| `--output` | *(required)* | Directory where results will be saved |
| `--model` | `gpt-4.1-mini` | LLM model name |
| `--base-url` | *(none)* | Base URL for an OpenAI-compatible server (Ollama, vLLM…) |
| `--api-key` | *(env)* | API key — falls back to `OPENAI_API_KEY` |
| `--max-workers` | `4` | Parallel workers per phase |
| `--max-repair-rounds` | `3` | Max self-repair iterations per clause |
| `--provider` | `Unknown` | Provider name (for raw text / PDF inputs) |
| `--title` | *(filename)* | Document title (for raw text / PDF inputs) |
| `--date` | `Unknown` | Document date (for raw text / PDF inputs) |
| `--source` | *(path)* | Source URL or path (for raw text / PDF inputs) |
| `--description` | *(empty)* | Short description of the document |

### Examples

**OpenAI with a pre-split JSON (recommended for reproducibility):**
```bash
python main.py \
  --input data/data_openai/use_cases_openai.json \
  --model gpt-4.1 \
  --output output/openai_gpt41/
```

**From a raw text file, providing metadata:**
```bash
python main.py \
  --input data/elsevier/api_service_agreement_2017.txt \
  --provider "Elsevier" --title "API Service Agreement" --date "2017" \
  --output output/elsevier-2017/
```

**Local Ollama model (OpenAI-compatible endpoint):**
```bash
python main.py \
  --input data/data_openai/use_cases_openai.json \
  --base-url http://localhost:11434/v1 \
  --model qwen2.5:72b \
  --output output/openai_qwen72b/
```

**Ollama on a remote Tailscale node:**
```bash
python main.py \
  --input data/data_openai/use_cases_openai.json \
  --base-url https://<node>.ts.net/v1 \
  --model qwen:110b \
  --output output/openai_qwen110b/
```
> Note: use the `/v1` path, not `/api/generate` — the pipeline uses the OpenAI-compatible endpoint.

---

## Pipeline phases

Each run writes intermediate results to the output directory:

```
output/<run>/
├── phase1/
│   └── metadata.json          # clause type, party, action, asset per clause
├── phase2/
│   └── clause_<n>.ttl         # raw Turtle output per clause
├── phase3/
│   └── clause_<n>.ttl         # validated / self-repaired Turtle
├── analysis/
│   └── clause_<n>.json        # SPARQL queries: deontic status + unfair terms
├── evaluation.json            # semantic similarity scores (back-translation)
└── result.json                # full combined result
```

| Phase | What it does |
|-------|-------------|
| **Step 0** | Splits the raw document into individual clauses |
| **Phase 1** | Extracts metadata (type, party, action, asset) per clause |
| **Phase 2** | Generates an ODRL/TOSL Turtle (TTL) policy per clause |
| **Phase 3** | Validates each TTL against the TOSL ontology and self-repairs if needed |
| **Analysis** | Runs SPARQL queries to extract deontic rules and detect unfair terms |
| **Evaluation** | Back-translates each TTL to natural language and measures semantic similarity |

---

## Web interface

The project includes a Next.js frontend and a FastAPI backend.

**Start the backend** (from the project root):
```bash
source .venv/bin/activate
uvicorn backend.main:app --reload --port 8000
```

**Start the frontend** (in a separate terminal):
```bash
cd frontend
npm run dev
```

Then open `http://localhost:3000`.

The web interface lets you upload a file, configure the model and endpoint, track progress in real time, and browse past analyses from the History page (`/jobs`).

---

## Input formats

### Pre-split JSON (`.json`)
Clauses are already split. Skips Step 0 (faster, fully reproducible).

```json
{
  "PROVIDER": "OpenAI",
  "SOURCE": "https://openai.com/policies/...",
  "TITLE": "Terms of Use",
  "DATE": "2024-12",
  "CLAUSES": [
    { "ID": "clause_1", "TEXT": "You must be at least 13 years old..." },
    ...
  ]
}
```

### Raw text (`.txt`) or PDF (`.pdf`)
The pipeline runs Step 0 to split the document into clauses automatically. Provide `--provider`, `--title`, and `--date` for traceability.

---

## Data in this repo

| Path | Description |
|------|-------------|
| `data/data_openai/use_cases_openai.json` | OpenAI Terms of Use (Dec 2024, EU) — pre-split |
| `data/data_elsevier/use_cases_elsevier.json` | Elsevier API Service Agreement — pre-split |
| `data/elsevier/*.txt` | Raw Elsevier agreements (2014–2017) |
| `data/*/..._expected.json` | Ground-truth classifications for evaluation |
| `metamodel/tosl_odrl_simplified.ttl` | TOSL/ODRL ontology |
| `metamodel/tosl_guidelines.md` | Prompt guidelines for the LLM |
