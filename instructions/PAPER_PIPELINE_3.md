# Paper Pipeline — Step 3c: Resolve Bibliography

**Model:** GPT

You are resolving bibliography entries for arXiv paper [ARXIV_ID].

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools.

---

## Task
Match cited keys against the .bib file and extract bibliographic data.

**Inputs:**
- Cited keys: `data/papers/[ARXIV_ID]_cited_keys.json`
- Bib file: `/tmp/[ARXIV_ID]/*.bib` (or embedded in .tex)

**For each key**, look it up in the .bib and extract:
- First author name
- Year
- DOI (if present)
- Single author? true/false

**Output:** `data/papers/[ARXIV_ID]_bibliography_complete.json`
```json
[
  {
    "key": "LyndsToomre1976",
    "first_author": "Lynds",
    "year": "1976",
    "doi": null,
    "single_author": false,
    "claim_summary": "Seminal work on collisional ring formation"
  }
]
```

This is mechanical — only resolve the ~80-100 actually-cited references, not the full .bib.
