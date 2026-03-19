# ArXiv Parse Workflow

This is the definitive reference for how we ingest, process, and record arXiv papers in the Atlas.

---

## 1. Where is the queue of papers to analyze?

**File:** `data/papers/YYYY-MM-DD_analyzed.md`

Each date has a tracking file (e.g., `data/papers/2026-03-13_analyzed.md`) that lists every astro-ph.GA paper from that day. Papers are listed with checkboxes:

- `[x]` = analyzed and done
- `[ ]` = still in the queue, waiting to be processed

Example:
```
## Completed
1. ✅ arXiv:2603.12121 - Zheng et al. - "Bar Formation..."

## To Analyze
- [x] arXiv:2603.12219 - Huston et al. - "SynthPop..."
- [ ] arXiv:2603.12070
- [ ] arXiv:2603.11899
```

**The unchecked `[ ]` entries are the queue.** Start from the top and work down.

Cross-listed papers (from other arXiv categories) are noted at the bottom and skipped.

---

## 2. What to do to process each paper

For each unchecked `[ ]` paper in the queue, perform these steps in order:

### Step 1: Fetch the paper
- Fetch the arXiv abstract page: `https://arxiv.org/abs/XXXX.XXXXX`
- Fetch the full HTML text: `https://arxiv.org/html/XXXX.XXXXXv1`
- If HTML is unavailable, note this and work from the abstract + PDF extraction.

### Step 2: Extract metadata
From the abstract/HTML page, extract:
- **Title**
- **Authors** (full list)
- **arXiv ID** (e.g., `2603.12070`)
- **DOI** (if present)
- **Submitted date**
- **Abstract** (full text)
- **References** (list of DOIs/arXiv IDs from the bibliography at the end)

### Step 3: Analyze content
Read the paper and identify:
- **3–5 key claims/findings** with specific evidence
- **Key concepts** mentioned (e.g., bar formation, AGN feedback, ram pressure stripping)
- **Connections** to existing Atlas pages (check `src/pages/pages/` for what already exists)

### Step 4: Create the analysis file
Write a structured analysis to `data/papers/[descriptive_name].md` following the format of existing files (see `data/papers/zheng2026_bulges_bar_formation.md` as a template). Include:
- Title, authors, arXiv ID, date, status
- Abstract summary
- Key findings (organized by theme)
- Implications
- List of wiki pages to create/update

### Step 5: Create/update the paper page on the wiki
Create an Astro page at `src/pages/pages/[author]_[year]_[short_topic].astro` using the template at `src/pages/pages/_template.astro`. The page must include:
- Paper metadata block (authors, arXiv ID with link, date, status)
- Abstract box
- Key findings sections with `<WikiLink>` components linking to concept pages
- Related concepts list
- **References section** — every factual claim must cite the paper or papers it references
- Tags

### Step 6: Create/update concept pages
For each key concept identified in Step 3:
- If a page already exists in `src/pages/pages/`, update it with new information from this paper (add claims, update references)
- If no page exists, create one using `_template.astro` as the base
- **Every factual statement must have an inline citation** (to the paper being processed, or to papers it cites via DOI)
- Flag anything unsourced as `[citation needed]`

### Step 7: Update the database
All DB operations target: `data/arxiv.db`

**a) Insert or update the paper:**
```sql
INSERT INTO papers (arxiv_id, title, authors, abstract, doi, submitted_date, processed_date, status, summary_path)
VALUES ('<arxiv_id>', '<title>', '<authors>', '<abstract>', '<doi>', '<date>', datetime('now'), 'done', '<path_to_analysis_md>');
```

**b) Insert page entries:**
```sql
INSERT OR IGNORE INTO pages (page_slug, title, page_type, source_paper_id, path)
VALUES ('pages/<slug>', '<title>', '<paper|concept>', <paper_id>, '<path_to_astro_file>');
```

**c) Link paper to pages:**
```sql
INSERT OR IGNORE INTO paper_page_links (paper_id, page_id, role)
VALUES (<paper_id>, <page_id>, '<primary|related>');
```

