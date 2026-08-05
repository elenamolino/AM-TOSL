# ---------------------------------------------------------------------------
# LLM
# ---------------------------------------------------------------------------

DEFAULT_MODEL = "gpt-4.1-mini"
DEFAULT_TEMPERATURE = 0
MAX_REPAIR_ROUNDS = 3

# ---------------------------------------------------------------------------
# TOSL API
# ---------------------------------------------------------------------------

TOSL_VALIDATOR_URL = "https://tosl.onrender.com/validator/validate"
TOSL_DEONTIC_URL = "https://tosl.onrender.com/sparql/deontic_status"
TOSL_UNFAIR_URL = "https://tosl.onrender.com/sparql/unfair_terms"

DEONTIC_QUERIES = ["get_duties", "get_permissions", "get_prohibitions", "total_rules"]

UNFAIR_TERM_TYPES = [
    "change",
    "termination",
    "contract_by_use",
    "choice_of_law",
    "jurisdiction",
    "arbitration",
    "content_removal",
    "limitation_of_liability",
]

# ---------------------------------------------------------------------------
# TOSL / ODRL action vocabulary
# ---------------------------------------------------------------------------

TOSL_ACTIONS = [
    "tosl:allowDownload",
    "tosl:appeal",
    "tosl:assign",
    "tosl:claim",
    "tosl:consent",
    "tosl:develop",
    "tosl:evaluate",
    "tosl:integrate",
    "tosl:procedure",
    "tosl:publish",
    "tosl:remove",
    "tosl:terminate",
    "tosl:test",
]

ODRL_ACTIONS = [
    "odrl:acceptTracking",
    "odrl:aggregate",
    "odrl:anonymize",
    "odrl:annotate",
    "odrl:archive",
    "odrl:attribute",
    "odrl:compensate",
    "odrl:concurrentUse",
    "odrl:delete",
    "odrl:derive",
    "odrl:digitize",
    "odrl:display",
    "odrl:distribute",
    "odrl:ensureExclusivity",
    "odrl:execute",
    "odrl:extract",
    "odrl:give",
    "odrl:grantUse",
    "odrl:include",
    "odrl:index",
    "odrl:inform",
    "odrl:install",
    "odrl:modify",
    "odrl:move",
    "odrl:nextPolicy",
    "odrl:obtainConsent",
    "odrl:play",
    "odrl:present",
    "odrl:print",
    "odrl:read",
    "odrl:reproduce",
    "odrl:reviewPolicy",
    "odrl:sell",
    "odrl:stream",
    "odrl:synchronize",
    "odrl:textToSpeech",
    "odrl:transfer",
    "odrl:transform",
    "odrl:translate",
    "odrl:uninstall",
    "odrl:use",
    "odrl:watermark",
]

ALL_ACTIONS = TOSL_ACTIONS + ODRL_ACTIONS + ["unspecified"]

# ---------------------------------------------------------------------------
# RDF namespace prefixes (used when shortening URIs in API responses)
# ---------------------------------------------------------------------------

RDF_PREFIXES: dict[str, str] = {
    "http://www.w3.org/ns/odrl/2/": "odrl:",
    "https://w3id.org/tosl/": "tosl:",
    "http://purl.org/dc/terms/": "dcterms:",
    "http://example.com/": ":",
    "http://www.w3.org/2001/XMLSchema#": "xsd:",
    "http://www.w3.org/ns/shacl#": "sh:",
}
