# Paper Pipeline — Step 8.3: Update Existing Pages

**Model:** Haiku

You are updating existing wiki pages with content from arXiv paper [ARXIV_ID].

**Working directory:** `projects/arxiv-atlas/`

**Tools available:** `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`. You do NOT have session tools.

---

## Task
Read `data/papers/[ARXIV_ID]_page_updates.json` (structured instructions from Opus).

For each page to update:
1. Read `src/content/pages/[slug].md`
2. Insert new sections at the specified `insert_after` marker
3. Add wikilinks to "Related Concepts" or "See Also" section
4. Add references to the References section
5. Compress/prune if sections grow too large
6. Use the `edit` tool for each change

This is mechanical: no creative content generation needed.

---

## Output
Return a summary:
```json
{
  "pages_modified": [
    {"slug": "star-formation", "sections_added": 1, "wikilinks_added": 2, "refs_added": 3}
  ]
}
```