**d) Register concept-to-concept links:**
```sql
INSERT INTO page_links (source_page_id, target_page_slug, link_text)
VALUES (<source_id>, 'pages/<target_slug>', '<display_text>');
```

**e) Log the processing:**
```sql
INSERT INTO processing_log (paper_id, attempt, status, message)
VALUES (<paper_id>, 1, 'done', 'Processed successfully. Created pages: [list]. Updated pages: [list].');
```

---

## 3. How to record that a paper has been processed

Three places must be updated:

### a) The tracking file (`data/papers/YYYY-MM-DD_analyzed.md`)
Change the paper's checkbox from `[ ]` to `[x]` and add its title:
```
- [x] arXiv:2603.12070 - Author et al. - "Paper Title"
```
If it's a major paper, also add it to the `## Completed` section at the top with a ✅.

### b) The database (`data/arxiv.db`)
- `papers` table: row with `status = 'done'` and `processed_date` set
- `processing_log` table: row with `status = 'done'` and a message listing created/updated pages

### c) The wiki filesystem
- Paper page exists at `src/pages/pages/<slug>.astro`
- Analysis file exists at `data/papers/<descriptive_name>.md`
- Any new concept pages exist at `src/pages/pages/<concept_slug>.astro`

---

## 4. After finishing all papers for a date: Daily Summary

Once every `[ ]` entry for a date is checked off:

1. Create a daily summary page at `src/pages/pages/daily_YYYY_MM_DD.astro`
2. The summary must:
   - Identify 3–4 key research areas/themes from that day's papers
   - Group papers under those themes with 1–2 sentence summaries each
   - Link to each paper's wiki page via `<WikiLink>`
3. Insert a `pages` row in the DB for the summary (page_type: 'daily_summary')
4. Update `src/data/daily_summaries.json` with the new entry
5. Ensure the "Daily Summaries" portal page links to the new summary

---

## 5. Future: Weekly & Monthly Summaries

- Aggregate daily summaries into weekly and monthly pages
- Track counts per research area, notable disagreements, candidate review papers
- To be implemented after daily workflow is stable

---

## 6. Site rebuild

After processing papers and creating pages, rebuild the site:
```bash
cd projects/arxiv-atlas
python tools/build_site.py
```
This runs: `export_for_site.py` → `generate_links.py` → `npm run build`

Output goes to `dist/` (static HTML, ready for GitHub Pages).

---

## Quick Reference

| What | Where |
|------|-------|
| Paper queue | `data/papers/YYYY-MM-DD_analyzed.md` (unchecked `[ ]` items) |
| Analysis files | `data/papers/<name>.md` |
| Wiki paper pages | `src/pages/pages/<author>_<year>_<topic>.astro` |
| Wiki concept pages | `src/pages/pages/<concept_slug>.astro` |
| Page template | `src/pages/pages/_template.astro` |
| Database | `data/arxiv.db` |
| Daily summaries | `src/pages/pages/daily_YYYY_MM_DD.astro` + `src/data/daily_summaries.json` |
| Site build script | `tools/build_site.py` |
| Built site | `dist/` |

---

---

## Appendix A: Sub-Agent Architecture & Workflow

### Overview
Each paper gets a dedicated sub-agent that analyzes content and proposes wiki updates. Main agent reviews and approves all changes.

### Sub-Agent Execution Flow

When a sub-agent processes a paper, it:

1. **Fetches the paper** (HTML from arXiv abstract page, falls back to PDF)
2. **Analyzes and identifies key concepts** (3-7 concepts that should have wiki pages)
3. **For each concept:**
   - Checks if wiki page exists (`src/pages/pages/{concept}.astro`)
   - If exists: reads it to understand current content
   - Drafts new content or updates
4. **Returns a structured proposal:**
   ```json
   {
     "paper": {
       "title": "...",
       "authors": [...],
       "arxiv_id": "...",
       "year": 2026
     },
     "concepts": [
       {
         "name": "Concept Name",
         "action": "create" | "update",
         "existing_page": true | false,
         "proposed_content": "...",
         "changes_summary": "..."
       }
     ],
     "new_paper_summary": "..."
   }
   ```

