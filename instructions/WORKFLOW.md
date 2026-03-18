ArXiv Atlas - Workflow

1) Paper ingestion
- Daily ArXiv fetch (astro-ph.GA). Claim papers into DB per-day.
- Each paper gets a sub-agent worker (use GPT model for analysis while setup continues).
- Prefer HTML when available; fall back to PDF -> extract text.
- Deduplicate by DOI/arXiv id and title similarity.

2) Paper processing (per paper)
- Sub-agent fetches full text, extracts sections, identifies key concepts and claims.
- Create or update paper page in DB and on-disk wiki pages (pages table + filesystem).
- Register page_links for concept↔concept and paper↔page links.
- Commit to data/arxiv.db (transactional); sub-agent reports summary and created pages.

**Citation rule (CRITICAL):** Every factual statement on any wiki page MUST include a reference.
- The reference can be the paper being processed, or any paper it cites.
- Use DOIs from the paper's reference list to identify cited works.
- Format: inline citation linking to the paper page or DOI.
- No unsourced claims. If a fact can't be traced to a specific paper, flag it as [citation needed].
- This applies to concept pages, paper pages, summary pages — everything.

3) Daily summary pages (NEW - added 2026-03-16)
- At end of parsing each day, create a [YYYY-MM-DD] summary page and DB entry.
- Each daily summary must:
  * Identify 3-4 key areas (themes) explored that day.
  * Split the day's papers into those key areas; list each paper under the area with a 1-2 sentence summary.
  * Provide links to the paper pages (internal wiki links) for each paper.
- Ensure there is a portal page "Daily summaries" on the wiki that links to these date pages.
- Daily summaries are exported into src/data/daily_summaries.json for site build.

4) Weekly & Monthly summaries (future)
- Aggregate daily summaries into weekly and monthly pages.
- Metadata: counts per area, notable disagreements, candidate review papers.

5) Site build
- Run tools/build_site.py after DB updates to export JSON and rebuild the static site.
- CI: add a weekly scheduled GitHub Action to run the export + build and deploy to gh-pages.

6) Notes
- Use GPT model for analysis tasks in this setup phase (as requested by Sai).
- Maintain transactions in sqlite (WAL) and simple retry/backoff for writers.
- Track processed paper dates in processing_log table.

Last updated: 2026-03-16
