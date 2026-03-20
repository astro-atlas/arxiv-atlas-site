# Paper Pipeline — Orchestrator

This is the orchestrator reference for processing arXiv papers. The orchestrator spawns one subagent per step, passing data between them via the filesystem. Each step's detailed instructions are in a separate file — pass only the relevant file to each subagent.

**Working directory:** `projects/arxiv-atlas/`. All other folders and files are in this directory. Instructions are in the `instructions/` folder.

---

## Overview

```
Step 1  [GPT]     Fetch paper source (tarball → HTML → PDF)
Step 2  [GPT]     Extract metadata → data/papers/[id].md
Step 3  [Haiku]  Section-by-section analysis → append to data/papers/[id].md
Step 3c [GPT]     Resolve cited keys against .bib → bibliography JSON
Step 4  [GPT]   Check wiki connections against existing pages
Step 5  [Haiku]   Recommend new wiki pages
Step 6  [Opus]    Critical analysis + knowledge graph + page update instructions
Step 7  [Opus]    Key Takeaways synthesis
Step 8  [Opus]    Write paper page + new concept pages
Step 8.3[Haiku]   Update existing concept pages (mechanical)
  ↓
Orchestrator:     Ingest manifest → DB → extract links → rebuild site. Then push updates to github.
```

---

## Subagent Dispatch

Subagents should write their outputs in the files noted in `Outputs`. The primary output file is the `data/papers/[id].md` summary file that is shared between subagents. Avoid creating unneccessary files.
**Agents must finish their runs in this order - do not start another subagent until the previous one completed their task.**

| Step(s)  | Model  | Instructions File      | Inputs                                      | Outputs                                                |
|----------|--------|------------------------|----------------------------------------------|--------------------------------------------------------|
| 1 & 2   | GPT    | `PAPER_PIPELINE_1.md`  | arXiv ID                                     | `/tmp/[id]/fetch_result.json`, `data/papers/[id].md`   |
| 3        | Haiku | `PAPER_PIPELINE_2.md`  | `.tex` source, `data/papers/[id].md`         | Appended analysis, `_cited_keys.json`, `_concepts.json`|
| 3c       | GPT    | `PAPER_PIPELINE_3.md`  | `_cited_keys.json`, `.bib` file              | `_bibliography_complete.json`                          |
| 4 & 5   | GPT  | `PAPER_PIPELINE_4.md`  | `data/papers/[id].md`, `existing-slugs.json` | Appended Wiki Connections + Recommended Pages          |
| 6, 7, 8 | Opus   | `PAPER_PIPELINE_5.md`  | `data/papers/[id].md`, existing wiki pages   | Critical Analysis, Key Takeaways, wiki pages, manifest |
| 8.3      | Haiku  | `PAPER_PIPELINE_6.md`  | `_page_updates.json`, existing wiki pages    | Modified `.md` files + update summary                  |

**Tools available to subagents:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. They do NOT have session tools.

**Agent ID:** All pipeline subagents MUST be spawned with `agentId: "pipeline"`. This routes them through the `pipeline` agent config which has `cacheRetention: "none"` — avoiding unnecessary cache writes for one-shot paper processing runs.

---

## Orchestrator Responsibilities

### Before spawning subagents
1. Claim paper in DB: `python3 -c "import db_access; db_access.claim_paper_for_processing('[arxiv-id]')"`
2. Create tracking entry in `data/papers/tracking/YYYY-MM-DD_analyzed.md`

### After subagent returns manifest
1. **Ingest into database:**
   ```bash
   python3 tools/ingest_manifest.py data/papers/[arxiv-id]_manifest.json
   ```
   This upserts the paper, creates all page records, and links them.

2. **Extract page links from .md files:**
   ```bash
   python3 tools/extract_and_insert_page_links.py
   ```

3. **Rebuild site:**
   ```bash
   python3 tools/build_site.py
   ```

4. **Update tracking:** Mark `[x]` in tracking file.

### Batch processing
- Spawn multiple subagents in parallel (they write to different files)
- Collect manifests as they complete
- Run DB ingestion + site rebuild once after all complete (or after each)
- If two subagents modify the same concept page, review and merge before ingestion

---


## Key Paths

| What | Where |
|------|-------|
| Analysis files | `data/papers/<id>.md` |
| Bibliography JSON | `data/papers/<id>_bibliography_complete.json` |
| Manifest JSON | `data/papers/<id>_manifest.json` |
| Page updates JSON | `data/papers/<id>_page_updates.json` |
| Wiki pages | `src/content/pages/` |
| Existing page index | `public/existing-slugs.json` |
| Database | `data/arxiv.db` |
| Ingestion script | `tools/ingest_manifest.py` |
| Build script | `tools/build_site.py` |
| Tracking | `data/papers/tracking/YYYY-MM-DD_analyzed.md` |
