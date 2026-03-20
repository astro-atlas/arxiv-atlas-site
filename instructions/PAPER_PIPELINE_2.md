# Paper Pipeline — Step 3: Section-by-Section Analysis

**Model:** Haiku

You are analyzing arXiv paper [ARXIV_ID] section by section.

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools.

---

## ⚠️ Context management is critical
You will analyze a long paper. Process ONE section at a time. Sections are identified by `\section{}` command in TeX. Subsections (e.g., `\subsection`, `\subsubsection`, etc) belong to their parent section and should be analyzed together. After each section, write a checkpoint and compact context.

---

## Process for each section

1. **Read ONE section** from the LaTeX source (use `grep -n` or `sed` to extract boundaries, look for `\section` tex command). **Do not split on subsections.**
2. **Analyze** and extract:
   - 3–5 key claims/findings with specific evidence
   - Key concepts across five dimensions AND three depth levels (see below)
   - Every `\cite{key}`: record the key + 1-sentence claim summary of what it supports
3. **Append** to `data/papers/[ARXIV_ID].md`:
   ```markdown
   ## Section 1: [Section Name]

   ### Key claims
   - [claim with evidence]

   ### Concepts and connections
   FOUNDATIONAL: [list]
   INTERMEDIATE: [list]
   SPECIALIST: [list]

   ### References cited
   - [citation_key]: [1-sentence claim summary]
   ```
4. **Compact context** before next section

---

## After ALL sections

- Write `data/papers/[ARXIV_ID]_cited_keys.json`:
  ```json
  [{"key": "LyndsToomre1976", "claim_summary": "Seminal work on collisional ring formation"}]
  ```
- Write `data/papers/[ARXIV_ID]_concepts.json` with all concepts by level

---

## Five concept dimensions
1. Core astronomy concepts (physical processes/phenomena)
2. Techniques and methods
3. Important objects (named clusters, galaxies, notable sources)
4. Instruments and observatories
5. Surveys and programs

## Three depth levels (ALL required)
1. **Foundational** — broadest concepts a general reader needs. Examples: "magnetic-field", "star-formation", "dust", "galaxy", "gravity"
2. **Intermediate** — grad-student level. Examples: "infrared-dark-clouds", "dust-polarimetry"
3. **Specialist** — research-level. Examples: "davis-chandrasekhar-fermi-method"

**You MUST identify foundational concepts.** Every paper touches fundamental physics — name them. Goal: a reader can traverse from "galaxy" to the most specialist topic. Every step should have a corresponding wiki page.

Name concepts directly — NO "basics", "overview", "fundamentals" suffixes.
