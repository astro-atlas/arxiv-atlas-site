# Database Reference

The database is a SQLite file at `data/arxiv.db`.

---

## Tables

### `papers`
The primary ingest table. One row per arXiv paper.

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER PK | Auto-increment |
| `arxiv_id` | TEXT UNIQUE | e.g. `2603.12070` |
| `title` | TEXT | |
| `authors` | TEXT | JSON array of author name strings |
| `abstract` | TEXT | |
| `doi` | TEXT | May be null |
| `submitted_date` | DATE | arXiv submission date (`YYYY-MM-DD`) |
| `processed_date` | DATETIME | When the pipeline last processed this paper |
| `status` | TEXT | Pipeline state: `pending` → `processed` → `analyzed` → `done` |
| `summary_path` | TEXT | Relative path to an external summary file |
| `metadata_json` | TEXT | JSON blob for any extra metadata |
| `score` | REAL | Curation/relevance score; nullable |
| `created_at` | DATETIME | Auto-set on insert |
| `updated_at` | DATETIME | Should be updated on every write |

**Indexes:** `arxiv_id`, `status`

---

### `pages`
All generated wiki-style content pages. A page can be a paper summary, a concept article, a hand-curated narrative, or a daily digest.

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER PK | Auto-increment |
| `page_slug` | TEXT UNIQUE | URL-path identifier, e.g. `papers/zheng-2026-bar-formation`, `concepts/galaxy-bimodality` |
| `title` | TEXT | Human-readable title |
| `page_type` | TEXT | `paper`, `concept`, `page`, or `daily_summary` |
| `source_paper_id` | INTEGER FK → `papers.id` | Set only for pages derived from a specific paper; `SET NULL` on paper delete |
| `path` | TEXT | Filesystem path to the rendered file, if applicable |
| `counters_json` | TEXT | JSON object for arbitrary counters (e.g. link counts) |
| `metadata_json` | TEXT | JSON blob for extra page metadata |
| `created_date` | DATETIME | Auto-set on insert |
| `updated_date` | DATETIME | Should be updated on every write |

**Indexes:** `page_type`

**`page_type` values:**
- `paper` — one summary page per processed paper
- `concept` — extracted concept/topic article (the majority of pages)
- `page` — general narrative or curated page
- `daily_summary` — aggregated digest for a day's papers

---

### `paper_page_links`
Many-to-many join between `papers` and `pages`, with a semantic role label.

| Column | Type | Notes |
|---|---|---|
| `paper_id` | INTEGER FK → `papers.id` | Cascades on delete |
| `page_id` | INTEGER FK → `pages.id` | Cascades on delete |
| `role` | TEXT | Relationship type |

**Primary key:** `(paper_id, page_id)`

**`role` values:**
- `primary` — this page is the paper's own generated page
- `related` — this page is topically related to the paper
- `introduces` — the paper introduces the concept on this page
- `mentions` — the paper mentions this page's topic
- Any other short slug label is valid for domain-specific roles.

---

### `page_links`
Directed hyperlink graph between pages. Supports forward references: `target_page_slug` is a plain TEXT field with no foreign key, so it can point to pages that do not yet exist (stub links).

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER PK | Auto-increment |
| `source_page_id` | INTEGER FK → `pages.id` | Cascades on delete |
| `target_page_slug` | TEXT | Slug of the target page; may not exist in `pages` yet |
| `link_text` | TEXT | Anchor text of the link |
| `created_at` | DATETIME | Auto-set on insert |

**Indexes:** `source_page_id`, `target_page_slug`

To check whether a link is a stub (target does not exist yet):
```sql
SELECT pl.target_page_slug
FROM page_links pl
LEFT JOIN pages p ON pl.target_page_slug = p.page_slug
WHERE p.page_slug IS NULL;
```

---

### `page_tags`
Categorical labels assigned to pages for filtering and grouping. A page can have many tags; a tag can appear on many pages.

| Column | Type | Notes |
|---|---|---|
| `page_id` | INTEGER FK → `pages.id` | Cascades on delete |
| `tag` | TEXT | Tag string, e.g. `Tag_Galaxy_Structure`, `Tag_Secular_Evolution` |

**Primary key:** `(page_id, tag)`  
**Indexes:** `tag`

Tags are freeform strings. By convention, use `Tag_` prefix with `Title_Case` words (e.g. `Tag_Dark_Matter`, `Tag_Quenching_Mechanisms`). They are distinct from concept cross-links — tags classify a page; links express relationships between pages.

**Query all pages with a given tag:**
```sql
SELECT p.page_slug, p.title
FROM page_tags pt
JOIN pages p ON pt.page_id = p.id
WHERE pt.tag = 'Tag_Galaxy_Structure';
```

**Query all tags for a given page:**
```sql
SELECT tag FROM page_tags
WHERE page_id = (SELECT id FROM pages WHERE page_slug = 'pages/bar_formation');
```

---

### `processing_log`
Append-only audit log of pipeline processing attempts per paper.

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER PK | Auto-increment |
| `paper_id` | INTEGER FK → `papers.id` | Cascades on delete |
| `attempt` | INTEGER | Attempt number (1-based) |
| `status` | TEXT | `success`, `error`, or any short status string |
| `message` | TEXT | Human-readable detail or error message |
| `created_at` | DATETIME | Auto-set on insert |

---

### `migrations`
Tracks which schema migrations have been applied.

| Column | Type | Notes |
|---|---|---|
| `version` | INTEGER PK | Migration version number |
| `applied_at` | DATETIME | Auto-set on insert |

When adding new schema migrations, insert a row here with the next version number.

---

### `meta`
Arbitrary key/value configuration store.

| Column | Type | Notes |
|---|---|---|
| `key` | TEXT PK | Setting name |
| `value` | TEXT | Setting value (may be JSON) |

---

## Entity Relationships

```
papers ──< paper_page_links >── pages ──< page_tags
                                  │
                     page_links ──┘ (source)
                     page_links ──→ target_page_slug (may not exist)

papers ──< processing_log
```

- A paper can relate to many pages via `paper_page_links` (with a role).
- A page can link to many other pages via `page_links`; target slugs are not enforced by FK, so stub links are valid.
- Concept pages (`page_type = 'concept'`) are regular rows in `pages` — to "tag" a page with a concept, add a `page_links` row pointing to its slug (e.g. `concepts/galaxy-bimodality`).

---

## Common Queries

**All pages linked from a given page:**
```sql
SELECT target_page_slug, link_text
FROM page_links
WHERE source_page_id = (SELECT id FROM pages WHERE page_slug = 'papers/my-paper');
```

**All pages that link to a given slug:**
```sql
SELECT p.page_slug, pl.link_text
FROM page_links pl
JOIN pages p ON pl.source_page_id = p.id
WHERE pl.target_page_slug = 'concepts/galaxy-bimodality';
```

**Papers and their primary page:**
```sql
SELECT p.arxiv_id, pg.page_slug
FROM papers p
JOIN paper_page_links ppl ON p.id = ppl.paper_id
JOIN pages pg ON ppl.page_id = pg.id
WHERE ppl.role = 'primary';
```

**Unprocessed papers:**
```sql
SELECT arxiv_id, title FROM papers WHERE status = 'pending';
```
