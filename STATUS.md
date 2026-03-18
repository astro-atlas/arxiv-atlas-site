# ArXiv Atlas Project Status

## Current Phase: Pipeline Restructure & Instructions Complete
Updated: 2026-03-17 (major reorganization by Sai)

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

**New clean database:** `data/arxiv.db`
- Papers: 0 entries (fresh start)
- Pages: 11 template/portal entries
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

✅ **Ready to process papers:**
- Complete workflow documentation in `instructions/`
- Full tool suite in `tools/`
- Clean database with correct schema
- Directory structure matches instructions
- Astro components and layouts functional
- Build pipeline operational and verified
- Example files available for reference

## Next Steps

1. **Immediate:** Fix directory structure to match instructions (create `src/pages/pages/`, `data/papers/`, `data/temp/`)
2. **Soon:** Start processing papers with new workflow
3. **Future:** Add GitHub Action for weekly automated builds

## Recent Updates
- 2026-03-17: Complete pipeline restructure, instructions centralized, structure analysis completed
- 2026-03-16: Added link-map generator and build pipeline
- 2026-03-11: Completed Astro paper pages for March 11 papers