### Main Agent Review
- Examine each proposed change
- For updates: compare old vs new content
- Approve, modify, or reject each proposal
- Execute approved changes
- Store paper summary in `data/papers/`

### Conflict Resolution
If multiple sub-agents touch the same page:
- Main agent holds the lock (sequential processing)
- Or: sub-agents return proposals, main agent merges intelligently

---

## Appendix B: Sub-Agent Task Template (Batch Processing)

When spawning a sub-agent to process a batch of papers, use this as the task prompt:

```
Goals:
- Claim and process all papers in the [DATE] queue (in data/arxiv.db / projects/arxiv-atlas/).
- For each paper, in order:
  1. Fetch the paper (prefer HTML, fall back to PDF->text).
  2. Extract title, authors, abstract, DOI/arXiv id, references (DOIs), and main sections.
  3. Identify key concepts and 3–5 main claims/findings.
  4. Create or update a paper page (pages table + on-disk file under src/pages/pages/) with:
     - 1-paragraph summary
     - Structured metadata (authors, arXiv id, DOI, date)
     - Extracted key claims with inline citations to the paper (and cited DOIs where relevant)
  5. Create/update concept pages referenced by the paper and register page_links
     (concept↔concept and paper↔page).
  6. Commit all DB changes transactionally to
     /home/node/.openclaw/workspace/projects/arxiv-atlas/data/arxiv.db.
  7. Produce a verification report: created/updated pages, page_links added,
     any missing references flagged.

- After finishing all papers for the date, create a daily summary page in the wiki
  and an entry in the DB. The daily summary should:
  * Identify 3–4 key areas explored that day
  * Group the day's papers under those areas with 1–2 sentence summaries
  * Provide internal wiki links to the paper pages

- Export/update src/data/daily_summaries.json and ensure files are on-disk for site build.

Constraints & Rules:
- Use the GPT model (github-copilot/gpt-5-mini) for all analysis steps with thinking=high.
- Perform tasks sequentially to avoid DB contention.
- Every factual statement on any created page must include an inline reference
  (the paper itself or cited DOIs). If a fact lacks sourcing, mark as [citation needed].
- If npm build or other errors occur, capture logs and report them back to the main session.
- Update data/papers/YYYY-MM-DD_analyzed.md as each paper is completed (check off the box).

Working directory: /home/node/.openclaw/workspace
DB path: /home/node/.openclaw/workspace/projects/arxiv-atlas/data/arxiv.db
Queue: unchecked [ ] entries in data/papers/YYYY-MM-DD_analyzed.md

Key references:
- Read ARXIV_PARSE_WORKFLOW.md for the full processing workflow
- Use src/pages/pages/_template.astro as the page template
- See data/papers/zheng2026_bulges_bar_formation.md for analysis file format
- See src/pages/pages/zheng_2026_bar_formation.astro for paper page format

Deliverables (one-shot run):
- For each paper: paper page file, analysis md, DB updates, verification report.
- Daily summary page for the date and updated src/data/daily_summaries.json.
- A final run report listing processed papers and any issues.
```

---

## Appendix C: Standing Instructions from Sai

These are standing instructions that apply to all ArXiv Atlas work:

1. **Model choice:** Use the GPT model (github-copilot/gpt-5-mini) for all parsing
   tasks/subagents during the setup phase. This is a temporary choice while we are
   still getting everything set up.

2. **Daily summaries:** At the end of parsing each day's papers, create a "[date] summary"
   page on the portal/db which should:
   - Identify 3–4 key areas explored that day
   - Split the papers into these key areas and list them under each area,
     with 1–2 sentence summaries
   - Provide links to the paper pages

3. **Daily Summaries portal:** There should be a portal page with "Daily summaries"
   on the wiki which links to these date summary pages.

4. **Weekly & Monthly summaries (future):** When we are done with daily workflow,
   we should also have "Weekly summaries" and "Monthly summaries" — to be
   implemented later.

5. **Citations everywhere:** When creating *any* page on the wiki, for any factual
   statement, add a reference from the paper being processed. Everything should be
   backed up by references as much as possible. The reference can be the paper itself,
   or any papers they cite. Use DOIs from the citation list at the end of each paper.

---

_Last updated: 2026-03-16_
