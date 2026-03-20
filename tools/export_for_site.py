"""Export selected DB views into JSON files under src/data/ for Astro SSG consumption.
Also generates public/ static JSON files for client-side search and red-link detection.
Run this prior to `npm run build` to populate static JSON used by the site.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'src' / 'data'
OUT_DIR.mkdir(parents=True, exist_ok=True)
PUBLIC_DIR = ROOT / 'public'
PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

def write_json(name, obj, directory=OUT_DIR):
    p = directory / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
    print('Wrote', p)


def main():
    db_access.migrate()
    write_json('stats.json', db_access.stats())
    write_json('recent_papers.json', db_access.recent_papers(limit=20))
    write_json('papers_index.json', db_access.all_papers_index())
    write_json('pages_index.json', db_access.all_pages_index())
    write_json('paper_pages.json', db_access.paper_pages())
    write_json('daily_summary_pages.json', db_access.daily_summary_pages())
    write_json('page_tags.json', db_access.all_page_tags())

    # --- Client-side static files (served from public/) ---

    # Search index: title + slug for every page
    pages = db_access.all_pages_index()
    search_entries = [
        {'title': p['title'], 'slug': p['page_slug']}
        for p in pages
        if p['page_slug'].startswith('pages/') and '_template' not in p['page_slug']
    ]
    write_json('search-index.json', search_entries, PUBLIC_DIR)

    # Existing slugs: scan disk for actual files; cross-reference DB for titles
    all_pages = db_access.all_pages_index()
    slug_to_title = {}
    for p in all_pages:
        raw = p['page_slug']
        for prefix in ('pages/', 'papers/'):
            if raw.startswith(prefix):
                slug_to_title[raw[len(prefix):]] = p['title']
    src_pages = ROOT / 'src' / 'pages' / 'pages'
    content_pages = ROOT / 'src' / 'content' / 'pages'
    existing: dict[str, str] = {}
    for d in [src_pages, content_pages]:
        if d.exists():
            for f in d.iterdir():
                if f.suffix in ('.astro', '.mdx', '.md') and not f.stem.startswith(('_', '[')):
                    existing[f.stem] = slug_to_title.get(f.stem, f.stem)
    existing_with_titles = [
        {'slug': slug, 'title': title}
        for slug, title in sorted(existing.items())
    ]
    write_json('existing-slugs.json', existing_with_titles, PUBLIC_DIR)


if __name__ == '__main__':
    main()
