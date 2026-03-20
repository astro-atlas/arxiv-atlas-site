# Next Paper Checklist

Use this for every new paper. Copy & paste the commands.

## Before Starting

- [ ] Have arXiv ID ready (e.g., 2603.15869)
- [ ] Check internet connection
- [ ] No database locks: `lsof projects/arxiv-atlas/data/arxiv.db | wc -l` (should be 0)

## Pipeline Steps (Replace 2603.15869 with real ID)

### Step 1-2: Fetch & Metadata (30 sec)
Spawn GPT subagent to fetch source tarball and extract metadata.

**Expected output:** `/tmp/[arxiv_id]/` with `.tex` and `.bib` files

### Step 3: Section Analysis (2-3 min)
Spawn Sonnet subagent for deep reading.

**Expected output:** Analysis appended to `data/papers/[arxiv_id].md`, `_cited_keys.json` created

### Step 3c: Citation Resolution (15 sec)
Spawn GPT subagent to match citations against `.bib`.

**Expected output:** `_bibliography_complete.json` (typically 28-70 resolved)

### Steps 4-5: Wiki Connections (1 min)
Spawn Haiku subagent to find existing pages and recommend new ones.

**Expected output:** Wiki connections + recommendations appended to `.md`

### Steps 6-8: Critical Analysis & Pages (7 min)
Spawn Opus subagent to analyze critically and write wiki pages.

**Expected output:** 
- 8-10 `.md` files in `src/content/pages/`
- `_manifest.json` with `pages_created` array

### Ingest & Rebuild (1 min)

```bash
cd projects/arxiv-atlas
python3 tools/ingest_manifest.py data/papers/2603.15869_manifest.json
python3 tools/build_site.py
```

**Verify success:**
```bash
sqlite3 data/arxiv.db "SELECT arxiv_id, title FROM papers WHERE arxiv_id = '2603.15869';"
# Should return: 2603.15869 | Paper Title
```

### Cleanup (30 sec)

```bash
rm -f data/papers/2603.15869_{manifest,cited_keys,page_updates,meta,parse_note,raw_bib,keytakeaways}* \
      data/papers/2603.15869.{pdf,bib} \
      data/papers/2603.15869_critical_analysis.md
rm -rf /tmp/2603.15869/
```

**Verify cleanup:**
```bash
ls data/papers/2603.15869*
# Should only show: 2603-15869.md  2603-15869_bibliography_complete.json
```

## After All Papers Done

### Verify Site Built
```bash
open dist/pages/2603-15869/index.html
# Check title, concepts, references, disputes
```

### Check Papers Page
```bash
open dist/papers/index.html
# Verify all new papers appear with proper titles (NO duplicates)
```

### Update Memory
```bash
# Edit memory/YYYY-MM-DD.md with:
# - Papers processed today
# - Any issues encountered
# - New concepts discovered
```

## Troubleshooting

| Problem | Check |
|---------|-------|
| Database locked | `lsof data/arxiv.db` — kill any stray processes |
| Papers don't appear in `/papers/` | Verify `_manifest.json` has `pages_created` array |
| PDF text extraction failed | Normal — already handled via HTML |
| Citation resolution low (< 20 matches) | Normal for very old papers |
| Site build fails | Check for syntax errors in wiki `.md` files |
| Duplicate papers still showing | `sqlite3 data/arxiv.db "DELETE FROM pages WHERE page_slug LIKE 'papers/%';"` |

## Time Budget

- Total per paper: **12-15 minutes**
  - Fetch: 0.5 min
  - Analysis: 2-3 min
  - Citations: 0.25 min
  - Wiki: 1 min
  - Critical + pages: 7-8 min
  - Ingest + build + cleanup: 1 min

## Documentation

If you need to understand any step:
- **Overview:** `projects/arxiv-atlas/QUICK_START.md`
- **Complete reference:** `projects/arxiv-atlas/STATUS_2026-03-19.md`
- **Detailed instructions:** `projects/arxiv-atlas/instructions/PAPER_PIPELINE_*.md`

---

**Ready?** Pick an arXiv ID and go! 🚀
