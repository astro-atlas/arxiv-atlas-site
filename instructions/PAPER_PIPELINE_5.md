# Paper Pipeline — Steps 6, 7 & 8: Critical Analysis + Key Takeaways + Write Pages

**Model:** Opus

You are performing deep analysis and writing wiki pages for arXiv paper [ARXIV_ID].

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools. When writing, keep a professional, scientific, but not overly complicated tone. Think of writing a review or a summary of a scientific paper for peers by peers.


---

## Step 6: Critical Analysis

**Output:** `## Critical Analysis` + `## Broader context` in analysis file, and `data/papers/[ARXIV_ID]_page_updates.json`

### ⚠️ Context management
Read existing wiki pages ONE at a time. For each: read → compare and contrast to the information in this paper. Summarize your comparison in `data/papers/[ARXIV_ID].md` as `## Broader context` under subheader `### [page slug]`. Summary should be max two sentences. Then move to next. Do NOT hold multiple full pages in context.

### ⚠️ Dispute Detection
**Critical:** When you find evidence that multiple sources (papers) disagree on a claim, be explicit about it:
- Create a **Dispute** section/box in the wiki page highlighting the disagreement
- Show both sides with citations
- If there's a resolution or consensus, state it clearly
- Format: Use a `<div class="dispute">` container with subsections for each viewpoint

### Task
Read `data/papers/[ARXIV_ID].md` and relevant existing wiki pages. Answer five questions:

1. **What are 3–5 key claims and findings?** (with evidence)
2. **Which papers/concepts does this support?** (specific pages, frameworks)
3. **Which papers/concepts does this contradict?** (specific pages, challenges) — **FLAG these as potential disputes**
4. **How should existing concept pages be updated?** Output structured instructions (see below)
5. **Knowledge graph traversal:** Trace concept paths from "astronomy" down to this paper's most specific concepts. Example: astronomy → galaxy → agn → radio-jet → recollimation-shocks. Every node = a required wiki page. List ALL nodes.

### Output

Append `## Critical Analysis` to `data/papers/[ARXIV_ID].md`.

Write `data/papers/[ARXIV_ID]_page_updates.json`:
```json
{
  "pages_to_update": [
    {
      "slug": "star-formation",
      "sections_to_add": [
        {
          "title": "Interaction-Triggered Star Formation",
          "content": "Full markdown with <a href=\"#refN\">[N]</a> citations",
          "insert_after": "## Related Processes",
          "wikilinks_to_add": [
            {"text": "Galaxy mergers", "slug": "galaxy-mergers"}
          ]
        }
      ],
      "references_to_add": [
        {"id": "ref10", "author_year": "Di Matteo et al. (2007)", "title": "...", "doi": "10.xxxx/yyyy"}
      ]
    }
  ]
}
```

---

## Step 7: Key Takeaways

**Output:** `## Key Takeaways` in analysis file

### Task
Read `data/papers/[ARXIV_ID].md` (especially Critical Analysis). Synthesize:

1. **Main Results** — 3–5 bullet points (concise, science-first, each traceable to a citation)
2. **Implications** — 1 short paragraph on field-level implications, with an eye to galaxy evolution
3. **Other Works** — 1 short paragraph on how this paper fits in the broader field

Append as `## Key Takeaways` to `data/papers/[ARXIV_ID].md`.

---

## Step 8: Write Wiki Pages

**Output:** New `.md` files DIRECTLY in `src/content/pages/` + manifest JSON

### Task
Read `data/papers/[ARXIV_ID].md` (full analysis including Key Takeaways). **DIRECTLY WRITE** the following files using the `write` tool:

1. **Paper page:** `src/content/pages/[ARXIV_ID_WITH_HYPHENS].md` (convert dots to hyphens: `2603.15899` → `2603-15899.md`)
2. **New concept pages:** One `src/content/pages/[concept-slug].md` for each recommended page from the analysis

### Paper Page Structure

**Study the example:** `src/content/pages/2603-15899.md` — your page must follow this exact structure.

**Required sections (in order):**

1. **Frontmatter** (YAML):
   ```yaml
   ---
   title: "First Author et al. (Year) — Paper Title"
   pageType: paper
   status: done
   ---
   ```

2. **Page title + infobox** (HTML table with paper metadata):
   - Authors (abbreviated with "et al." if >6)
   - arXiv ID (linked)
   - Submitted date
   - Journal (if applicable)
   - Type (e.g., "Observational — multi-wavelength")
   - Instruments
   - **Key concepts (max 4!)** — wikilinked list from Recommended Pages (NOT more than 4)

