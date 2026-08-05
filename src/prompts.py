from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------------------------------------------------
# Step 0 — Clause splitting
# ---------------------------------------------------------------------------

SPLIT_PROMPT = ChatPromptTemplate.from_template("""
You are a legal document analyst.

Your task is to split the following Terms of Service text into individual, self-contained clauses.

Rules:
- Each clause must express exactly one legal obligation, right, or statement.
- Preserve the original wording exactly — do not paraphrase or summarise.
- Ignore pure headings, section numbers, and non-substantive text (e.g. "Effective Date: 2025-01-01").
- Return a JSON array of strings, one entry per clause.
- Do not include any explanation or commentary outside the JSON array.

Terms of Service text:
{text}
""")

# ---------------------------------------------------------------------------
# Phase 1 — Classification and metadata extraction
# ---------------------------------------------------------------------------

PHASE1_PROMPT = ChatPromptTemplate.from_template("""
You are a legal analyst specializing in SaaS Terms of Service.

For the following clause, perform these steps:

1. Classify it EXCLUSIVELY as one of these 6 labels, in lowercase:
   - permission: granting a right or authorization (e.g. "may use", "is permitted").
   - prohibition: restricting or forbidding an action (e.g. "may not", "prohibited").
   - obligation: the party owes or is required to do something (e.g. "must", "shall", "required to").
   - dispute resolution: legal conflict mechanisms (e.g. "arbitration", "jurisdiction", "governing law").
   - liability: responsibilities or limitations of liability (e.g. "limitation of liability", "warranty disclaimer").
   - other: ONLY for pure headings, non-substantive text, or definition lists without operational context.

2. Identify the responsible party: "customer", "provider", or "both".
   - If the clause refers to "the parties" or "each party", use "both".
   - Do not use "unspecified" if the party is clearly implied in the text.

3. Identify the most relevant action from the list below.
   - "dispute resolution" and "liability" clauses always use "unspecified".
   - ONLY select from the list — do not create new actions.
   {actions_list}

4. Identify the asset (object of the clause), as a short noun phrase (≤ 3 words).
   - If no asset is clearly specified, write "unspecified".

Return ONLY a JSON object with exactly these fields:
{{
  "type": "<label>",
  "party": "<party>",
  "action": "<action>",
  "asset": "<asset>"
}}

Clause:
{clause}
""")

# ---------------------------------------------------------------------------
# Phase 2 — Turtle generation
# ---------------------------------------------------------------------------

PHASE2_PROMPT = ChatPromptTemplate.from_template("""
You are a legal knowledge extractor specialized in TOSL and ODRL policy modeling.

Tasks:
- Read the clause and its metadata.
- Produce a SINGLE minimal ODRL/TOSL policy in Turtle.

Guidelines:
- Output MUST be valid Turtle inside a single fenced code block: ```ttl … ```
- Use ONLY the vocabulary, classes, properties, and prefixes from the ontology context and reference template below.
- All URIs and prefixes must be exactly as shown.
- Do not add explanations, headers, or any commentary outside the code block.
- Use the clause ID "{clause_id}" as a suffix for all policy-specific local URIs to avoid conflicts when files are merged.
  Example: :{clause_id}_agreement, :{clause_id}_permission01, :{clause_id}_asset
  Shared named entities (provider, customer, etc.) keep standard names: :OpenAI, :customer, :provider

Ontology context:
{ontology}

Reference template:
{guidelines}

Document metadata:
- Provider: {provider}
- Source: {source}
- Title: {title}
- Date: {date}
- Clause ID: {clause_id}

Clause: {clause}
Classification type: {clause_type}
Party: {party}
Suggested action: {action}
Target asset: {asset}
""")

# ---------------------------------------------------------------------------
# Phase 3 — Self-repair
# ---------------------------------------------------------------------------

PHASE3_REPAIR_PROMPT = ChatPromptTemplate.from_template("""
You are a knowledge engineer specialized in RDF/Turtle and ontology-driven validation.

Tasks:
- Read the original clause text, the Turtle file, and the validator violations listed below.
- Fix ALL violations so that the output conforms to the TOSL guidelines.
- Preserve all correct information and the original meaning of the clause wherever possible.

Guidelines:
- Output MUST be valid Turtle inside a single fenced code block: ```ttl … ```
- Use ONLY the vocabulary and structure from the reference template below.
- All URIs and prefixes must be exactly as shown.
- Do not add explanations or commentary outside the code block.
- Do not introduce new errors while fixing existing ones.

Reference template:
{guidelines}

Original clause text:
{clause_text}

Validator violations (JSON):
{violations}

Original Turtle:
{ttl}
""")
