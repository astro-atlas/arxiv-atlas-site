# arXiv paper analysis workflow - subagent

These are the instructions to analyze a single arxiv paper for a subagent. It is essential to follow them **precisely**.

You will be passed an **arxiv id** of a paper in the format `XXXX.XXXXX`. Follow these steps. **Pay close attention to referencing and switch models as stated.**

You will be asked to compact context many times. Each time, you should full read these instructions again.

## Step 1: Fetch the paper [model: GPT]
- Fetch the arXiv abstract page: `https://arxiv.org/abs/[arxiv id]`
- Download the source tarball: `https://arxiv.org/e-print/[arxiv id]`
- Extract the tarball and locate:
  - The main `.tex` file (usually `main.tex` or `aanda.tex`)
  - The bibliography file (usually `*.bib` or embedded in the main `.tex` as `\begin{thebibliography}`)
- **If tarball is unavailable**, fall back to HTML (`https://arxiv.org/html/[arxiv id]`) or PDF (`https://arxiv.org/pdf/[arxiv id].pdf`)
- If none of these can be fetched, return "Failed to fetch the paper" and skip to next paper
- If a step fails at any point during this workflow, return early with error details

### Step 2: Extract metadata [model: GPT]
From the abstract/HTML page, extract:
- **Title**
- **Authors** (full list)
- **arXiv ID** (e.g., `2603.12070`)
- **DOI**
- **Submitted date** (should be the date you are analyzing)
- **Comments / status** (can be blank)
- **Abstract** (full text)

Write these as the first section to `data/papers/[arxiv id].md`. Compact context.

### Step 3: Summarize content [model: Sonnet]

**First: Extract the complete bibliography.** From the `.bib` file (or embedded bibliography in `.tex`), parse every entry and create a structured reference with:
- Citation key (identifier used in `\cite{}`)
- First author name
- Year (if present)
- DOI (if present)
- Single author? [x] or [] (no)

Save this as a JSON file: `data/papers/[arxiv-id]_bibliography_complete.json`

Then analyze the paper sections:

The paper is split into several sections, separated by main headings. You will analyze each section one by one, following the same steps, and compact context to ~1k tokens after each section is done.

Read each section and note down:
- **3–5 key claims/findings** with specific evidence
- **Key concepts** mentioned (both discipline-specific and broad educational concepts — think of breadth from undergraduate level to research level)
- **Every reference**: all sentences where another paper is cited. For each in-text citation, record:
  - Citation key (from the `.tex` file `\cite{}` command)
  - First author name (from bibliography JSON)
  - Year (from bibliography JSON)
  - DOI (from bibliography JSON)
  - **1-sentence claim summary** — what does this reference support or illustrate in this paper?


**Record your findings in `data/papers/[arxiv-id].md` for each section.** Follow the format below. 
Example:
```
# Particle acceleration at recollimation shocks...

## Metadata

* Title: ...
* Authors: ...
* arXiv ID: ...
* DOI: ...
* Abstract: ...

## Contents

### Introduction

#### Key claims
1. Claim with evidence
2. Claim with evidence

#### Key concepts
- Recollimation shocks (specific, physics-level)
- Shock acceleration (intermediate, research-level)
- Particle acceleration fundamentals (broad, undergraduate-level)

#### Citations
* Bromberg2011 (Bromberg, 2011, 10.1234/xxx): Provides analytic jet-cocoon formalism that this work extends to sub-relativistic regimes.
* Hillas1984 (Hillas, 1984, null): Establishes maximum energy criteria for particle accelerators.
* ...

### Results

[Similar structure: key claims, concepts, citations with 1-sentence summaries]

...
```

**Compact context before moving onto the next section.**

### Step 4: Check wiki connections [model: GPT]

For every key concept and cited paper from Step 3, check if pages are already created on the wiki.

* **Concepts:** Check `src/pages/pages/` for existing pages (both specific/physics-level AND broad/educational-level)
  - Example: if you mention "recollimation shocks", check for:
    - `recollimation-shocks.astro` (specific physics concept)
    - `shock-acceleration.astro` (intermediate concept)
    - `particle-acceleration-fundamentals.astro` (broad undergraduate concept)
  - Mark as [x] if it exists, [] if it does not

* **Papers:** For every cited paper with a DOI, check if a page `src/pages/pages/[DOI].astro` exists
  - Mark as [x] if exists, [] if not