3. **Key Takeaways box** (`.key-takeaways` div):
   - Main Results (3–6 bullets, each with inline citations)
   - Implications (1 paragraph)
   - Other works (1 paragraph on literature context)
   
   Copy directly from the `## Key Takeaways` section of the analysis file.

4. **Summary** (`<h2 id="summary">`): 2–3 paragraph overview of the paper

5. **Key Findings** (`<h2 id="findings">`): Organized by theme, each subsection with:
   - Descriptive heading
   - Evidence with citations
   - Wikilinks to related concepts

6. **Methodology** (`<h2 id="methodology">`): Instruments, techniques, data sources

7. **Literature Context** (`<h2 id="literature">`): How this fits in the field

8. **What This Paper Supports** (`<h2 id="supports">`): Bullet list with wikilinks

9. **What This Paper Challenges** (`<h2 id="challenges">`): Bullet list (if applicable)

10. **References** (`<div class="references">`, NOT collapsible):
    - Numbered list matching all `<a href="#refN">[N]</a>` citations
    - **Reference format: regular text (NOT superscript)**, e.g. `[1]` or `[1,3,4]` for multiple
    - Format: `<li id="refN">Author(s) (Year). "Title." Journal/arXiv. DOI link.</li>`
    - References must always be visible (NOT in `<details>` tag)

### Concept Page Structure

**Study the example:** `src/content/pages/agn-feedback.md`

**Required sections:**

1. **Frontmatter**:
   ```yaml
   ---
   title: "Concept Name"
   pageType: concept
   status: done
   level: foundational|intermediate|specialist
   ---
   ```

2. **Title + infobox** with concept metadata

3. **Opening paragraph** (definition + importance)

4. **Thematic sections** (H2 headers) with evidence from literature

5. **References** (same format as paper pages)

### Formatting Rules

- **Every claim** must cite: `<a href="#refN">[N]</a>` (can cite multiple: `[1][2][3]`)
- **WikiLinks:** `<a href="/pages/slug" class="wikilink">Text</a>`
- **No LaTeX:** Use HTML entities (`&times;`, `&asymp;`, `&ge;`) and tags (`<sup>`, `<sub>`)
- **No blank lines** inside HTML blocks (divs, tables)
- **Exhaustive references:** Include ALL cited works from the analysis file

### Output

After writing all files, save a manifest to `data/papers/[ARXIV_ID]_manifest.json`:

```json
{
  "arxiv_id": "[ARXIV_ID]",
  "title": "Paper Title",
  "authors": ["Author 1", "Author 2"],
  "date": "YYYY-MM-DD",
  "doi": "10.xxxx/yyyy",
  "status": "done",
  "pages_created": [
    {
      "slug": "2603-15869",
      "type": "paper",
      "title": "Short title for page listings",
      "level": null
    },
    {
      "slug": "concept-slug",
      "type": "concept",
      "title": "Concept Name",
      "level": "foundational|intermediate|specialist"
    }
  ],
  "analysis_file": "data/papers/2603-15869.md",
  "bibliography_file": "data/papers/2603-15869_bibliography_complete.json"
}
```

**IMPORTANT:** The `pages_created` array MUST include:
- Each page you create with: `slug`, `type` (paper or concept), `title`, `level` (null for papers; foundational/intermediate/specialist for concepts)
- This is what the orchestrator uses for database ingestion

---

## URL & Link Conventions

| Target | URL | Source file |
|--------|-----|-------------|
| Home | `/` | `src/pages/index.astro` |
| Paper index | `/papers/` | `src/pages/papers.astro` |
| Random | `/random/` | `src/pages/random.astro` |
| Concept page | `/pages/<slug>/` | `src/content/pages/<slug>.md` |
| Paper page | `/pages/<id>/` | `src/content/pages/<id>.md` |
| Portal | `/pages/portal-<theme>/` | `src/content/pages/portal-<theme>.md` |

**Rules:**
1. All wiki pages in `src/content/pages/` → routed at `/pages/...`
2. Top-level utility pages in `src/pages/`
3. Kebab-case only
4. `<a href="/pages/slug" class="wikilink">` for cross-references
5. arXiv IDs: hyphens in slugs/filenames (`2603-16183`), dots in display (`arXiv:2603.16183`)
