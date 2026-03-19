# ArXiv Atlas — Quick Start for Paper Processing

## One-Paper Run (Copy & Paste)

Replace `2603.15869` with the actual arXiv ID.

### Step 1-2: Fetch & Metadata (GPT)
```bash
# Spawn in main session or use:
sessions_spawn --task "Read PAPER_PIPELINE_1.md and process 2603.15869" \
  --model GPT --runtime subagent --cwd projects/arxiv-atlas
```

### Step 3: Section Analysis (Sonnet)
```bash
sessions_spawn --task "Read PAPER_PIPELINE_2.md and analyze 2603.15869 sections" \
  --model CopilotSonnet --runtime subagent --cwd projects/arxiv-atlas
```

### Step 3c: Citation Resolution (GPT)
```bash
sessions_spawn --task "Read PAPER_PIPELINE_3.md and resolve 2603.15869 citations" \
  --model GPT --runtime subagent --cwd projects/arxiv-atlas
```

### Steps 4-5: Wiki Connections (Haiku)
```bash
sessions_spawn --task "Read PAPER_PIPELINE_4.md and find wiki connections for 2603.15869" \
  --model CopilotHaiku --runtime subagent --cwd projects/arxiv-atlas
```

### Steps 6-8: Critical Analysis + Pages (Opus)
```bash
sessions_spawn --task "Read PAPER_PIPELINE_5.md and write wiki pages for 2603.15869" \
  --model CopilotOpus --runtime subagent --cwd projects/arxiv-atlas
```

### Ingest & Rebuild
```bash
cd projects/arxiv-atlas
python3 tools/ingest_manifest.py data/papers/2603.15869_manifest.json
python3 tools/build_site.py
```

### Cleanup
```bash
rm -f data/papers/2603.15869_{manifest,cited_keys,page_updates,meta,parse_note,raw_bib,keytakeaways}* \
      data/papers/2603.15869.{pdf,bib} \
      data/papers/2603.15869_critical_analysis.md
rm -rf /tmp/2603.15869/
```

## Key Files

- **Instructions:** `instructions/PAPER_PIPELINE_*.md` (1 through 5, plus MAIN)
- **Database:** `data/arxiv.db`
- **Papers (analysis):** `data/papers/[arxiv_id].md`
- **Wiki pages:** `src/content/pages/[slug].md`
- **Built site:** `dist/` (static HTML)

## Manifest Format (Opus Must Produce This!)

**File:** `data/papers/[arxiv_id]_manifest.json`

```json
{
  "arxiv_id": "2603.15869",
  "title": "J-PLUS...",
  "authors": ["Author"],
  "date": "2026-03-15",
  "doi": "10.48550/arXiv.2603.15869",
  "status": "done",
  "pages_created": [
    {"slug": "2603-15869", "type": "paper", "title": "...", "level": null},
    {"slug": "galaxy-groups", "type": "concept", "title": "...", "level": "intermediate"}
  ],
  "analysis_file": "data/papers/2603-15869.md",
  "bibliography_file": "data/papers/2603-15869_bibliography_complete.json"
}
```

**CRITICAL:** The ingester MUST see `pages_created` array!

## Common Debugging

| Problem | Solution |
|---------|----------|
| "Database locked" | Wait 2 seconds and retry |
| Papers don't appear in `/papers/` | Check manifest has `pages_created` |
| Duplicate papers | Delete bad entries: `sqlite3 data/arxiv.db "DELETE FROM pages WHERE page_slug LIKE 'papers/%';"` |
| PDF text extraction fails | Normal — fallback to HTML. Already done by subagent. |
| Reference links don't expand | Verify `/pages/` shows the paper. Check Base.astro script loaded. |

## Verify Success

```bash
# Check DB has paper
sqlite3 data/arxiv.db "SELECT arxiv_id, title FROM papers WHERE arxiv_id = '2603.15869';"

# Check pages exist
ls src/content/pages/2603-15869.md src/content/pages/galaxy-groups.md ...

# Check site built
open dist/pages/2603-15869/index.html
```

---

**For full details:** Read `instructions/PAPER_PIPELINE_MAIN.md`
