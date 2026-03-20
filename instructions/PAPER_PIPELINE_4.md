# Paper Pipeline — Steps 4 & 5: Wiki Connections + Page Recommendations

**Model:** GPT

You are checking wiki connections and recommending pages for arXiv paper [ARXIV_ID].

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools.

---

## Step 4: Wiki Connections

**Output:** Appended `## Wiki Connections` section in `data/papers/[ARXIV_ID].md`

### Task
1. **Read the existing page index:** Load `public/existing-slugs.json` for all page slugs and titles
2. **Read the analysis:** `data/papers/[ARXIV_ID].md`
3. For every concept and cited paper, check if a page exists. Mark `[x]` if yes, `[ ]` if no
4. **Scan the full index** for existing pages relevant to this paper that weren't identified as key concepts — these are cross-link candidates

Append results to `data/papers/[ARXIV_ID].md` as:
```markdown
## Wiki Connections

### Concepts
- [x] star-formation (exists)
- [ ] collisional-ring-galaxies (new)

### Cross-link candidates
- galaxy-mergers — relevant to merger discussion in §3
```

---

## Step 5: Page Recommendations

**Output:** Appended `## Recommended Pages` section in `data/papers/[ARXIV_ID].md`

### Task
Read the wiki connections from `data/papers/[ARXIV_ID].md`. For each missing concept, recommend:
- **Page name** (kebab-case slug)
- **Level** (foundational / intermediate / specialist)
- **Why needed**
- **Suggested first reference**
- **Related existing pages**

Also note which existing pages should be updated with content from this paper.

Append to `data/papers/[ARXIV_ID].md` as `## Recommended Pages`.
