# Subagent Task: Process ArXiv Papers with Full Model Switching

## Overview

Process a batch of arXiv papers through a 6-step pipeline with **full model switching** using `sessions_send()`. Each paper produces a complete analysis file at `data/papers/[doi].md` with:
- Metadata extraction (GPT)
- Section-by-section content summarization (Sonnet)
- Concept & citation connection mapping (GPT)
- Background gathering (GPT)
- Critical analysis & reasoning (Opus)

The canonical workflow reference is `instructions/SUBAGENT_PARSE_WORKFLOW.md`. This file provides the concrete `sessions_send()` implementation.

## Prerequisites

Your subagent session has access to:
- `web_fetch()` — fetch HTML and PDF from arXiv
- `exec()` — run shell commands
- `Read()` / `Write()` — file operations
- **`sessions_send()`** — invoke other models (GPT, Sonnet, Opus)

## Task: Process Papers [BATCH_NUMBER: PAPERS]

**Working directory:** `/home/node/.openclaw/workspace/projects/arxiv-atlas/`

**Papers to process:**
[LIST OF ARXIV IDS]

---

## Pipeline: 6 Steps with Model Switching

### Step 1: Fetch Paper [GPT - github-copilot/gpt-5-mini]

Use `web_fetch()` locally:
```python
# Fetch abstract page
abs_page = web_fetch(f"https://arxiv.org/abs/{arxiv_id}")
# Try HTML first
html_page = web_fetch(f"https://arxiv.org/html/{arxiv_id}")
# If no HTML, try PDF
if "not available" in html_page:
    pdf_page = web_fetch(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    paper_text = extract_text_from_pdf(pdf_page)
else:
    paper_text = html_page
```

If neither HTML nor PDF can be fetched, return "Failed to fetch the paper" and skip to the next paper.

**Output:** Full paper text (HTML or PDF-extracted)

---

### Step 2: Extract Metadata [GPT - github-copilot/gpt-5-mini]

Use `sessions_send()` to invoke GPT for structured extraction:

```python
metadata_prompt = f"""
Extract metadata from this arXiv paper.

{paper_text[:2000]}  # First 2000 chars include title, authors, abstract, DOI

Return EXACTLY in this format:

# Metadata

* **Title:** [title]
* **Authors:** [full author list]
* **arXiv ID:** {arxiv_id}
* **DOI:** [doi if present, or leave blank]
* **Submitted date:** [YYYY-MM-DD]
* **Comments / status:** [comments from arXiv, or leave blank]
* **Abstract:** [full abstract text]
"""

result = sessions_send(
    label="gpt",
    message=metadata_prompt,
    timeoutSeconds=30
)
```

Write the result as the first section to `data/papers/{doi}.md`. **Compact context.**

**Output:** Structured metadata section written to file.

---

### Step 3: Summarize Content [Sonnet - anthropic/claude-sonnet-4-5]

The paper is split into sections by main headings. **Analyze each section one by one**, compacting context to ~1k tokens after each section.

For each section, use `sessions_send()` to invoke Sonnet:

```python
section_prompt = f"""
You are analyzing one section of an arXiv paper. Extract:

1. **3–5 key claims/findings** with specific evidence
2. **Key concepts** mentioned (e.g., bar formation, AGN feedback, ram pressure stripping).
   Note if a wiki page exists at src/pages/pages/[concept].astro.
3. **Every reference cited in this section**: first author, DOI, and the claim
   this citation supports — one sentence each.

SECTION TEXT:
{section_text}

Return as:

## {section_name}

### Key claims
- [claim 1 with evidence]
- [claim 2 with evidence]
...

### Concepts and connections
- [concept 1] — [exists/missing on wiki]
- [concept 2] — [exists/missing on wiki]
"""

result = sessions_send(
    label="sonnet",
    message=section_prompt,
    timeoutSeconds=60
)
```

After processing all sections, compile a **Citations** section from references gathered across all sections:

```
## Citations

* [DOI] [First author] [main concept]: statement [] []
* [DOI] [First author] [main concept]: statement [] []
```

The two trailing bracket pairs will be filled in Step 4.

Append all section summaries and citations to `data/papers/{doi}.md`. **Compact context before moving to Step 4.**

**Output:** Section-by-section summary with citations appended to the analysis file.

---

### Step 4: Make Connections [GPT - github-copilot/gpt-5-mini]

For each citation in the Citations section:

```python
connections_prompt = f"""
For each reference listed below, do the following:
1. Retrieve the citation's DOI from the paper's bibliography
2. Summarize the context of the citation in one short sentence
3. Check if a page exists at src/pages/pages/[doi].astro

CITATIONS TO RESOLVE:
{citations_from_step3}

For each, return the updated line:
  [DOI] [First author] [main concept]: statement [x]
if the page exists, or:
  [DOI] [First author] [main concept]: statement []
if it does not.

Also check each key concept from the analysis. Note if a wiki page
exists at src/pages/pages/[concept_slug].astro.
"""

result = sessions_send(
    label="gpt",
    message=connections_prompt,
    timeoutSeconds=30
)
```

