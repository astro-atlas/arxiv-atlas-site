# arXiv paper workflow

This is the reference for how we ingest, process, and record arXiv papers in the Atlas. Follow this with utmost precision.

---

## 1. Fetching daily papers from arxiv.org [model: GPT]

There are many papers posted on arxiv each day. Fetch them from the arxiv website:

**URL:** `https://arxiv.org/list/astro-ph.GA/recent?skip=0&show=2000`

You will be told to fetch papers from a specific date, `YYYY-MM-DD`.

**Method:**
- The webpage lists published papers grouped by submission date
- Submission dates appear as **headers** (e.g., `Wed, 18 Mar 2026`)
- Each paper is a list item with an arxiv ID, title, and links
- **Extract all papers between the [DATE] header and the [DATE-1] header** (i.e., all papers submitted on that specific date)
- **Skip cross-listed papers** (marked with "cross-list from astro-ph.XX") — these come from other categories and are listed separately at the bottom of each date section

**Result:**
- You get a list of arxiv IDs for all primary astro-ph.GA submissions on that date
- Store them in a tracking file (see Step 2)

---

## 2. Storing the list of papers [model: GPT]

Store the list of papers to process in a markdown file.

**Markdown file:** `data/papers/tracking/YYYY-MM-DD_analyzed.md`

Each date has a tracking file (e.g., `data/papers/tracking/2026-03-13_analyzed.md`) that lists every astro-ph.GA paper from that day. Papers are listed with checkboxes:

- `[x]` = analyzed and done
- `[ ]` = still in the queue, waiting to be processed

**Add the papers you found in the queue and note their author, title, and arxiv code.**

Example:
```
2026-03-13 papers

- [x] arXiv:2603.12219 - Huston et al. - "SynthPop..."
- [ ] arXiv:2603.12070
- [ ] arXiv:2603.11899
```

**The unchecked `[ ]` entries are the queue.** Start from the top and work down.

---

## 3. Analyze each paper in order [model: GPT]

### Goal / deliverables

For each paper, your goal is to produce several deliverables:
* A wiki page summarizing the key concepts and conclusions from the paper
* Updates to existing concept pages when they are mentioned in the paper
* New concept pages, if any
* An update to the markdown paper tracker file  `data/papers/2026-03-13_analyzed.md`
* An update to the SQL database hosting wiki pages `data/arxiv.db`

### Workflow

* For each paper, spawn a subagent by passing them the arxiv id for the paper. Each subagent analyzes the content and proposes wiki updates. The subagent workflow is described in `SUBAGENT_PARSE_WORKFLOW.md`
* Each agent will write an analysis with recommended pages in `data/papers/[arxiv-id].md`
* **After subagent completes**, the main agent must:
  1. Create recommended wiki pages in `src/pages/pages/` (concept pages, paper pages)
  2. Ingest the analysis into the database (runs tools to populate `papers`, `pages`, `page_links` tables)
  3. Rebuild the site (updates counters, navigation, indexes)

---

# 4. Subagent output [model: GPT]

* If the subagent returns "Failed to fetch the paper", note `[?]` in the tracking file and let Sai know. 
* If successful, the subagent will produce a `data/papers/[arxiv-id].md` file with their complete analysis.

---

# 5. Post-processing: Wiki pages and database [model: Sonnet]

**After each subagent completes**, follow these steps to populate the wiki and database:

## Step 5.1: Create wiki pages

Based on the "Recommended Wiki Pages" section in the analysis file, create `.astro` pages in `src/pages/pages/`.

### Concept pages
Use kebab-case filenames (e.g., `shock-waves.astro`, `diffusive-shock-acceleration.astro`). Each page should include:
* Educational level (undergraduate / intermediate / research)
* Brief explanation (appropriate to that level)
* "Why this matters" section
* Key references from the paper's bibliography
* Related concept links using `<WikiLink />` component
* "See also" link back to the paper

### Paper reference pages
Create pages for frequently-cited papers (e.g., `Bromberg_2011.astro`). Include:
* Paper metadata (authors, year, DOI)
* Brief summary of key findings
* Why this paper is important
* Which concept pages reference it

