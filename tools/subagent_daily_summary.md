# Sub-Agent Daily Summary Generator

This sub-agent generates a daily summary page after all papers for a date have been processed.

## Task

Generate a daily summary page for **{DATE}** that synthesizes all papers processed that day.

## Implementation (Sonnet Model)

You are a Sonnet agent. Your job:

1. **Identify papers processed on {DATE}**
   - Query or read from: `data/arxiv.db` (papers table, filtered by processing_date)
   - List all papers processed that day
   - Example: [2603.13010, 2602.45678, ...]

2. **Read concept/paper pages created for those papers**
   - For each paper, find its page in `src/pages/pages/` (.astro) or `src/content/pages/` (.mdx)
   - Read all concept pages linked to that paper
   - Extract: key claims, main arguments, central concepts
   - You now have the full context of what was discovered that day

3. **Identify 3–4 key research themes**
   - Look across ALL papers and concepts from that day
   - Ask yourself: "What are the major threads connecting these papers?"
   - Examples: "Galaxy morphological transformation", "AGN feedback mechanisms", "Stellar halo structure"
   - For each theme, list which papers/concepts belong to it
   - Write 1 sentence describing the theme

4. **Group papers under themes**
   - For each theme, list the papers that contribute to it
   - For each paper under a theme, write 1–2 sentence summary
   - Make sure each summary highlights the paper's contribution to that theme

5. **Create the daily summary page**
   - Call or run: `tools/generate_daily_summary.py --date {DATE}`
   - This creates the daily summary as MDX in `src/content/pages/daily_YYYY_MM_DD.mdx` (preferred)
   - Or as .astro in `src/pages/pages/daily_YYYY_MM_DD.astro` (legacy)
   - Verify the file was created

6. **Update database and indices**
   - Ensure `data/arxiv.db` has a row in the pages table:
     - `page_slug: "pages/daily_YYYY_MM_DD"`
     - `page_type: "daily_summary"`
     - `title: "Daily summary — YYYY-MM-DD"`
   - Verify: `sqlite3 data/arxiv.db "SELECT * FROM pages WHERE page_type='daily_summary' AND created_date LIKE '{DATE}%';"`

7. **Verify the indices**
   - Check `src/data/daily_summary_pages.json` includes the new entry
   - Check `src/data/pages_index.json` includes the new entry
   - Verify: `cat src/data/daily_summary_pages.json | grep {DATE}`

## Format & Structure

**Theme structure (in the .astro page):**
```
## Key research themes

### Theme 1: [Name]
- **Paper A** ([arxiv_id]): [1–2 sentence summary]
- **Paper B** ([arxiv_id]): [1–2 sentence summary]
- Related concepts: [link to concept pages]

### Theme 2: [Name]
...
```

**Key constraints:**
- Themes should be 3–4 max
- Each summary must be concise (1–2 sentences, max 100 words per paper)
- Link to paper pages and concept pages using <WikiLink> where possible
- Every claim should reference the source paper/concept page

## Success Criteria

✅ All papers for {DATE} identified
✅ 3–4 themes extracted and described
✅ Papers grouped under themes with summaries
✅ .astro page created and saved
✅ Database updated (pages table + indices)
✅ No broken links (all WikiLinks resolve)
✅ Return JSON with: date, file_path, papers_processed, themes_identified

## Return Format

```json
{
  "date": "{DATE}",
  "success": true,
  "file_path": "src/pages/pages/daily_YYYY_MM_DD.astro",
  "papers_processed": 7,
  "themes_identified": 4,
  "themes": [
    {"name": "Theme 1", "papers": ["2603.13010", "2602.45678"]},
    {"name": "Theme 2", "papers": ["2602.11111"]}
  ],
  "errors": []
}
```

## Key Resources

- Working directory: `/home/node/.openclaw/workspace/projects/arxiv-atlas/`
- Database: `data/arxiv.db` (use `tools/db_access.py` helpers)
- Paper pages: `src/pages/pages/`
- Concept pages: `src/pages/concepts/`
- Daily summary script: `tools/generate_daily_summary.py`
- Indices: `src/data/daily_summary_pages.json`, `src/data/pages_index.json`

## Tips

- Read the .astro files on disk to understand the paper content — don't rely on summaries alone
- Look for connections between concepts across papers — that's where themes emerge
- If a paper doesn't fit any theme, create a new theme (up to 4)
- Use proper WikiLink syntax: `<WikiLink slug="concept_name" text="Concept Name" />`

Good luck! 🌟
