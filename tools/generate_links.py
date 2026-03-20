"""Generate links.json for build-time WikiLink resolution.
Only emits {slug: {title, exists}} — the minimum needed for WikiLink.
Full link graph data stays in SQLite; use export_for_site.py for other views.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / 'src' / 'pages'
CONTENT_PAGES = ROOT / 'src' / 'content' / 'pages'
OUT = ROOT / 'src' / 'data' / 'links.json'


def normalize_slug(s):
    """Canonical slug: lowercase, spaces/hyphens → underscores, strip slashes."""
    if s is None:
        return s
    s = s.strip()
    s = s.lstrip('/').rstrip('/')
    s = s.replace(' ', '_').replace('-', '_').lower()
    return s


def scan_disk_pages():
    """Gather page slugs from .astro files under src/pages and .mdx under src/content/pages."""
    slugs = set()
    for p in SRC_PAGES.rglob('*.astro'):
        if p.stem.startswith(('_', '[')):
            continue
        rel = p.relative_to(SRC_PAGES).with_suffix('')
        slug = str(rel).replace('\\', '/').lower()
        slugs.add(normalize_slug(slug))
    if CONTENT_PAGES.exists():
        for p in CONTENT_PAGES.rglob('*.md'):
            slug = 'pages/' + p.stem.lower()
            slugs.add(normalize_slug(slug))
        for p in CONTENT_PAGES.rglob('*.mdx'):
            slug = 'pages/' + p.stem.lower()
            slugs.add(normalize_slug(slug))
    return slugs


def build_link_map():
    slugs_on_disk = scan_disk_pages()
    pages = db_access.all_pages_index()
    page_map = {normalize_slug(p['page_slug']): p for p in pages}

    # Gather all target slugs referenced in page_links
    import sqlite3
    conn = sqlite3.connect(str(db_access.DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT target_page_slug FROM page_links')
    target_slugs = {normalize_slug(r['target_page_slug']) for r in cur.fetchall()}
    conn.close()

    # Slim link map: only title + exists
    link_map = {}
    for slug, p in page_map.items():
        link_map[slug] = {
            'title': p.get('title'),
            'exists': slug in slugs_on_disk,
        }

    # Also include targets that are referenced but not in pages table
    for target in target_slugs:
        if target and target not in link_map:
            link_map[target] = {
                'title': None,
                'exists': target in slugs_on_disk,
            }

    return link_map


def main():
    db_access.migrate()
    lm = build_link_map()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(lm, indent=2, ensure_ascii=False))
    print(f'Wrote {OUT} ({len(lm)} entries)')

if __name__ == '__main__':
    main()