Update the Citations section in `data/papers/{doi}.md` with resolved markers. **Compact context to ~1k tokens.**

**Output:** Updated citations with exist/missing markers.

---

### Step 5: Gather Background [GPT - github-copilot/gpt-5-mini]

```python
background_prompt = f"""
For these identified concepts and connected papers, gather relevant
background from the local wiki at src/pages/pages/.

CONCEPTS: {concepts_from_step3}
CONNECTED PAPERS WITH WIKI PAGES: {existing_pages_from_step4}

For each related wiki page found:
- Read the page content
- Note key claims relevant to this paper
- Note papers cited on those pages (if their pages also exist)

Return as:
## Background
- [page slug]: [brief relevance to this paper]
- [page slug]: [brief relevance to this paper]
"""

result = sessions_send(
    label="gpt",
    message=background_prompt,
    timeoutSeconds=30
)
```

Append the Background section to `data/papers/{doi}.md`. **Compact context to ~1k tokens.**

**Output:** Background section with wiki connections.

---

### Step 6: Critical Analysis [Opus - anthropic/claude-opus-4-6]

Use `sessions_send()` to invoke Opus for deep reasoning:

```python
analysis_prompt = f"""
You are a research scientist and a peer of these authors. Read this
complete paper analysis and answer critically, thoughtfully, and thoroughly.

PAPER ANALYSIS:
{complete_analysis_from_steps_1_5}

Answer these questions:

1. **Key claims & findings** (3–5)
   - What are the most important claims? What evidence supports them?

2. **Papers/statements/concepts this paper SUPPORTS**
   - Note specific concept page slugs where relevant.

3. **Papers/statements/concepts this paper CONTRADICTS**
   - Note specific concept page slugs. How strong is the contradiction?

4. **How should existing concept pages change to incorporate this paper?**
   - Which pages to update and how?
   - New concept pages to create?

Return as:

## Analysis

### Key Findings
- [Finding 1 with evidence]
- [Finding 2 with evidence]

### Supports
- [concept page slug]: [how this paper supports it]

### Contradicts
- [concept page slug]: [contradiction details]

### Wiki Update Recommendations
- Create page: [concept] — [reason]
- Update page: [concept page slug] — [what to add/change]
"""

result = sessions_send(
    label="opus",
    message=analysis_prompt,
    timeoutSeconds=120  # Opus may take longer
)
```

Write the Analysis section as the final section of `data/papers/{doi}.md`.

**Return to the main agent and end processing.** The main agent handles writing wiki pages, updating the database, and rebuilding the site.

---

## Output File Format

After each paper completes all 6 steps, the file at `data/papers/{doi}.md` should contain:

```markdown
# Metadata

* **Title:** ...
* **Authors:** ...
* **arXiv ID:** XXXX.XXXXX
* **DOI:** ...
* **Submitted date:** YYYY-MM-DD
* **Comments / status:** ...
* **Abstract:** ...

# Contents

## [Section 1 heading]

### Key claims
- ...

### Concepts and connections
- ...

## [Section 2 heading]
...

## Citations

* [DOI] [First author] [main concept]: statement [x]
* [DOI] [First author] [main concept]: statement []
* ...

## Background
- [page slug]: [relevance]
- ...

## Analysis

### Key Findings
- ...

### Supports
- ...

### Contradicts
- ...

### Wiki Update Recommendations
- ...
```

---

## Key Constraints

- **SWITCH MODELS** as specified — use `sessions_send()` to invoke Sonnet (Step 3) and Opus (Step 6)
- **Compact context** between steps and after each section (~1k tokens) — re-read `SUBAGENT_PARSE_WORKFLOW.md` after each compaction
- **Every factual statement must cite** a source (the paper being processed, or a paper it cites via DOI)
- **Do NOT** write wiki pages or update the database — produce analysis files only
- **PDF fallback:** If HTML unavailable, fetch and extract text from PDF
- **If paper cannot be fetched**, skip with error note and continue to next

---

## Success Criteria

✅ All papers in batch processed
✅ All 6 steps executed for each paper
✅ Model switches (Sonnet for Step 3, Opus for Step 6) invoked via `sessions_send()`
✅ Output files created at `data/papers/[doi].md`
✅ Each file contains: Metadata, Contents (per-section), Citations, Background, Analysis
✅ Citations resolved with exist `[x]` / missing `[]` markers

---

## Example `sessions_send()` Call

```python
from sessions_send import sessions_send  # If available in subagent context

response = sessions_send(
    label="sonnet",  # Can also use full model name
    message=your_prompt_here,
    timeoutSeconds=60
)

# response will contain the model's output
extracted_text = response  # Use directly or parse as needed
```

---

## After Subagent Completes

The main agent will:
1. Review analysis files in `data/papers/` for quality
2. Create/update wiki pages per the Analysis recommendations (see `ARXIV_WORKFLOW.md` §5)
3. Update `data/arxiv.db` (see `DATABASE.md`)
4. Mark each paper as done in `data/papers/tracking/YYYY-MM-DD_analyzed.md`
5. Rebuild site via `tools/build_site.py`
