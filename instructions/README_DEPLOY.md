# ArXiv Atlas — Build & Deploy

## Architecture

Static site built with Astro. Data lives in a local SQLite DB (`data/arxiv.db`). At build time, Python scripts export DB contents to JSON files under `src/data/`, which Astro imports to produce fully static HTML. No server-side logic needed — perfect for GitHub Pages.

## Data Flow

```
Sub-agents write to DB
        ↓
export_for_site.py → src/data/{stats,papers_index,pages_index,recent_papers}.json
generate_links.py  → src/data/links.json (link map with exists/missing flags)
        ↓
npm run build → dist/ (static HTML/CSS/JS)
        ↓
Deploy dist/ to GitHub Pages
```

## Link System

**WikiLink component** (`src/components/WikiLink.astro`): Renders internal links using the precomputed `links.json`.
- Existing pages → styled as `.wikilink` (normal link appearance)
- Missing pages → styled as `.wikilink.missing` (muted, dashed underline — Wikipedia-style "red links")

**How missing pages work:**
1. When a sub-agent processes a paper and identifies concepts, it inserts records into the `page_links` table (source_page_id → target_page_slug)
2. If the target concept doesn't have a page yet, `create_placeholder_pages.py` creates a DB record with `metadata_json = {"placeholder": true}` and `path = NULL`
3. `generate_links.py` checks which slugs have actual `.astro` files on disk — those without get `exists: false` in `links.json`
4. The WikiLink component reads `exists` and applies the appropriate CSS class

**To turn a red link green:** Create the `.astro` page file, then rebuild.

## Quick Local Workflow

```bash
# 1. Export data and generate link map
python3 tools/export_for_site.py
python3 tools/generate_links.py

# 2. Build static site
npm run build

# 3. Serve locally
cd dist && python3 -m http.server 8081
```

Or use the combined build script:
```bash
python3 tools/build_site.py
```

For dev with hot reload:
```bash
python3 tools/export_for_site.py && python3 tools/generate_links.py
npm run dev
```

## After Adding New Papers or Pages

```bash
# If new papers were ingested into the DB:
python3 tools/export_for_site.py

# If pages were added/removed or links changed:
python3 tools/extract_and_insert_page_links.py   # scan .astro files for links
python3 tools/create_placeholder_pages.py         # create DB records for missing targets
python3 tools/generate_links.py                   # rebuild link map

# Then rebuild:
npm run build
```

## After Converting Links on New Pages

If you've written new `.astro` pages with plain `<a href="/pages/...">` links:
```bash
python3 tools/patch_astro_links.py    # convert to <WikiLink> components
```

Note: The patcher skips links containing nested HTML (e.g., `<span>` inside `<a>`). Those should remain as plain `<a>` tags.

## Tool Scripts Reference

| Script | Purpose |
|--------|---------|
| `tools/db_access.py` | SQLite access layer (migrate, claim_paper, finish_paper, create_page, link_paper_page) |
| `tools/db_schema.sql` | Database schema (papers, pages, page_links, paper_page_links, page_tags, processing_log) |
| `tools/export_for_site.py` | Export DB → JSON files for Astro |
| `tools/generate_links.py` | Build link map (exists/missing) from DB + disk scan → links.json |
| `tools/extract_and_insert_page_links.py` | Scan .astro files for internal links → insert into page_links table |
| `tools/create_placeholder_pages.py` | Create DB records for referenced-but-missing concept pages |
| `tools/patch_astro_links.py` | Convert `<a href="/pages/...">` to `<WikiLink>` components |
| `tools/sync_pages_from_disk.py` | Ensure all .astro files have corresponding DB page records |
| `tools/generate_daily_summary.py` | Generate daily summary .astro page from DB data |
| `tools/build_site.py` | Combined: export → generate_links → npm run build |

## CI / GitHub Pages

Create a GitHub Action that runs weekly (or on push to main):
```yaml
- run: |
    python3 tools/export_for_site.py
    python3 tools/generate_links.py
    npm run build
- uses: peaceiris/actions-gh-pages@v3
  with:
    publish_dir: ./dist
```