**Important**: Avoid LaTeX-style math notation in `.astro` files (e.g., `p^{-q}` breaks Astro's parser). Use HTML tags instead: `p<sup>-q</sup>`.

## Step 5.2: Ingest analysis into database

Run these Python tools in sequence:

```bash
cd /home/node/.openclaw/workspace/projects/arxiv-atlas

# 1. Ingest the analysis file (creates paper + page records)
python3 tools/ingest_analysis_files.py data/papers/[arxiv-id].md

# 2. Sync .astro files to pages table
python3 tools/sync_pages_from_disk.py

# 3. Extract and insert page links
python3 tools/extract_and_insert_page_links.py
```

## Step 5.3: Rebuild the site

Run the build script to update site data files (stats, indexes, navigation) and compile the Astro site:

```bash
python3 tools/build_site.py
```

This script:
* Exports database to JSON files in `src/data/` (stats.json, recent_papers.json, papers_index.json, pages_index.json, links.json)
* Generates the links graph
* Runs `npm run build` to compile the Astro site to `dist/`

**Result**: The site now reflects:
* Updated paper count
* Updated page count
* New papers in "Recent papers"
* New concept pages in navigation
* Cross-references and backlinks

---

# 6. Daily summary and tracking [model: Sonnet]

After processing all papers for a day:

## Generate daily summary

Create a thematic summary grouping the day's papers into 3-4 key themes:

```bash
python3 tools/generate_daily_summary.py YYYY-MM-DD
```

This creates a `daily_summary_YYYY-MM-DD.astro` page that:
* Groups papers by scientific theme/topic
* Highlights connections between papers
* Notes contradictions or complementary findings

## Update tracking file

Mark all processed papers in `data/papers/tracking/YYYY-MM-DD_analyzed.md`:

```markdown
# 2026-03-18 Papers (astro-ph.GA)

- [x] 2603.16647 — Particle acceleration at recollimation shocks
- [x] 2603.16796 — ...
- [ ] 2603.16706 — (pending)
```

---

# 7. Portal organization [model: GPT]

As the wiki grows, organize related concepts into **portal pages** (similar to Wikipedia portals).

**When to create a portal:**
* 10+ papers share a common theme (e.g., "Galaxy Evolution", "AGN Feedback", "Bar Dynamics")
* Multiple concept pages cluster around a topic

**Portal structure:**
* Overview of the research area
* Key questions and open problems
* Featured papers (representative works)
* Concept index (links to all related concept pages)
* Recent papers in this area

**Portal file naming:** Portal pages live in `src/pages/pages/` with the prefix `portal-`:
* `src/pages/pages/portal-particle-acceleration-in-jets.astro`
* `src/pages/pages/portal-galaxy-evolution.astro`
* `src/pages/pages/portal-agn-feedback.astro`

**Sidebar auto-detection:** The sidebar automatically detects portal pages by matching page_slug prefix `pages/portal-`. Any new portal page will appear in the sidebar "Portals" section after the next site rebuild. No manual sidebar edits needed.

**Example portals:**
* `portal-galaxy-evolution.astro` — Structural changes, quenching, morphology
* `portal-agn-feedback.astro` — Jets, winds, energy injection
* `portal-high-redshift-galaxies.astro` — JWST, early universe, formation

---

# 8. Review and verify [model: GPT]

After each batch (daily or per paper), verify:

## Create wiki pages

When adding new content to wiki pages, make sure to 
* Add cross-references whenever possible
* Support factual statements with citations
* If relevant, always add a citation, even if the fact is already supported by a different reference. Our goal is to provide the most complete reference portal possible.

Reference aggressively. You are given a list of references in the `References` section. Whenever you state a claim, support it with a citation. Never cite a paper for a claim it did not make. Never cite a paper that is not explicitly cited in the `References` section or the Wiki portal, i.e. never cite from your own knowledge base.

The `References` section, the format is
```
[DOI] [First author] [main concept]: statement [pagelink] [exists_marker]
```
* If a paper exists on the wiki, then when citing a paper, link to its wiki page given by `[pagelink]`
* If it does not exist, note it as a stub.

### Paper page

* Create a page summarizing the paper in `src/pages/pages/[doi].astro`
* See src/pages/pages/zheng_2026_bar_formation.astro for paper page format
* Use src/pages/pages/_template.astro as the page template
* Every statement you make should be supported by a reference, if possible. Refer to the `References` section of the agent's output.
* Provide internal wiki links any pages / concepts that are relevant.

### New concept pages

* If `Analysis` states that a new concept page must be made, create that page following the same format as other concept pages `which is...?`
* Follow the format of `..............`
* Reference and cross-link carefully. Use the `References` section. 

### Update existing concept pages

* Follow the `Analysis` section of the output to carefully update the concept pages.
* If a paper supports a statement that already exists on the concept page, simply add it as a reference.
* If a paper contradicts a statement, add a `Debate` section to the concept page or subsection and use the paper as a reference.
* For each concept page you edit, also check if a paper from the `References` section can be a useful citation. If relevant, always add the citation. 

## Update the SQL database [model: Sonnet]

* Create/update concept pages referenced by the paper and register page_links (concept↔concept and paper↔page).
* Update `data/arxiv.db` with any new pages that have been added to the wiki (including new papers and concepts). The database architecture is summarized in `instructions/DATABASE.md`
* Update the `data/papers/tracking/[DATE]-analyzed.md` and mark the paper as done

---

# 6. Daily summary [model: GPT]

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

## 7. Site rebuild

After processing papers and creating pages, rebuild the site:
```bash
cd projects/arxiv-atlas
python tools/build_site.py
```
This runs: `export_for_site.py` → `generate_links.py` → `npm run build`

Output goes to `dist/` (static HTML, ready for GitHub Pages).


---

## URL & Link Conventions

All wiki content pages live in `src/pages/pages/` and are served at `/pages/<slug>/`.

**Internal links:**
| Target | URL path | Source file |
|--------|----------|-------------|
| Home | `/` | `src/pages/index.astro` |
| Paper summaries index | `/papers/` | `src/pages/papers.astro` |
| Random page | `/random/` | `src/pages/random.astro` |
| Concept page | `/pages/<concept-slug>/` | `src/pages/pages/<concept-slug>.astro` |
| Paper page | `/pages/<arxiv-id>/` | `src/pages/pages/<arxiv-id>.astro` |
| Portal page | `/pages/portal-<theme>/` | `src/pages/pages/portal-<theme>.astro` |

**Rules:**
1. **All wiki pages** (concepts, papers, portals) go in `src/pages/pages/` → routed at `/pages/...`
2. **Top-level utility pages** (papers index, random) go in `src/pages/` → routed at `/papers/`, `/random/`
3. **Never link to** `/pages/Portal_Galaxy_Evolution/` or similar PascalCase paths — use kebab-case: `/pages/portal-galaxy-evolution/`
4. **Use WikiLink component** for cross-references between wiki pages; use plain `<a>` tags for external links and top-level utility pages
5. **Portal pages** use the `portal-` prefix in their filename so the sidebar detects them automatically

---

## Quick Reference

| What | Where | URL |
|------|-------|-----|
| Paper queue | `data/papers/tracking/YYYY-MM-DD_analyzed.md` | — |
| Analysis files | `data/papers/<arxiv-id>.md` | — |
| Wiki paper pages | `src/pages/pages/<arxiv-id>.astro` | `/pages/<arxiv-id>/` |
| Wiki concept pages | `src/pages/pages/<concept-slug>.astro` | `/pages/<concept-slug>/` |
| Portal pages | `src/pages/pages/portal-<theme>.astro` | `/pages/portal-<theme>/` |
| Papers index | `src/pages/papers.astro` | `/papers/` |
| Random page | `src/pages/random.astro` | `/random/` |
| Page template | `src/pages/pages/_template.astro` | — |
| Database | `data/arxiv.db` | — |
| Daily summaries | `src/pages/pages/daily_YYYY_MM_DD.astro` | `/pages/daily_YYYY_MM_DD/` |
| Site build script | `tools/build_site.py` | — |
| Built site | `dist/` | — |

---