Create a summary table or list showing:
- All concepts identified (by level: broad/undergraduate, intermediate, specialist/research)
- Which pages exist [x] and which are missing []

**Compact context to ~1k tokens.**

### Step 5: Recommend wiki pages [model: GPT]

Based on your analysis, identify which concept and paper pages need to be created or updated.

For each missing concept (from Step 4), create a recommendation with:
- **Page name** (kebab-case, e.g., `recollimation-shocks`, `shock-acceleration-mechanisms`)
- **Level** (broad/undergraduate, intermediate, specialist/research)
- **Why needed**: which claims in this paper depend on this concept?
- **Suggested first reference**: which cited papers should be linked as foundational for this concept?
- **Related pages**: what other concept pages should link to this one?

Example:
```
## Recommended Wiki Pages

### 1. Particle acceleration fundamentals
- **Level**: Broad / Undergraduate
- **Why**: Paper builds on basic acceleration physics; readers need foundational understanding
- **First reference**: Longair 1992 (10.1017/...) — comprehensive overview
- **Related pages**: [shock-acceleration], [DSA-mechanisms]

### 2. Recollimation shocks
- **Level**: Specialist / Research
- **Why**: Central mechanism of this paper
- **First reference**: Bromberg 2011 (10.xxx) — foundational analytic formalism
- **Related pages**: [jet-cocoon-systems], [particle-acceleration-fundamentals]
```

Note which existing wiki pages should be updated to incorporate findings from this paper. Compact context to ~1k tokens.

### Step 6: Critical Analysis [model: Opus]

Read through the complete summary in `data/papers/[arxiv-id].md` (metadata, sections, all citations, wiki checks, and recommended pages). Answer these four questions thoughtfully and thoroughly:

* **What are 3-5 key claims and findings of this paper?** (directly from the paper's results and conclusions, with supporting evidence)
* **Which papers/statements/concepts does this paper support?** (note specific concept pages, referenced papers, or theoretical frameworks that this work agrees with, extends, or builds upon)
* **Which papers/statements/concepts does this paper contradict?** (note specific concept pages or referenced papers that this work disagrees with or challenges)
* **How should you change existing concept pages to incorporate this paper's findings?** (for each concept page that should be updated: what specific edits or new sections should be added? which claims from this paper should be incorporated?)

Focus on mapping the paper's claims to existing knowledge and concepts. Do not evaluate the paper's scientific quality or methodological limitations — just identify how its findings connect to the broader knowledge landscape.

Write down your analysis as the final `## Critical Analysis` section of `data/papers/[arxiv-id].md`. 

Return back to the main agent and end this process. The main agent handles writing wiki pages, updating the database, and rebuilding the site.

---

## Key paths

| What | Where |
|------|-------|
| Working directory | `/home/node/.openclaw/workspace/projects/arxiv-atlas/` |
| Analysis output | `data/papers/[doi].md` |
| Wiki pages | `src/pages/pages/` |
| Page template | `src/pages/pages/_temlate.astro` |
| Existing page index | `src/data/links.json` |
| Database | `data/arxiv.db` (main agent updates this; subagent does not write to it directly) |

## Key constraints

- **Switch models as stated** in each step heading.
- **Compact context** after every section and between steps — re-read these instructions each time.
- **Every factual statement** must cite a source paper (the paper being processed, or one it cites via DOI).
- **Do not write wiki pages or update the database** — return your analysis to the main agent, which handles all writes.
- **Token budget:** keep each compacted context to ~1k tokens.
- If a step fails, return early with error details.

## Success criteria

1. ✅ Paper fetched from arXiv source tarball (or HTML/PDF fallback) and metadata extracted
2. ✅ Complete bibliography parsed into JSON with: key, first_author, year, DOI, single_author flag
3. ✅ Every section analyzed with 3-5 key claims, key concepts (at multiple levels: broad→specialist), and ALL in-text citations recorded with 1-sentence claim summaries
4. ✅ Wiki connectivity checked for all concepts (at all levels) and cited papers
5. ✅ Recommended wiki pages identified with: name, level, justification, first reference, related pages
6. ✅ Critical analysis completed answering 4 questions with specific references to concepts/papers
7. ✅ Complete `data/papers/[arxiv-id].md` with: metadata, sections, citations, wiki checks, recommendations, critical analysis returned to main agent


