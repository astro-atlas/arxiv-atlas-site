# Paper Pipeline — Steps 1 & 2: Fetch + Extract Metadata

**Model:** GPT

You are processing arXiv paper [ARXIV_ID].

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools.

---

## Step 1: Fetch Paper

**Output:** Extracted source files in `/tmp/[ARXIV_ID]/`

### Task
Fetch the paper source and extract it.

1. Fetch abstract page: `https://arxiv.org/abs/[ARXIV_ID]`
2. Download source tarball: `https://arxiv.org/e-print/[ARXIV_ID]`
3. Extract to `/tmp/[ARXIV_ID]/` and locate:
   - Main `.tex` file (usually `main.tex`, `ms.tex`, or `aanda.tex`)
   - Bibliography file (`*.bib` or embedded `\begin{thebibliography}`)
4. **Fallbacks:** If tarball unavailable, try HTML (`https://arxiv.org/html/[ARXIV_ID]`) then PDF (`https://arxiv.org/pdf/[ARXIV_ID].pdf`)
5. If nothing works, return: `{"status": "failed", "error": "Failed to fetch the paper"}`

### Output
Write a summary to `/tmp/[ARXIV_ID]/fetch_result.json`:
```json
{
  "status": "ok",
  "tex_file": "/tmp/[ARXIV_ID]/main.tex",
  "bib_file": "/tmp/[ARXIV_ID]/refs.bib",
  "fallback_used": null
}
```

---

## Step 2: Extract Metadata

**Output:** First section of `data/papers/[ARXIV_ID].md`

### Task
From the abstract page and source files, extract metadata and write it as the first section of `data/papers/[ARXIV_ID].md`:

```markdown
# [ARXIV_ID]: [Title]

**Authors:** [full author list]
**arXiv ID:** [ARXIV_ID]
**DOI:** [if available]
**Submitted:** [date]
**Comments:** [if any]

## Abstract
[full abstract text]
```

**Do NOT parse the .bib file here.** Many bib files have 1000+ entries. Citation resolution happens later in a separate step.
