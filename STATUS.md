# ArXiv Atlas Project Status

## Current Phase: Active Paper Processing
Updated: 2026-03-19 01:46 UTC

## Architecture

The site is built with **Astro** (https://astro.build/), a static site generator that produces pure HTML/CSS/JS output. All pages share a single Astro layout template for consistent look and feel.

**Comprehensive documentation:** All workflow instructions are now in the `instructions/` folder.

**Current Project Structure:**
```
arxiv-atlas/
├── instructions/              # ← ALL workflow documentation
│   ├── WORKFLOW.md            # High-level overview
│   ├── DATABASE.md            # Complete DB schema reference
│   ├── ARXIV_WORKFLOW.md      # Main agent workflow
│   ├── SUBAGENT_PARSE_WORKFLOW.md  # Subagent instructions
│   ├── ARXIV_PARSE_WORKFLOW.md     # Alternative parse workflow
│   └── README_DEPLOY.md       # Build & deployment guide
├── data/
│   └── arxiv.db               # SQLite database (clean slate - 0 papers, 11 template pages)
├── tools/                     # Python scripts for DB & build pipeline
│   ├── db_access.py           # SQLite access layer
│   ├── db_schema.sql          # Schema definition
│   ├── export_for_site.py     # DB → JSON export
│   ├── generate_links.py      # Build link map
│   ├── build_site.py          # Orchestrate full build
│   └── [other tools...]
├── src/
│   ├── layouts/
│   │   └── Base.astro         # Shared page template
│   ├── components/
│   │   ├── Sidebar.astro      # Auto-TOC sidebar
│   │   └── WikiLink.astro     # Smart link component (handles missing pages)
│   ├── data/                  # JSON exports (imported by Astro at build time)
│   │   ├── links.json
│   │   ├── stats.json
│   │   ├── pages_index.json
│   │   └── [other exports...]
│   └── pages/
│       ├── index.astro        # Homepage
│       └── _template.astro    # Article template
├── dist/                      # Built static output
├── *_old/                     # Previous structure (preserved)
│   ├── data_old/              # 53 analyzed papers from old workflow
│   ├── src_old/
│   ├── papers_old/
│   └── concepts_old/
└── arxiv_atlas.db             # Old database (preserved for reference)
```

## Major Changes (2026-03-17)

### Complete Pipeline Restructure

**Instructions centralized:** All workflow documentation moved to `instructions/` folder:
- WORKFLOW.md — High-level overview with citation rules
- DATABASE.md — Complete schema reference
- ARXIV_WORKFLOW.md — Main agent coordination workflow
- SUBAGENT_PARSE_WORKFLOW.md — Detailed subagent analysis steps
- ARXIV_PARSE_WORKFLOW.md — Alternative workflow reference
- README_DEPLOY.md — Build & deployment guide

**Two-tier processing model:**
1. **Main agent** (coordinator) — reviews proposals, writes to DB/wiki, rebuilds site
2. **Sub-agents** — analyze papers, extract concepts, propose changes

**Multi-model pipeline per paper:**
- **GPT** (github-copilot/gpt-5-mini) — Fetch, query wiki, write updates
- **Sonnet** (anthropic/claude-sonnet-4-5) — Extract concepts, summarize, parse
- **Opus** (anthropic/claude-opus-4-6) — Critical analysis, reasoning

**Critical citation rule:** Every factual statement on any wiki page MUST include a reference (to the paper itself or cited DOIs). Format: `[DOI] [First author] [main concept]: statement [pagelink] [exists]`

**Daily summaries:** After processing each day's papers, create `daily_YYYY_MM_DD.astro` page identifying 3-4 key themes and grouping papers under them.

### Database State

**Active database:** `data/arxiv.db`
- Papers: 9 entries (processing March 18 batch)
- Pages: 140 total (9 paper pages + 131 concept pages)
- Schema: matches DATABASE.md exactly

**Old database preserved:** `arxiv_atlas.db` contains 53 analyzed papers from previous workflow (in `data_old/`)

### Structure Fixed ✅

**Directory structure now matches instructions (fixed 2026-03-17 20:48 UTC):**
- ✅ Created `src/pages/pages/` for wiki articles
- ✅ Created `data/papers/` for tracking/analysis files
- ✅ Created `data/temp/` for subagent working files
- ✅ Moved template to `src/pages/pages/_template.astro`
- ✅ Copied example analysis file for reference

**Verification complete:**
- Export tools run successfully
- Link map generation works
- Site builds in 1.09s
- All paths align with documentation

## Current State

✅ **Actively processing papers:**
- Complete workflow documentation in `instructions/`
- Full tool suite in `tools/`
- 9 papers processed from March 18 batch
- 140 wiki pages live (9 paper + 131 concept)
- Directory structure matches instructions
- Astro components and layouts functional
- Build pipeline operational (site rebuilds in ~2s)

## Next Steps

1. **Continue:** Process remaining 6 papers from March 18 queue (2603.15860, 15825, 15769, 15761, 15752, 15738, 15729)
2. **Future:** Daily paper checks at ~10 AM EST on weekdays
3. **Later:** Add GitHub Action for weekly automated builds

## Recent Updates
- 2026-03-19: Processed 2603.15841 (EGS-z11-R0, first red dust-rich galaxy at z=11.45) — added 8 concept pages
- 2026-03-18: Processed 8 papers from March 18 batch
- 2026-03-17: Complete pipeline restructure, instructions centralized, structure analysis completed
- 2026-03-16: Added link-map generator and build pipeline
