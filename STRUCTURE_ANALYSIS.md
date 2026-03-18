# ArXiv Atlas Structure Analysis
**Date:** 2026-03-17  
**Analyst:** Fai

## Overview

Reviewed all instruction files in `instructions/` against the current project structure. Found several inconsistencies that need resolution.

---

## ❌ Major Inconsistencies

### 1. **Missing `src/pages/pages/` directory**

**Instructions reference:** Multiple files (ARXIV_WORKFLOW.md, ARXIV_PARSE_WORKFLOW.md, SUBAGENT_PARSE_WORKFLOW.md) instruct creating pages at:
- `src/pages/pages/[arxiv_id].astro` (paper pages)
- `src/pages/pages/[concept_slug].astro` (concept pages)
- `src/pages/pages/daily_YYYY_MM_DD.astro` (daily summaries)

**Current structure:** 
```
src/pages/
├── index.astro
└── _template.astro
```

**Problem:** The `pages/` subdirectory doesn't exist. Instructions tell subagents to write to a location that doesn't exist.

**Fix needed:** Either:
- Create `src/pages/pages/` directory, OR
- Update all instructions to use `src/pages/` directly

---

### 2. **Missing `data/papers/` directory**

**Instructions reference:** Multiple files specify:
- `data/papers/YYYY-MM-DD_analyzed.md` (tracking files)
- `data/papers/[descriptive_name].md` (analysis files)
- `data/temp/[arxiv_id].md` (subagent working files)

**Current structure:**
```
data/
└── arxiv.db
```

**Problem:** No `papers/` or `temp/` subdirectories exist.

**Fix needed:** Either:
- Create `data/papers/` and `data/temp/` directories, OR
- Update instructions to specify different paths (e.g., `papers/` at root level)

---

### 3. **Template location mismatch**

**Instructions say:** `src/pages/pages/_template.astro`  
**Actual location:** `src/pages/_template.astro`

**Problem:** Subagents looking for the template at the instructed path will fail.

**Fix needed:** Move template to match instructions OR update all instruction references.

---

### 4. **Database location inconsistency**

**Instructions reference:** `data/arxiv.db` (DATABASE.md, ARXIV_WORKFLOW.md, SUBAGENT_PARSE_WORKFLOW.md)  
**Current structure:** 
- `data/arxiv.db` ✅ (correct, new database)
- `arxiv_atlas.db` (old database at project root)

**Status:** ✅ This is correct. Old database preserved for reference.

---

## ⚠️ Minor Issues

### 5. **Reference to non-existent example files**

**ARXIV_PARSE_WORKFLOW.md says:**
> "see `data/papers/zheng2026_bulges_bar_formation.md` as a template"

**Current structure:** This file exists in `data_old/papers/` but not in active `data/papers/`.

**Fix needed:** Either:
- Copy an example file to `data/papers/` for reference, OR
- Update instruction to point to `data_old/papers/zheng2026_bulges_bar_formation.md`

---

### 6. **Subagent working directory assumptions**

**SUBAGENT_PARSE_WORKFLOW.md specifies:**
- Working directory: `/home/node/.openclaw/workspace/projects/arxiv-atlas/`
- Analysis output: `data/temp/[arxiv id].md`

**Problem:** If subagent CWD is different (e.g., workspace root), relative paths will fail.

**Fix needed:** Use absolute paths in instructions OR ensure subagents are always spawned with correct CWD.

---

## ✅ What's Correct

### Components
- ✅ `src/components/WikiLink.astro` exists as documented
- ✅ `src/components/Sidebar.astro` exists as documented

### Layouts
- ✅ `src/layouts/Base.astro` exists as documented

### Data exports
- ✅ `src/data/` exists with all expected JSON files:
  - `links.json`
  - `stats.json`
  - `pages_index.json`
  - `papers_index.json`
  - `recent_papers.json`
  - `daily_summary_pages.json`
  - `paper_pages.json`
  - `page_tags.json`

### Database
- ✅ `data/arxiv.db` exists with correct schema (matches DATABASE.md)
- ✅ Schema includes all documented tables: papers, pages, paper_page_links, page_links, page_tags, processing_log, meta

### Tools
- ✅ All tools documented in README_DEPLOY.md exist in `tools/`:
  - `db_access.py`
  - `db_schema.sql`
  - `export_for_site.py`
  - `generate_links.py`
  - `build_site.py`
  - `extract_and_insert_page_links.py`
  - `create_placeholder_pages.py`
  - `sync_pages_from_disk.py`
  - `generate_daily_summary.py`
  - `patch_astro_links.py`

---

## 📋 Recommended Actions

### ✅ COMPLETED (2026-03-17 20:48 UTC)

**Fixed directory structure to match instructions:**
```bash
cd /home/node/.openclaw/workspace/projects/arxiv-atlas
mkdir -p src/pages/pages
mkdir -p data/papers
mkdir -p data/temp
mv src/pages/_template.astro src/pages/pages/_template.astro
cp data_old/papers/zheng2026_bulges_bar_formation.md data/papers/
```

**Verification:**
- ✅ Export tools run successfully
- ✅ Link map generation works
- ✅ Site builds successfully (1 page in 1.09s)
- ✅ All paths now match instruction documentation

### Remaining recommendations:

**Priority 3:** Update SUBAGENT_PARSE_WORKFLOW.md
- Change all relative paths to absolute paths, OR
- Add explicit CWD requirement at the top

**Priority 4:** Add pre-flight checks to main workflow
Before spawning subagents, verify:
- Required directories exist
- Database is accessible
- Template file exists at expected location

---

## 🔍 Database State Analysis

**Current state (data/arxiv.db):**
- Papers: 0 entries
- Pages: 11 entries (template/portal pages only)

**Pages in database:**
```
index | page
_template | page
pages/another-topic | concept
pages/author-year | concept
pages/galaxy-bimodality | concept
pages/portal-galaxy-evolution | concept
pages/random | concept
pages/related-concept | concept
pages/related-page | concept
pages/tag-concept | concept
pages/tag-galaxy-evolution | concept
```

**Observation:** These are placeholder/template entries. No real paper or concept pages yet.

**Old database (arxiv_atlas.db):** Contains historical data from previous workflow (53 analyzed papers).

---

## Summary

The instructions are **comprehensive and well-designed**, but the directory structure needs to be aligned. The simplest fix is to create the missing directories (`src/pages/pages/`, `data/papers/`, `data/temp/`) and move the template file to match the documented structure.

All tools, components, and database schema are correct and ready to use. Once directory structure is fixed, the pipeline should work as documented.

---

**Recommendation:** Go with **Option A** (create directories to match instructions) to preserve the well-thought-out instruction set without requiring extensive documentation rewrites.
